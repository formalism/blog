Title: ZynqのPLを操作するLinuxドライバ (ユーザプログラム編)
Date: 2014-05-14 08:52:00
Category: 
Tags: Zynq,Linux
Slug: zynqpllinux

[ZynqのPLを操作するLinuxドライバ (DTS設定編)]({filename}./zynqpllinux-dts.md)の続き。これは見た方が早いと思うので、コードを示す。

-----------------------------------------------

    :::c
    #include <stdlib.h>
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <sys/mman.h>
    #include <fcntl.h>
    #include <errno.h>
    
    int main()
    {
        int uiofd;
        int err;
        int i;
        unsigned icount;
        unsigned int* map_addr;
        unsigned int cnt;
        unsigned int one = 1;
    
        uiofd = open("/dev/uio0", O_RDWR);
        if (uiofd < 0) {
            perror("uio open:");
            return errno;
        }
    
        map_addr = (unsigned int*)mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, uiofd, 0);
        if (!map_addr){
            fprintf(stderr, "mmap failed\n");
            return errno;
        }
    
        write(uiofd, &one, 4);    // enable interrupt to uio_pdrv_genirq
        map_addr[0] = 0x0BEBC200;    // 200M
        map_addr[1] = 0; // disable
        map_addr[2] = 1;    // clear interrupt
        map_addr[1] = 1; // enable
    
        for(i = 0;; ++i) {
            /* Print out a message, for debugging. */
            if (i == 0)
                fprintf(stderr, "Started uio test driver.\n");
            else
                fprintf(stderr, "Interrupts: %d,%x\n", icount, cnt);
    
            /* Wait for next interrupt. */
            err = read(uiofd, &icount, 4);
            if (err != 4) {
                perror("uio read:");
                break;
            }
            cnt = map_addr[3];
            map_addr[2] = 1;    // clear interrupt
            write(uiofd, &one, 4);    // enable interrupt again
        }
        munmap(map_addr, 4096);
        close(uiofd);
        return errno;
    }

-----------------------------------------

要点は次の通り：

1. /dev/uio0をオープンする
2. デバイスレジスタにアクセスするためにuiofdに対してmmapする
3. uiofdに対するreadで割り込み待ちが可能。読み込むバイト数は4にしなければならない
4. readが戻ったときには、ドライバが割り込み禁止にしているので、write(uiofd, &one, 4)をすることで、再度割り込みを有効にする。
5. mmapで得られた領域の先頭要素が、デバイスレジスタ領域の先頭に対応しているので、普通のメモリのように読み書きすると、デバイスレジスタを読み出し/書き込みできる。

以上を例によってZYBOにて実験してみたところ、デバイスの割り込みがHighになってから、おおよそ75マイクロ秒程度でreadが完了した(CPU負荷はデバッガを除いてほとんど無い状態。アプリケーションはデバッグビルド)。それほど厳しい制御が必要でない場合は、この程度の応答性でも十分実用になりそうだ。
