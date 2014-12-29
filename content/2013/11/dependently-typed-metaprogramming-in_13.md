Title: Dependently Typed Metaprogramming (in Agda) メモ (2) 有限集合Finについて
Date: 2013-11-13 14:25:00
Category: 
Tags: Agda
Slug: dependently-typed-metaprogramming-in_13

[Dependently Typed Metaprogramming (in Agda) メモ]({filename}./dependently-typed-metaprogramming-in.md)の続き。

Exercise 1.5では、有限集合を表す型Finを定義している。<br /><br />data Fin : N -&gt; Set where<br />&nbsp;&nbsp; fzero : {n : N} -&gt; Fin (suc n)<br />&nbsp;&nbsp; fsuc : {n : N} -&gt; Fin n -&gt; Fin (suc n)<br /><br />ここで、fzero, fsucとしたのは、自然数の型で使用しているzero, sucと区別しやすいようにするため。<br /><br />有限集合Finは、依存型言語で良く取り上げられる例題のようだが、理解するのは簡単ではないように思う。次のように考えると良いと分かった：<br /><br /><div style="text-align: left;">まず、Fin 0という型の要素があるか？と考えると、fzero, fsucどちらの構成子も、構成される型はFin (suc n)の形であるから、実際はFin 0の要素は存在しない。</div><div style="text-align: left;"><br /></div><div style="text-align: left;">次に、fzeroについて考える。定義からfzero : Fin 1, fzero : Fin 2, ... となる、つまりfzeroはFin n (n&gt;0)の要素となっている。次に、fzero : Fin 1よりfsuc fzero : Fin 2である。同様に、fzero : Fin 2だから、fsuc fzero : Fin 3である。これを続けると、fsuc fzeroは、Fin n (n&gt;1)の要素となっている。</div><div style="text-align: left;"><br /></div><div style="text-align: left;">これらを型ごとにまとめると、Fin 0は空であり、Fin 1はfzeroのみを含み、Fin 2はfzero, fsuc fzeroを含み、Fin 3はfzero, fsuc fzero, fsuc (fsuc fzero)を含み....となる。</div><div style="text-align: left;"><br /></div><div style="text-align: left;">つまり、Fin nは、nより小さい(0から始める)自然数全体からなる集合と同じであると見なせる。 </div>
