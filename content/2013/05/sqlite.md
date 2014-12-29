Title: SQLiteの時刻取得精度について調査した
Date: 2013-05-01 09:32:00
Category: 
Tags: Programming
Slug: sqlite

<p>SQLiteでselect julianday('now')とすると、整数部と小数部からなる値が表示される。これはユリウス日と言われる値になるそうだが、この小数部の精度がどうなっているのか気になったので調査した。</p> <p><span style="font-size: large;"><u>結論からすると、x86アーキテクチャのLinuxで動作している場合、<b>ミリ秒単位</b>が限界となりそうだ。</u></span></p> <p>SQLiteのソースだと、unixCurrentTimeInt64という関数で現在時刻を取得するようだ。この関数のコメントには、</p><br />/*<br />** Find the current time (in Universal Coordinated Time). &nbsp;Write into *piNow<br />** the current time and date as a Julian Day number times 86_400_000. &nbsp;In<br />** other words, write into *piNow the number of milliseconds since the Julian<br />** epoch of noon in Greenwich on November 24, 4714 B.C according to the<br />** proleptic Gregorian calendar.<br />**<br />** On success, return SQLITE_OK. &nbsp;Return SQLITE_ERROR if the time and date<br />** cannot be found.<br />*/<br /><br /><p>とある。ユリウス日起源からのミリ秒を*piNowに書き込む、とある。実際、(プリプロセッサのelseパートがコンパイルされるとして)gettimeofday(&amp;sNow, 0)が実行され、</p><br />*piNow = unixEpoch + 1000*(sqlite3_int64)sNow.tv_sec + sNow.tv_usec/1000;<br /><br /><p>が実行されて、マイクロ秒の1/1000単位までが保存される、つまりミリ秒が精度となる。</p>
