Title: ZYBOのSDカードブート
Date: 2014-05-21 14:47:00
Category: 
Tags: Zynq,Linux
Slug: zybosd

引き続き、SDカードからのLinuxブートを試してみた。<br /><br /><a href="https://github.com/Digilent/u-boot-Digilent-Dev">Digilentのu-boot</a>のxilinx-v2013.4をチェックアウトしたものでは、ZYBOのu-bootはSD起動にジャンパ設定されていると、SDカード内にuImage, devicetree.dtb, uramdisk.image.gzというファイルを探して、それをメモリに展開、Linuxをブートしてくれるようになっている(printenvで確認可能)。<br /><br />したがって、BOOT.binにはカーネルやramdisk, devicetreeは必要ではなくて、FSBLと(必要であれば)FPGAのbitstream, u-bootだけが入っていればよい。BOOT.binの作り方については、基本的に<a href="http://www.wiki.xilinx.com/Prepare+Boot+Image">こちらに記載されている方法</a>に従えばよい。<br /><br />以上でSDカードからのブートが出来るようになった。<br /><br />
