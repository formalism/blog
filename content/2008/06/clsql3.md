Title: CLSQL実験(3)
Date: 2008-06-05 07:11:00
Category: 
Tags: Programming
Slug: clsql3

CLSQLを使ったWebアプリの実験の続き。<br /><br />前回で、なんとなくCLSQLのリーダマクロが動作していないのでは??ということで終わってしまったが、結論からすると、リーダマクロは動作していた。<br />(setf hunchentoot:*catch-errors-p* nil)<br />をtop.lispに追加して実験してみたら、<br /><br />debugger invoked on a FLEXI-STREAMS:FLEXI-STREAM-ENCODING-ERROR in thread #<thread>:<br />#\KATAKANA_LETTER_SI is not a LATIN-1 character.<br /><br />というようなエラーがブラウザからのアクセス時に表示されたので、FLEXI-STREAM-ENCODING-ERRORあたりでググってみたら、<br /><br />(setf hunchentoot:*hunchentoot-default-external-format* :UTF-8)<br /><br />すると良い、という情報を発見。これをtop.lispに追加してみたら、見事に動作した。<br /><br />まだCommon Coldの継続機能は動作していないものの、とりあえず一安心。<br /><br /></thread>
