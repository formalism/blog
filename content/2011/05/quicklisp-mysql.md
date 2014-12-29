Title: quicklisp + mysql メモ
Date: 2011-05-23 14:45:00
Category: 
Tags: Programming,Lisp
Slug: quicklisp-mysql

自分用のメモ。<br /><br />quicklispでmysqlに接続するには、cl-msyqlというパッケージかclsqlを使う。cl-mysqlはまだprepared statementが実装されていなさそう(嘘かも)。なのでclsqlを使う。<br /><br />(ql:quickload "clsql")ではuffi(lispからC関数を呼び出すためのライブラリ?)やmysqlへの接続用ダイナミックライブラリを作るのに<b>Cコンパイラとmakeが必要</b>。それと<b>mysql.h</b>が無いと、clsqlに含まれているclsql_mysql.cのコンパイルができない(これはdb-mysqlディレクトリにclsql_mysql.soが存在するかで確認する)。しかし、これらのコンパイルに失敗しても(ql:quickload "clsql")自体はエラーを出力しないようだ。実際にclsql:connectをするときにエラーになる。とにかく原因追求が大変だった。
