Title: HaskellのMySQLバインディングについて調査
Date: 2012-02-08 14:33:00
Category: 
Tags: Programming,Haskell
Slug: haskellmysql

HaskellでMySQLを使うのにどのライブラリが良いか調べた。結果としては<a href="http://hackage.haskell.org/packages/archive/mysql-simple/0.2.2.3/doc/html/Database-MySQL-Simple.html">mysql-simple</a>が良さそうだ。<a href="http://hackage.haskell.org/package/HDBC-mysql-0.6.6.0">HDBC-mysql</a>も試して見たが、こちらは日本語が文字化けしてしまった。ソースを見る限りちゃんとUTF8の変換を行っているように思えたのだが。とりあえず使えるものが見つかったので今日の所はここまで。<br /><br />2012/2/14 追記<br /><br />Mac OS Xの方でmysql-simpleをインストールしたが、コンパイル/リンクされたファイルを実行しようとしたら、libmysqlclient.18.dylibが見つからないというエラーが発生した。このファイルがあるディレクトリをDYLD_LIBRARY_PATH環境変数で指定してみたが、なぜか解決しなかったので、<a href="http://d.hatena.ne.jp/yinkyweb/20111108/1320725744">"Library not loaded: libmysqlclient.18.dylib"の解消方法</a>にあった方法を使って、/usr/libにシンボリックリンクを作成して逃げた。<br /><br />どうにもMac OS XはLinuxと比べて面倒に遭遇する場合が多いと感じる。
