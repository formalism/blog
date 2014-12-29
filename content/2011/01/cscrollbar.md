Title: C#のScrollBar
Date: 2011-01-17 07:01:00
Category: 
Tags: C#, Programming
Slug: cscrollbar

ScrollBarの値をユーザが操作して変更すると、Scrollイベントが発生するが、プログラムコードでValueプロパティを変更するとScrollイベントは発生しない。ValueChangedイベントを使用すれば、Valueプロパティをコードで変更しても捕捉できる。分かってしまえばどうということは無いけれど、ちょっと調べる必要があった。<br /><br /># Delphiは確かコードで変更してもC#でいうところのValueChangedイベントのような動作がデフォルトだったように思った。
