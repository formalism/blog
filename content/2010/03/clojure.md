Title: Clojureが素敵な件
Date: 2010-03-26 07:00:00
Category: 
Tags: Programming
Slug: clojure

最近、ちょっとしたWeb+DBアプリケーションを書きたいと思った。数年前は、Java+Struts+MySQLのような組み合わせがはやっていたと思う。その後もJavaのフレームワークはSpringやらSeasarやらたくさん提案されてきたし、自分もSeasarは一時期使って便利だと思った。でもやっぱり記述量が多く、面倒くさい。<br /><br />近頃はLLブームということもあって、Ruby on Railsに始まるLL言語系フレームワークがある。RoRは自分で使ってみて、家計簿のWebアプリを作成し、今でも現役で使っている。ただ、個人的にはバージョンアップなどが手間で、あまり好きではない。<br /><br />自分の中での最近はやりの言語はCommon Lispである。その実装としてSBCLなどがあり、SBCL+MySQLでも簡単なWebアプリを作ってみた。が、Lisp系言語はライブラリをいちいちインストールするのが面倒に思う。特にWindowsは弱い。Linux, Windows, Solarisなどの環境で、ひとつのものから別のものへすぐに移行するのは難しい。あるいは、最近であればGoogle App Engineを使って、環境の管理は全部Google様におまかせ、というのが流行なのであろうか。でもGAEは基本的にはRDBは使えないし、Lispも使えない。 <br /><br />以上のような遍歴を経て、現状において最善の折衷案として自分的に浮上しているのは、<a href="http://clojure.org/">clojure</a>である。Lispとまではいかないが、Lisp風味であり、<a href="http://github.com/weavejester/compojure">compojure</a>というWebフレームワークもある。これに<a href="http://www.h2database.com/html/main.html">H2</a>を組み合わせれば、Pure Javaで、どの環境にもコピーでOKという素敵なWebアプリケーションが簡単に作れる。Javaは昔はいまいちだったが、JVMの功績は大きい。これはかなり最強の組み合わせではなかろうか。
