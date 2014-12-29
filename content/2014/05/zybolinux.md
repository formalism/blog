Title: ZYBOでLinux (使用メモリを制限)
Date: 2014-05-21 14:37:00
Category: 
Tags: Zynq,Linux
Slug: zybolinux

Zynq上でPLにロジックを自作してDMA処理を行う場合、アプリケーションからレジスタを操作するために最も手軽
なのは、[以前書いたとおり]({filename}./zynqpllinux-dts.md) UIOを使用することだと思う。

このような場合、ロジックで使用するメモリ領域はLinuxが使用する領域と完全に分けておいた方が
(少なくとも自分のような初心者には)楽だ。このためには、実装されているメモリより少ない領域を
使用するようにLinuxを構成しないといけない。

今回は、ZYBOで512MB実装されているところを256MBだけLinuxに割り当てた。しかし、結構これにはまった。
やり方は、以前の通りXilinx純正gitをcloneしてxilinx-v2014.1をcheckout。zynq-zed.dtsを編集し、
ps-clk-frequencyを変更するまでは同じ。bootargsを

    :::text
    console=ttyPS0,115200 root=/dev/ram rw earlyprintk

となっているのを、

    :::text
    console=ttyPS0,115200 mem=256M root=/dev/ram rw earlyprintk

とする。また、ps7_ddr_0: memory@0をreg = <0x0 0x20000000="">;からreg = <0x0 0x10000000="">;に変更する。
カーネルのコンパイルは、<a href="http://www.wiki.xilinx.com/Build+Kernel">こちら</a>に従い、 
uImageを作成する。u-bootについては変更不要。

ramdiskについては、<a href="http://www.wiki.xilinx.com/Build+and+Modify+a+Rootfs">こちら</a>の方法で
uramdisk.image.gzにしておく。

XMDからブートする場合、

    :::text
    connect arm hw
    rst -slcr
    fpga -f system_wrapper.bit
    source ps7_init.tcl
    ps7_init
    ps7_post_config
    source stub.tcl
    targets 64
    dow -data u-boot-Digilent-Dev/u-boot.bin 0x04000000
    #dow -data fit.itb 0x02000000 (これは以前のやり方)
    dow -data linux-xlnx/arch/arm/boot/uImage 0x03000000
    dow -data uramdisk.image.gz 0x02000000
    dow -data linux-xlnx/arch/arm/boot/dts/zynq-zed.dtb 0x02a00000
    con 0x04000000

でu-bootが起動する。bootmする前に、setenv fdt_high 0xFFFFFFFF, setenv initrd_high 0xFFFFFFFFとしておく。
最後に、

    :::text
    u-boot> bootm 0x3000000 0x2000000 0x2a00000

とすると、Linuxが256MBだけ使用して起動する。つまり、[以前の方法]({filename}./linux-on-zynq-zybo.md) だと
fit.itbを作成して、それをロードしていたが、今回のやり方だとu-bootから直接それぞれのイメージアドレスを
入力することでLinuxを起動している。

fit.itbを使用する方法でもいろいろ試行錯誤してみたが、試した範囲ではカーネルパニックをおこしたり、
デバイスツリーが読めなかったりで、どうしても思い通りにならなかった。
