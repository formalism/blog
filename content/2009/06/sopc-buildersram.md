Title: SOPC BuilderにてSRAMを使う
Date: 2009-06-11 05:49:00
Category: 
Tags: FPGA
Slug: sopc-buildersram

めも。<br /><br />QuartusIIのSOPC BuilderでSRAMを使いたい。QuartusIIにはCypressのコンポーネントが付いているが、ビット幅などが使用したいものと違うので、コンポーネントを作成する必要があった。<br /><br />Component Editorを起動してAvalon-MM Tristate Slaveをテンプレートから作成すると、とりあえずコンポーネントはできるものの、NIOSIIのメモリとして使用できない。調べた結果、<span style="font-weight: bold;">(コンポーネント名)_hw.tcl</span>にある、<span style="font-weight: bold;">isMemoryDevice</span>というのを、"false"から"true"にすればOKであると分かった。
