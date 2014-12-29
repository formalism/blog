Title: ZFSでのCIFS共有
Date: 2009-09-07 04:26:00
Category: 
Tags: OpenSolaris
Slug: zfscifs

Windowsで使用するファイルなども含めて、すべてのデータはこれまでLinuxで管理<br />してきたが、Solarisに心惹かれるものがあるので、数年ぶりに環境を移行した。<br /><br />使用したのはOpenSolaris 2009.06で、もちろんZFS!最近ファイルシステムが一杯になってきていたので、これで一安心。いくらでもディスク追加ができるのは素晴らしい。<br /><br />でも早速CIFSでWindowsからファイルを共有するのにつまづいた。共有を有効にすること自体は、<br /><a href="http://blogs.sun.com/timthomas/ja/entry/opensolaris_cifs_%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%92%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%83%A2%E3%83%BC%E3%83%89%E3%81%A7%E6%A7%8B%E6%88%90">http://blogs.sun.com/timthomas/ja/entry/opensolaris_cifs_%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%92%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%83%A2%E3%83%BC%E3%83%89%E3%81%A7%E6%A7%8B%E6%88%90<br /></a>この記事を基本にして設定できた。<br /><br />問題は、ファイルをWindows側で作成/変更したりするときに発生した。要するに、OpenSolarisのCIFSサーバは、ZFSのACLにユーザをマップする(らしい)が、これは"普通の"ユーザ、グループ、everyoneのパーミッションとは異なる。分かりやすい記事が、<br /><a href="http://cuddletech.com/blog/pivot/entry.php?id=939">http://cuddletech.com/blog/pivot/entry.php?id=939</a><br />にあった。<br /><br />これらを参考にして、Windows側からも、Solaris側からもファイルを操作できるようになった。
