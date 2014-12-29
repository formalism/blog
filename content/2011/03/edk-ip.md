Title: XPS IPコアでのVerilogモジュールの使用
Date: 2011-03-14 03:51:00
Category: 
Tags: Programming,FPGA
Slug: edk-ip

EDKで自作IPコアの使用を試している。Create or Import Peripheralを使用し、VHDLでuser_logic.vhdを作成する。user_logic.vhdからVerilogで記述された回路を使用したい。PAOファイルにVerilogファイルを記述したり、MPDファイルにVerilogも使用する設定の記述などを行ったが、どうやってもISEでコンパイルできなかった。<br /><br />結局、IPコアとして埋め込むのはあきらめて、MicroBlazeのxmpがISEでトップレベルファイルになっていたのをやめて、MicroBlazeのstubファイルをトップレベルにし、普通にISEプロジェクトにVerilogのファイルを追加したらOKになった。<br /><br /><b>後日記</b><br /><b><br /></b><br />上記の方法でまたおかしくなってしまったのが、もう一度挑戦したら、最初に試みた方法でできるようになった。ただし、verilogのソースを変更したときは、implementationフォルダにあるngcファイルと、その中のcacheフォルダにあるファイルを削除してからgenerate netlistしないと、変更が反映されない。
