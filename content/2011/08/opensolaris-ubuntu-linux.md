Title: OpenSolaris -> Ubuntu Linux
Date: 2011-08-27 14:53:00
Category: 
Tags: Linux,OpenSolaris
Slug: opensolaris-ubuntu-linux

これまでメインのデータストレージはVM上のOpenSolaris 2009.6のZFSファイルシステムであったが、Solarisの今後を考えると少し不安なので(FreeBSD+ZFSという手もあるが)、Ubuntu Linux 10.04LTS上のLVM2+ext4に移行した。ZFSの先進性からすると、ファイルストレージとしては後退した感はあるが、いろいろなオープンソースソフトウェアは、なんだかんだいってLinuxが主なターゲットになっているのが現実であるので、メリットもある。<br /><br />btrfsは安定性を考慮して、今のところ見送り。FreeBSD+ZFSもメモリを食うという情報が多かったので見送り。<br /><br />なかなか現状オープンソースで満足のゆく解はなさそうだ。
