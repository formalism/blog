Title: Xilinx Flashコンフィグレーション
Date: 2011-03-29 10:01:00
Category: 
Tags: Programming,FPGA
Slug: xilinx-flash

自分のメモ。<br /><br /><b>回路</b><br />Slave Serialモード。XCF32クロックを接続。<br /><br /><b>ソフトウェア</b><br />ISEプロジェクトにELFファイルを追加すると、bitファイルにELFが埋め込まれる。Generate Programming Fileのプロパティで圧縮オプションを有効にする。iMPACTで、Create PROM Fileでbitからmcsファイルを生成。できたmcsファイルをxcf32pにアサインしてProgram。
