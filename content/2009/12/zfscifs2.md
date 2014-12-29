Title: ZFSでのCIFS共有(2)
Date: 2009-12-25 05:04:00
Category: 
Tags: OpenSolaris
Slug: zfscifs2

以前[ZFSでのCIFS共有]({filename}../09/zfscifs.md)にて、zfsのプロパティで共有する方法を紹介しましたが、
どうやらOpenSolaris 2009.6ではまだCIFSが不安定です。自分の環境はOpenSolarisはVMWareで動かしているの
ですが、サスペンドから復帰すると再接続できなくなることが何度かありました。

それで、結局現在はSambaを入れて共有しています。

最近は、<a href="http://zfs-fuse.net/">ZFS for Linux</a>もあるようですので、無料でセキュリティパッチが
提供されていない(?)OpenSolarisの優位性が自分にとっては少なくなってきてしまいました。ちなみに、
ZFS for Linuxは、Ubuntu 8.04で簡単にコンパイルできました。まだdaemonを動かしただけでディスクを
使った実験はしていないので、性能などについては何ともいえませんが。
