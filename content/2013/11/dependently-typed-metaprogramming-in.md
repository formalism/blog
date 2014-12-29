Title: Dependently Typed Metaprogramming (in Agda) メモ
Date: 2013-11-13 09:42:00
Category: 
Tags: Agda
Slug: dependently-typed-metaprogramming-in

<a href="http://www.cl.cam.ac.uk/~ok259/agda-course-13/">Dependently Typed Metaprogramming (in Agda)</a>のメモ <br /><br /><b>Agdaの編集方法：</b> <br />Emacsのagda-modeを使えば、TeXの感覚で記号を入力できる。例：<br />太字のN : \bn <br />下付の数字 : \_0, \_1など<br />× : \times<br />→ : \rightarrow<br /><br />それと型構成子×は、open import Data.Productを書かないと使えなかった。また、最初はData.Productが開けなかったので、(custom-set-variables '(agda2-include-dirs (quote ("." "agda-lib-folder/src"))))を.emacs.elに追加する必要があった。<br /><br />------------------------------------<br />C-cC-lで現在開いているagdaファイルをロードしてチェックしてくれる。<br /><br />zip : forall {n S T} -&gt; Vec S n -&gt; Vec T n -&gt; Vec (S × T) n<br />zip ss ts = ?<br /><br />上のように、関数の型定義のみを記述し、関数の本体定義の右側に?を入れてからロードすると、対話的に証明が出来る。<br /><br />zip ss ts = { }0<br /><br />となり、 ?0 : Vec (.S × .T) .nと情報が表示される。これは{}0の場所に、型Vec (.S × .T) .nを持つ式を記述すればよい、ということを示している。<br /><br />{}0の中にssを入力し、C-cC-cをすると、ssについて場合分けができる。{}の中が自明であれば、この中でC-cC-aをすると、型に合う式を見つけて、自動的に式を作ってくれる。<br /><br />既に定義した名前を{}に入れてからC-cC-aすると、それらの名前もヒントとして使用してくれる(Exercise 1.3. vapp vecと書いてからC-cC-aで埋めてくれる。Exercise 1.4もvapp vecを書くだけでvapp (vapp (vec _,_) ss) tsと埋めてくれる)<br /><br />とりあえず、今回はここまで。
