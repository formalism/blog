Title: 位相相関による画像位置合わせ
Date: 2012-04-05 04:33:00
Category: 
Tags: Programming
Slug: image-registration-phase-correlation

メモ。<br /><br />平行移動している2つの画像の移動量を検出する方法について調査しいていたら、位相相関法というのが見つかった。<br /><br /><a href="http://nashruddin.com/phase-correlation-function-in-opencv.html">Phase Correlation in OpenCV</a><br /><br /><a href="http://wwww.vis.ne.jp/mt/archives/000680.html">高速フーリエ変換ライブラリ FFTW ver 3 の使い方</a><br /><br /><a href="http://en.wikipedia.org/wiki/Phase_correlation">Phase correlation</a><br /><br /><a href="http://www.aoki.ecei.tohoku.ac.jp/%7Eito/vol1_030.pdf">位相限定相関法に基づく高精度マシンビジョン</a><br /><br />英語ではこのような処理を一般にimage registrationと呼ぶらしい。これを行うには、上記のように周波数領域で行う以外にも、いろいろな方法が提案されている。実際に上記のページのソースを参考にプログラムを作成してみたら、ちゃんとずれ量を検出できた。<br /><br/><SCRIPT charset="utf-8" type="text/javascript" src="http://ws.amazon.co.jp/widgets/q?rt=qf_sp_sr_mfw&ServiceVersion=20070822&MarketPlace=JP&ID=V20070822/JP/formalism-22/8001/d7bb008a-a0a8-4a3e-b024-32fc532c0d5a"> </SCRIPT> <NOSCRIPT><A HREF="http://ws.amazon.co.jp/widgets/q?rt=qf_sp_sr_mfw&ServiceVersion=20070822&MarketPlace=JP&ID=V20070822%2FJP%2Fformalism-22%2F8001%2Fd7bb008a-a0a8-4a3e-b024-32fc532c0d5a&Operation=NoScript">Amazon.co.jp ウィジェット</A></NOSCRIPT>
