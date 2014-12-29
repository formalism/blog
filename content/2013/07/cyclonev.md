Title: CycloneVがやばい??
Date: 2013-07-11 13:38:00
Category: 
Tags: FPGA
Slug: cyclonev

<p>twitter経由で、CycloneVに重大な欠陥がある、というようなものを見つけた。<a href="http://www.altera.co.jp/literature/es/es_cyclone_v.pdf">Errata Sheet for CycloneV Devices</a>によると、重大な問題というのは、2番目のFractional PLL Phase Alignment Errorのようだ。PLLの位相が設定値よりもずれてしまう場合がある、というようなことらしい。影響を受ける事例としてLVDSが挙げられている。例えば、受信クロックをPLLでロックさせてnビットデシリアライズする、といったときに影響するのかも知れない。確かに、ここに問題があるとすれば、用途によっては使い物にならなくなってしまうかも知れない。</p> <p>PLLの詳しい仕組みには詳しくないが、PLLだけでも<a href="http://www.amazon.co.jp/gp/product/4789830233/ref=as_li_qf_sp_asin_tl?ie=UTF8&camp=247&creative=1211&creativeASIN=4789830233&linkCode=as2&tag=formalism-22">本</a>が何冊も書けるくらいだから、アナログ回路の真骨頂なのだろう。それだけに問題も起きやすいところかも知れない。</p> <p>いずれにせよ、しばらくはXilinx優位ということになりそうだ。</p>
