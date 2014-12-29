Title: Zynq USBデバイステスト (ファームウェア)
Date: 2014-04-30 09:33:00
Category: 
Tags: Zynq,Programming,FPGA
Slug: zynq-usb

[Zynq USBデバイステスト (PC側ソフトウェア)]({filename}./zynqusb.md)の続き。

C:\Xilinx\SDK\2014.1\data\embeddedsw\XilinxProcessorIPLib\drivers\usbps_v2_0 のexamplesに対するパッチ。
usbMain関数を呼び出すと動作開始。examplesのファイル達はusbフォルダにコピーされたものとする。

概要としては、examplesはUSB mass storageとして動作するので、バルク転送のTX/RX割り込みがかかるところを
横取り(XUsbPs_HandleStorageReqをコメントにする)して、所望のデータ処理に置き換える。
また、サンプルはTX割り込みがかからないようになっているので、TXのビットをorして有効にする。

------------------------------

diff -cr examples/xusbps_ch9_storage.c usb/xusbps_ch9_storage.c

    :::diff
    examples/xusbps_ch9_storage.c    2014-04-16 23:53:27.579740500 +0900
    --- usb/xusbps_ch9_storage.c    2014-04-30 13:40:18.515248827 +0900
    **
    171,177 *
              0x00,                / bDeviceSubClass /
              0x00,                / bDeviceProtocol /
              USB_ENDPOINT0_MAXP,        / bMaxPackedSize0 /
    !         be2les(0x0d7d),            / idVendor /
              be2les(0x0100),            / idProduct /
              be2les(0x0100),            / bcdDevice /
              0x01,                / iManufacturer /
    --- 171,177 ----
              0x00,                / bDeviceSubClass /
              0x00,                / bDeviceProtocol /
              USB_ENDPOINT0_MAXP,        / bMaxPackedSize0 /
    !         be2les(0xABCD),            / idVendor /
              be2les(0x0100),            / idProduct /
              be2les(0x0100),            / bcdDevice /
              0x01,                / iManufacturer */
    ***
    227,235 *
               0x00,                / bInterfaceNumber /
               0x00,                / bAlternateSetting /
               0x02,                / bNumEndPoints /
    !          0x08,                / bInterfaceClass /
    !          0x06,                / bInterfaceSubClass /
    !          0x50,                / bInterfaceProtocol /
               0x05},                / iInterface /
      
              / Bulk Out Endpoint Config /
    --- 227,235 ----
               0x00,                / bInterfaceNumber /
               0x00,                / bAlternateSetting /
               0x02,                / bNumEndPoints /
    !          0xFF,                / bInterfaceClass 08->FF /
    !          0x00,                / bInterfaceSubClass 06->00 /
    !          0x00,                / bInterfaceProtocol 50->00 /
               0x05},                / iInterface /
      
              / Bulk Out Endpoint Config */
    ***
    285,295 *
      
          static char StringList[] = {
              "UNUSED",
    !         "Xilinx",
    !         "EPB USB Flash Drive Disk Emulation",
              "2A49876D9CC1AA4",
              "Default Configuration",
    !         "Default Interface",
          };
          char String;
          u32 StringLen;
    --- 285,295 ----
      
          static char StringList[] = {
              "UNUSED",
    !         "abstract",
    !         "Image Converter",
              "2A49876D9CC1AA4",
              "Default Configuration",
    !         "Image Inteface",
          };
          char *String;
          u32 StringLen;
    diff -cr examples/xusbps_intr_example.c usb/xusbps_intr_example.c
    examples/xusbps_intr_example.c    2014-04-16 23:53:27.661745200 +0900
    --- usb/xusbps_intr_example.c    2014-04-30 18:06:36.810127803 +0900
    **
    122,128 
       
       ***********/
      
    ! int main(void)
      {
          int Status;
      
    --- 122,128 ----
       
       ***********/
      
    ! int usbMain(void)
      {
          int Status;
      
    **
    290,296 
      
          / Set the handler for receiving frames. /
          Status = XUsbPs_IntrSetHandler(UsbInstancePtr, UsbIntrHandler, NULL,
    !                         XUSBPS_IXR_UE_MASK);
          if (XST_SUCCESS != Status) {
              goto out;
          }
    --- 290,296 ----
      
          / Set the handler for receiving frames. /
          Status = XUsbPs_IntrSetHandler(UsbInstancePtr, UsbIntrHandler, NULL,
    !                         XUSBPS_IXR_UE_MASK);    // notify transaction error
          if (XST_SUCCESS != Status) {
              goto out;
          }
    **
    310,316 
            been sent.
           /
          Status = XUsbPs_EpSetHandler(UsbInstancePtr, 1,
    !                 XUSBPS_EP_DIRECTION_OUT,
                      XUsbPs_Ep1EventHandler, UsbInstancePtr);
      
          / Enable the interrupts. /
    --- 310,316 ----
            been sent.
           /
          Status = XUsbPs_EpSetHandler(UsbInstancePtr, 1,
    !                 XUSBPS_EP_DIRECTION_OUT | XUSBPS_EP_DIRECTION_IN,    // Add XUSBPS_EP_DIRECTION_IN
                      XUsbPs_Ep1EventHandler, UsbInstancePtr);
      
          / Enable the interrupts. /
    **
    411,417 
          u32    BufferLen;
          u32    Handle;
      
    - 
          Xil_AssertVoid(NULL != CallBackRef);
      
          InstancePtr = (XUsbPs ) CallBackRef;
    --- 411,416 ----
    **
    476,485 
          u32    BufferLen;
          u32 InavalidateLen;
          u32    Handle;
    ! 
      
          Xil_AssertVoid(NULL != CallBackRef);
    - 
          InstancePtr = (XUsbPs ) CallBackRef;
      
          switch (EventType) {
    --- 475,484 ----
          u32    BufferLen;
          u32 InavalidateLen;
          u32    Handle;
    !     static u8 TempBuf[2561024];
    !     static u32 BufPtr = 0;
      
          Xil_AssertVoid(NULL != CallBackRef);
          InstancePtr = (XUsbPs ) CallBackRef;
      
          switch (EventType) {
    **
    493,509 
                  InavalidateLen = (BufferLen/32) * 32 + 32;
              }
      
    !         Xil_DCacheInvalidateRange((unsigned int)BufferPtr,
    !                                     InavalidateLen);
              if (XST_SUCCESS == Status) {
                  / Handle the storage class request. /
    !             XUsbPs_HandleStorageReq(InstancePtr, EpNum,
    !                             BufferPtr, BufferLen);
                  / Release the buffer. /
                  XUsbPs_EpBufferRelease(Handle);
              }
              break;
    - 
          default:
              / Unhandled event. Ignore. /
              break;
    --- 492,527 ----
                  InavalidateLen = (BufferLen/32) * 32 + 32;
              }
      
    !         Xil_DCacheInvalidateRange((unsigned int)BufferPtr, InavalidateLen);
              if (XST_SUCCESS == Status) {
                  / Handle the storage class request. /
    ! //            XUsbPs_HandleStorageReq(InstancePtr, EpNum, BufferPtr, BufferLen);
    ! 
    !             memcpy(&TempBuf[BufPtr], BufferPtr, BufferLen);
    !             BufPtr += BufferLen;
    !             if (BufPtr >= 2561024){
    !                 BufPtr = 0;
    !                 XUsbPs_EpBufferSend(InstancePtr, 1, &TempBuf[BufPtr], 512);    // loopback
    !                 BufPtr += 512;
    !             }
    ! 
                  / Release the buffer. /
                  XUsbPs_EpBufferRelease(Handle);
    +         }else{
    +             xil_printf("XUsbPs_EpBufferReceive: %X\n", Status);
    +         }
    +         break;
    +     case XUSBPS_EP_EVENT_DATA_TX:    // IN finish
    +         if (BufPtr < 2561024){
    +             Status = XUsbPs_EpBufferSend(InstancePtr, 1, &TempBuf[BufPtr], 512);
    +             if (Status != XST_SUCCESS){
    +                 xil_printf("XUsbPs_EpBufferSend: %X\n", Status);
    +             }
    +             BufPtr += 512;
    +         }else{
    +             BufPtr = 0;    // clear Pointer
              }
              break;
          default:
              / Unhandled event. Ignore. /
              break;
    
