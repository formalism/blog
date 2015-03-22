Title: Haskellにて変更可能配列(mutable vector)の実験
Date: 2015-03-22 23:10:00
Category:
Tags: Haskell
Slug: mutable_vector_in_haskell

自分用のメモ。Haskellにてmutable vectorを使う方法。STモナドの中であれば変更できる。STモナドは
PrimMonad ST, PrimState STとなっている。[実装はここ](https://gist.github.com/formalism/f6efc93df8e90cfd39b0 "DctQuant.hs"). DctQuantという名前なのにDCTしか実装していない。ijgjpegのfloatバージョンを元にして変更。あまり確認していないので、計算に間違いがあるかも。
