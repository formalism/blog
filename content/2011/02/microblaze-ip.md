Title: MicroBlaze + IPコア
Date: 2011-02-18 02:47:00
Category: 
Tags: Programming,FPGA
Slug: microblaze-ip

XilinxのMicroblazeに自作IPコアをどのように接続するかを調査中。いろいろ検索してみたが、要領よくまとまっている資料が見つからなかった。<div><br /><div>最新はAXIというARMのバスらしい。しかしこれは最新のFPGAにしか対応していないようだ。AlteraはAvalonかCustom Instructionくらいしかなかったが、Xilinxはしょっちゅうバスを入れ替えている。OPB, PLB, AXI, FSL。FSLはMicroBlazeにPoint-to-Pointで接続するので、残りとは少し違う。AlteraのCustom Instructionと同じような目的で使うために準備しているらしい。FSLのI/Fを使ってやりとりするのが一番簡単そうではある。でもこれだとCPUの介在がワードごとに必要なので、DMAで使えない。でも<a href="http://www.xilinx.com/support/documentation/ip_documentation/plb2fsl_bridge.pdf">PLB to FSL bridge</a>というのがあるので、FSL I/Fで作ったIPコアをPLBに接続することもできるっぽい。これでやってみようかと思う。ただ、PLB to FSL bridgeのデータシートは古いので、最新のISE12.4でも使えるのか、というのが少し不安。</div></div>
