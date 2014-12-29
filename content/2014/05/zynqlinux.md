Title: Zynq上でのLinuxアプリケーションのデバッグ方法
Date: 2014-05-07 14:40:00
Category: 
Tags: Zynq,Linux,TCF
Slug: zynqlinux

やっとZYBO上でLinuxが(Ethernetも含めて)動作するようになった。これについては別の記事でまとめることにするが、一番気になっていたのは、LinuxアプリケーションのデバッグがXilinxのSDKから簡単に可能かどうかだった。<br /><br />現在(2014.1)のSDKにはGDB, System Debuggerという2種類のデバッグ方法が用意されている。GDBでのデバッグは可能だったが、System Debuggerでは出来なかった。こちらの<a href="http://t.co/pq8oQ2lBwx">ビデオ</a>によると、System DebuggerでLinuxアプリケーションをデバッグしている。スレッド単位でブレークを掛けたりすることもできる様子で、なかなか強力だと思う。<br /><br />一方、<a href="http://t.co/VrNdQfhC09">System Debugger Limitations, Known Issues, and FAQs</a>によると、2013.4の時点ではSystem DebuggerでのLinuxアプリケーションのデバッグはできないように思われる。2014.1については情報は見つからなかった。<br /><br />上記のビデオでは実現できていることからすると、これが可能になったのはごく最近のことであると思われる。ビデオをよく見てみると、Yocto Linuxが起動しているのが分かる。また、TCF(System Debuggerが使用するフレームワークの仕様)のためのagentが最後の方で起動しているのも分かる。<br /><br />とりあえず自分の要件としてはGDBでも良いが、System Debuggerについても時間があるときに調査してみたい。<br /><br />また、<b>GDB, System Debuggerどちらの方法をとるにせよ、ZynqのLinux側でEthernetが使えていないとデバッグできないので注意</b>(これを知ったので、なんとかしてEthernetを動かしたかった)。hw_serverをホスト側で動かせばSystem Debuggerできるのでは？と妄想したが、どうもhw_serverではダメらしい。
