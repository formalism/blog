Title: C to Verilog (2)
Date: 2011-03-10 05:35:00
Category: 
Tags: Programming,FPGA
Slug: c-to-verilog-2

<b><span class="Apple-style-span" style="font-size: large;">合成の問題(?)について</span></b><br />C to Verilogを試していると、メモリの制御信号がDon't Careになってしまうことがあると分かった。いろいろ入力となるCプログラムを変えてみたら、どうやらfor<b>ループの中にcontinueがあるとうまくいかない</b>らしい、ということが分かった。ひょっとしたらbreakもだめなのかな？<br /><br /><b><span class="Apple-style-span" style="font-size: large;">メモリ(RAM)の使用について</span></b><br />C to Verilogでは、ポインタはRAMとして生成され、テストベンチの中にはRAMの宣言もある。このRAMはポート数は可変のようだが、タイミングは固定されてしまっている。つまり、同期書き込み、<b>非同期読み出し</b>のメモリでないと、期待したタイミングとずれてしまう。そして、Xilinxの場合、BRAMは<b>同期読み出し</b>である。したがって、C to Verilogで生成されたプログラムを使用する場合は、<b>BRAMは使用できない。</b>その代わりに、分散RAMを使用する。これであればdual-portメモリもOK。でも、dual-port設定時にC to Verilogで生成されるRAMのモジュールは、Write Enable信号が2つある。分散RAMは、書き込みは1ポートだけしか使えない。それで、片方のWrite Enable信号は除く必要がある。<br /><br />しかも、C to Verilogで生成されるxramの定義にはバグがある。メモリは配列として宣言されるが、配列の要素数の括弧が無いので、本来の要素数を持つ配列が定義されない。明示的に括弧をつける必要がある。
