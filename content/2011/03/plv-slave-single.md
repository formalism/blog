Title: PLB slave single
Date: 2011-03-11 01:33:00
Category: 
Tags: Programming,FPGA
Slug: plv-slave-single

plbv46_slave_singleの自分用のメモ<br /><br />ARD: Address Range Definition。アドレスデコードとチップセレクト信号を生成する。<br />C_ARD_ADDR_RANGE_ARRAY, C_ARD_NUM_CE_ARRAYは、VHDLのunconstrained arrayとして定義される。これら二つの配列のそれぞれ対応するインデックスのアドレスとチップセレクトが結び付けられる。<br /><br /><b>C_ARD_ADDR_RANGE_ARRAY</b>: 2データで1ペア。それぞれ、<b>ベースアドレス</b>と<b>ハイアドレス</b>。このアドレスは、バイトアドレスで指定する。ブロックサイズ(ハイアドレス-ベースドレス+1)は2の累乗でないといけない。ベースアドレスは、ブロックサイズの倍数のアドレスでないといけない。<br /><br /><b>C_ARD_NUM_CE_ARRAY</b>: それぞれのアドレススペースで必要なチップセレクトの数を指定する。それぞれの値は2の累乗でないといけない。各アドレススペースは、少なくとも1つのチップセレクトがないといけない。各アドレススペースは、チップセレクトの数で分割される。<br /><br />結局これらの配列の値は、Create or Import Peripheralでテンプレートを生成すると、一応genericで定義されるが、実際はXPSでインスタンスを作るときに決まる。
