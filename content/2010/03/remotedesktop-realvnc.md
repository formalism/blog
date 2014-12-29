Title: リモートデスクトップ
Date: 2010-03-04 06:41:00
Category: 
Tags: Software
Slug: remotedesktop-realvnc

Windowsを遠隔から操作しようとしたが、やり方が悪いのかもしれないが、リモートデスクトップでは、どうしても"コンソールセッション"に接続できなかった。接続先がXPだから??<br /><br />結局、リモートデスクトップはあきらめて、<a href="http://www.realvnc.com/">RealVNC</a>を使うことにした。これだとちゃんとコンソールセッションに接続できた。そして、Windowsの起動時に<a href="http://www.nanshiki.co.jp/software/index.html?sexe">sexe</a>を使用して、VMWare Playerをサービスとして起動し、LinuxサーバにSSHログインできるようにした。SSHのポートフォワードを使用して、VNCに遠隔から接続できるようになった。<br /><br />でも速度的にはリモートデスクトップの方が軽快...
