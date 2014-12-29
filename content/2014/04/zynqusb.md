Title: ZynqでのUSBデバイステスト (PC側ソフトウェア)
Date: 2014-04-30 09:15:00
Category: 
Tags: Programming
Slug: zynqusb

Zynqに内蔵されているUSBポートをデバイスモードで使用できるかテスト中。

とりあえず最低限のループバックでは動作したので、汚いがコードを貼っておく。

まずは、WinUSBを使用したPC側のソース。ほぼMicrosoftのドキュメントをくっつけただけ。インクルードの順番だけは結構重要だったりする。winusb.lib, setupapi.libをリンクすること。

ドライバはインストール済みの前提。

-----------------------------------------

    :::c
    #include "stdafx.h"
    //#include "usb.h"
    #include "windows.h"
    #include "usb100.h"
    #include "usb200.h"
    #include "SetupAPI.h"
    #include "winusb.h"
    #include "winusbio.h"
    #include "strsafe.h"
    
    #define MAX_DEVPATH_LENGTH (1024)
    
    // {9F68AD5A-84E0-4E0F-8EF3-11139532FD22}
    GUID GUID_DEVINTERFACE_OSRUSBFX2 = { 0x9F68AD5AUL, 0x84E0, 0x4E0F, { 0x8E, 0xF3, 0x11, 0x13, 0x95, 0x32, 0xFD, 0x22 } };
    
    typedef struct _DEVINFO {
        WINUSB_INTERFACE_HANDLE winUSBHandle;
        UCHAR deviceSpeed;
        UCHAR bulkInPipe, bulkOutPipe, interruptPipe;
    } DEVINFO;
    static DEVINFO devInfo;
    
    BOOL GetDevicePath(LPGUID InterfaceGuid, PCHAR DevicePath, size_t BufLen)
    {
        BOOL bResult = FALSE;
        HDEVINFO deviceInfo;
        SP_DEVICE_INTERFACE_DATA interfaceData;
        PSP_DEVICE_INTERFACE_DETAIL_DATA detailData = NULL;
        ULONG length;
        ULONG requiredLength = 0;
        HRESULT hr;
    
        // [1]
        deviceInfo = SetupDiGetClassDevs(InterfaceGuid, NULL, NULL,
                                        DIGCF_PRESENT | DIGCF_DEVICEINTERFACE);
        //Error handling code omitted.
    
        // [2]
        interfaceData.cbSize = sizeof(SP_DEVICE_INTERFACE_DATA);
    
        bResult = SetupDiEnumDeviceInterfaces(deviceInfo,
                                    NULL, InterfaceGuid, 0, &interfaceData);
        //Error handling code omitted.
    
        // [3]
        SetupDiGetDeviceInterfaceDetail(deviceInfo,
            &interfaceData,
            NULL, 0,
            &requiredLength,
            NULL);
    
        detailData = (PSP_DEVICE_INTERFACE_DETAIL_DATA)LocalAlloc(LMEM_FIXED, requiredLength);
    
        if (NULL == detailData)
        {
            SetupDiDestroyDeviceInfoList(deviceInfo);
            return FALSE;
        }
    
        detailData->cbSize = sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA);
        length = requiredLength;
    
        bResult = SetupDiGetDeviceInterfaceDetail(deviceInfo,
            &interfaceData,
            detailData,
            length,
            &requiredLength,
            NULL);
    
        if (FALSE == bResult)
        {
            LocalFree(detailData);
            return FALSE;
        }
    
        // [4]
        hr = StringCchCopy((LPTSTR)DevicePath, BufLen, detailData->DevicePath);
        if (FAILED(hr))
        {
            SetupDiDestroyDeviceInfoList(deviceInfo);
            LocalFree(detailData);
        }
    
        LocalFree(detailData);
    
        return bResult;
    }
    
    HANDLE OpenDevice(BOOL bSync){
        HANDLE hDev = NULL;
        char devicePath[MAX_DEVPATH_LENGTH];
        BOOL retVal;
    
        retVal = GetDevicePath((LPGUID)&GUID_DEVINTERFACE_OSRUSBFX2,
            devicePath,    sizeof(devicePath));
        //Error-handling code omitted.
    
        hDev = CreateFile((LPCWSTR)devicePath,
            GENERIC_WRITE | GENERIC_READ,
            FILE_SHARE_WRITE | FILE_SHARE_READ,
            NULL,
            OPEN_EXISTING,
            FILE_ATTRIBUTE_NORMAL | FILE_FLAG_OVERLAPPED,
            NULL);
    
        //Error-handling code omitted.
        return hDev;
    }
    
    BOOL Initialize_Device(){
        BOOL bResult;
        WINUSB_INTERFACE_HANDLE usbHandle;
        USB_INTERFACE_DESCRIPTOR ifaceDescriptor;
        WINUSB_PIPE_INFORMATION pipeInfo;
        UCHAR speed;
        ULONG length;
    
        HANDLE deviceHandle = OpenDevice(TRUE);
        bResult = WinUsb_Initialize(deviceHandle, &usbHandle);
    
        //[1]
        if (bResult)
        {
            devInfo.winUSBHandle = usbHandle;
            length = sizeof(UCHAR);
            bResult = WinUsb_QueryDeviceInformation(usbHandle, DEVICE_SPEED, &length, &speed);
            devInfo.deviceSpeed = speed;
        }
    
        //[2]
        if (bResult)
        {
            bResult = WinUsb_QueryInterfaceSettings(usbHandle, 0, &ifaceDescriptor);
        }
        if (bResult)
        {
            for (int i = 0; i  < ifaceDescriptor.bNumEndPoints; i++)   {
                //[3]
                bResult = WinUsb_QueryPipe(usbHandle, 0, (UCHAR)i, &pipeInfo);
                //[4]
                if (pipeInfo.PipeType == UsbdPipeTypeBulk &&
                    USB_ENDPOINT_DIRECTION_IN(pipeInfo.PipeId))
                {
                    devInfo.bulkInPipe = pipeInfo.PipeId;
                }
                else if (pipeInfo.PipeType == UsbdPipeTypeBulk &&
                    USB_ENDPOINT_DIRECTION_OUT(pipeInfo.PipeId))
                {
                    devInfo.bulkOutPipe = pipeInfo.PipeId;
                }
                else if (pipeInfo.PipeType == UsbdPipeTypeInterrupt)
                {
                    devInfo.interruptPipe = pipeInfo.PipeId;
                }
                else
                {
                    bResult = FALSE;
                    break;
                }
            }
        }
    
        return bResult;
    }
    
    #define BUFSZ (2561024)
    
    int _tmain(int argc, _TCHAR argv[])
    {
        ULONG bytesWritten;
        unsigned int buf[BUFSZ / 4], buf2[BUFSZ / 4];
    
        BOOL result = Initialize_Device();
        srand(0xF3ab1541);
        for (int i = 0; i < BUFSZ/4; i++)
            buf[i] = rand();
    
        result = WinUsb_WritePipe(devInfo.winUSBHandle, devInfo.bulkOutPipe, 
                                    (PUCHAR)buf, sizeof(buf), &bytesWritten, NULL);
        if (result && bytesWritten == sizeof(buf)){
            for (int i = 0; i < BUFSZ/4; i++) buf2[i] = 0;
    
            result = WinUsb_ReadPipe(devInfo.winUSBHandle, devInfo.bulkInPipe,
                                    (PUCHAR)buf2, sizeof(buf2), &bytesWritten, NULL);
            if (result && bytesWritten == sizeof(buf2)){
                for (int i = 0; i < BUFSZ/4; i++)
                    if (buf[i] != buf2[i])
                        printf("Data mismatch: %d\n", i);
            }else{
                printf("Receive error\n");
            }
        }else{
            printf("Send error\n");
        }
        FILE fd, fd2;
        fopen_s(&fd, "buf.txt", "w");
        fopen_s(&fd2, "buf2.txt", "w");
        char tmp[128];
        for (int i = 0; i < BUFSZ / 4; i++){
            int len = sprintf_s(tmp, "0x%08X\n", buf[i]);
            fwrite(tmp, len, 1, fd);
            len = sprintf_s(tmp, "0x%08X\n", buf2[i]);
            fwrite(tmp, len, 1, fd2);
        }
        fclose(fd);
        fclose(fd);
    
        return 0;
    }
    