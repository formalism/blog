Title: Avalonバスのメモ
Date: 2010-03-04 06:31:00
Category: 
Tags: FPGA
Slug: avalon

<b>Avalon-MMのバス幅</b><br /><br />マスターが32bitでスレーブが16bitの場合、マスター側で32bit readを行うと、スレーブ側では16bit readが2回発行される。このようになるので、マスター側から見ると、スレーブのデータ空間のアドレスは連続して見える。(Avalon Interface Specifications 3.6.1)
