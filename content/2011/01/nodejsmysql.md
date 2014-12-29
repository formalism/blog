Title: node.js+MySQLで文字化け
Date: 2011-01-21 08:57:00
Category: 
Tags: Programming
Slug: nodejsmysql

node.jsからMySQLを使用して、昔にRoRで作成したアプリと同等のものを(同じデータベースを使って)作ろうとしているが、いろいろやっても文字化けが解決できなかった。ひたすら検索し、<a href="http://www.gcd.org/blog/2009/09/177/">仙石浩明の日記  2009年9月14日 文字化けしていなくても MySQL 内の文字コードが正しくない場合がある</a>を見て、ついに原因が判明した。結局、既存のRoRで作成したアプリが、latin1でMySQLとやりとりしているのが原因だった。実際に、mysqldumpでデータベースをダンプする際に、--default-character-set=latin1を追加したら、文字化けしなかった。というわけで、根本的に解決するには、データベースのデータをちゃんとUTF8にすることだけれど、ひとまず、node.jsのプログラム側で、set names latin1というクエリを送って、RoRと同じ動作にさせたら、文字化けが直った。
