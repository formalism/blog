Title: NIOS+DDR2
Date: 2010-10-18 05:50:00
Category: 
Tags: Programming,FPGA
Slug: niosddr2

これまでNIOS2を使ったシステムでDDR2コントローラを使うときには、コントローラはAvalonバスに接続せずに、CPU外に置いていた。今回、ちょっと思い立ってAvalonバスに接続して試してみることにした。<br /><br />しかしはまった点がある。インプリメントしたSOFをボードにダウンロードするまでは良いのだが、Nios II IDEからファームをダウンロードして実行しようとしても、target processor not responding(正確ではないかも)のようなメッセージが出て、CPUが動作しない。いろいろ試して検索してみた結果、DDR2コントローラのポートglobal_reset_n_to_the_altmemddr_0をCPUからPIOで操作しようとしているのが悪さをしているらしいと分かった。これをFPGA端子に入力されているRSTnピンにしたら、ファームのダウンロードもできるようになった。これで半日つぶれてしまった。
