Title: androidのHttpURLConnection::getInputStreamでjava.io.FileNotFoundException
Date: 2013-05-15 14:39:00
Category: 
Tags: Programming,Android
Slug: androidhttpurlconnectiongetinputstreamj

<p>androidで、HttpURLConnectionクラスを使って、リモートサーバにGETリクエストを送り、結果を取得しようとした。だが、なぜかgetInputStreamを呼び出したところでjava.io.FileNotFoundExceptionが発生する。そのURLをブラウザでアクセスすることはできるのに。</p> <p>検索してみたところ、いつもの<a href="http://stackoverflow.com/questions/5178947/filenotfoundexception-when-calling-webservice">StackOverflow</a>に答えがあった。HTTPのレスポンスコードが400以上であると、HttpURLConnectionはFileNotFoundExceptionを投げる、ということが原因だった。ブラウザでアクセスできていると思っていたが、レスポンスコードを見てみると、403 Forbiddenだった。</p> <p>というわけで、同じ回答では、<a href="http://developer.android.com/reference/java/net/HttpURLConnection.html#getResponseCode%28%29">getResponseCode()</a>を使って問題を特定する、ということが勧められていた。</p>
