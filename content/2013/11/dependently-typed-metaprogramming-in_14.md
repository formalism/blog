Title: Dependently Typed Metaprogramming (in Agda) メモ (3) tabulate
Date: 2013-11-14 11:45:00
Category: 
Tags: Agda
Slug: dependently-typed-metaprogramming-in_14

まだExercise 1.5の続き。<br /><br />tabulate : forall {n X} -&gt; (Fin n -&gt; X) -&gt; Vec X n<br />tabulate {n} f = ?<br /><br />を完成させる。{n}0としてC-cC-cをして、後はひたすらC-cC-aをすると、型としては正しい式が完成する。<br /><br />tabulate {zero} f = &lt;&gt;<br />tabulate {suc y} f = f fzero , tabulate (\ _ -&gt; f fzero)<br /><br />というもの。fにずっとfzeroを与えたものをn個集めたVecを答えとしている。でも多分これは問題の答えとしては期待通りのものではない。イメージとしては、fにfzero, fsuc fzero, fsuc (fsuc fzero), ... を引数に与えたものをn個集めたものを得たい。つまり、f 0, f 1, f 2,..., f (n-1)を集めるというイメージ。Fin nに含まれるすべての要素をfに渡した結果をVecに集める。<br /><br />実は答えはData.Vecに既にあった。<br /><br />tabulate {zero} f = &lt;&gt;<br />tabulate {suc y} f = f fzero , tabulate {y} (\ n -&gt; f (fsuc n))<br /><br />も型を満たす。実際にtabulate {3} fなどを展開してみると、上記の期待通りとなっていることが確認できる。再帰を繰り返す毎に、fzeroに適用されるfsucが一つずつ増えていく。F (n-1), F (n-2), ..., F 0を作ろうとすると難しいが、逆に0からはじめて1ずつ加えていくのを再帰と共に行うところがミソか。
