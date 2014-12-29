Title: blaze-htmlでのname属性
Date: 2012-07-10 14:56:00
Category: 
Tags: Programming,Haskell
Slug: blaze-htmlname

 blaze-htmlでname属性の値を設定するときに、コンパイルエラーが出てしまった。次のようなエラー。<br /><br /><pre>    Couldn't match expected type `H.AttributeValue'<br />                with actual type `[a0]'<br />    In the return type of a call of `concat'<br />    In the second argument of `($)', namely<br />      `concat ["s", show y, "-", show m, ....]'<br />    In the expression: A.name $ concat ["s", show y, "-", show m, ....]&nbsp;<br /></pre><br />concatを使って、name属性の値になってほしい文字列を作っているのだが、これがAttributeValue型にならないと言われる。例によってStackOverflowに解決策が出ていた：<a href="http://stackoverflow.com/questions/3313056/how-does-one-get-strings-not-string-literals-into-blazehtml-attributes-element">how does one get strings (not string literals) into blazehtml attributes/element contents?</a><br /><br />AttributeValue型はIsStringのインスタンスだが、OverloadedStringsを宣言したファイルの文字列リテラルはOKでも、プログラムで作るString型は受け付けない。それで代わりにtoValue :: a -&gt; AttributeValueを用いればよい(一番最後のMagnus Kronqvistさんのコメント)。<br /><br />解決するのに1時間くらいはかかってしまった。
