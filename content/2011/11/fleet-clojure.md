Title: fleet (clojureによるテンプレートシステム)
Date: 2011-11-19 16:06:00
Category: 
Tags: Programming,clojure
Slug: fleet-clojure

また久しぶりにclojureをいじり始めた。またWebシステムの実装に用いる予定。どうやってJSPやASPのように動的にWebページを生成するのが良いのか、最近の流行を少し調べてみた。<br /><br />結果として、自分には<a href="https://github.com/Flamefork/fleet">fleet</a>が現状良さそうという結論に達した。若干悩んだ点と調べて分かったことのメモ。<br /><br /><ul><li>fleet-nsでテンプレートを生成するときに、引数で指定したディレクトリにあるファイルを 走査して、それぞれの<b>テンプレートファイルに対応するテンプレート関数</b>が作られる。例えば、post.html.fleetというファイルが存在すれば、postという関数が、(同じく引数で指定した名前空間に)作られる。</li><li>post関数の内部(つまり、テンプレートファイルの中)では、dataという名前でテンプレート関数への<b>実引数</b>を参照できる。すなわち、&lt;(:hoge data)&gt;とpost.html.fleetに記述すれば、このテンプレート関数が実行されるときに、実引数として渡されたmapにあるhogeキーの値を出力する。</li></ul>
