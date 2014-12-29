Title: GitHub Pagesに移行しました
Date: 2014-12-30 05:50:00
Category: 
Tags: Blogging
Slug: moved-to-github-pages

これまでBloggerを使用していたけれど、ずっとWebベースのUIがいまいち
好きになれなかった。また、カスタマイズも結構面倒だった。

色々調査した結果、[GitHub Pages](https://pages.github.com/ "GitHub Pages")が
便利そうだ、ということが分かったので、なんとか色々駆使することで
Bloggerのデータを移行できたと思う。

最初は静的サイトの生成に[hakyll](http://jaspervdj.be/hakyll/ "hakyll")を使おうと
したけれど、なかなかカスタマイズが面倒になってしまった。実はこれだけでも
暇なときに2,3週格闘していた。

結局[Pelican](http://blog.getpelican.com/ "Pelican")を使用することで、最低限の
状態にはなったと思う。また、GitHub Pagesの場合、gh-pagesというブランチに
コミットしなければいけない、というルールがあるので、そのために
[ghp-import](https://github.com/davisp/ghp-import)を使用した。
これで少しはまったのは、ghp-import outputとすると、とくに何もコンソールには
表示されずにコミットまでされてしまうので、それに気付かずに何回も
コミットしてしまったこと。基本的にはghp-import -m 'message' -p outputのように
使用するのが良さそうだ。

これでMarkdownも使えるようになった。コードのハイライトなども楽に書けて嬉しい。
