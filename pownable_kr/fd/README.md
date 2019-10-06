sshで下記のURLに入ると以下のflagファイルがあるのだが、permission errorで開かないのでELFファイルのfdを用いて何とかしろと言う問題

```bash
$ ssh fd@pwnable.kr -p2222
The authenticity of host '[pwnable.kr]:2222 ([128.61.240.205]:2222)' can't be established.
ECDSA key fingerprint is SHA256:I9nWMZvctQv4Vypnh9ICs6aB2g20WV/EjTIYJ83P0K8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[pwnable.kr]:2222,[128.61.240.205]:2222' (ECDSA) to the list of known hosts.
fd@pwnable.kr's password:
 ____  __    __  ____    ____  ____   _        ___      __  _  ____
|    \|  |__|  ||    \  /    ||    \ | |      /  _]    |  |/ ]|    \
|  o  )  |  |  ||  _  ||  o  ||  o  )| |     /  [_     |  ' / |  D  )
|   _/|  |  |  ||  |  ||     ||     || |___ |    _]    |    \ |    /
|  |  |  `  '  ||  |  ||  _  ||  O  ||     ||   [_  __ |     \|    \
|  |   \      / |  |  ||  |  ||     ||     ||     ||  ||  .  ||  .  \
|__|    \_/\_/  |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|

- Site admin : daehee87.kr@gmail.com
- IRC : irc.netgarage.org:6667 / #pwnable.kr
- Simply type "irssi" command to join IRC now
- files under /tmp can be erased anytime. make your directory under /tmp
- to use peda, issue `source /usr/share/peda/peda.py` in gdb terminal
Last login: Mon Jul  8 04:09:44 2019 from 175.195.197.177
fd@prowl:~$ ls -la
drwxr-x---   5 root   fd   4096 Oct 26  2016 .
drwxr-xr-x 114 root   root 4096 May 19 15:59 ..
d---------   2 root   root 4096 Jun 12  2014 .bash_history
-r-sr-x---   1 fd_pwn fd   7322 Jun 11  2014 fd
-rw-r--r--   1 root   root  418 Jun 11  2014 fd.c
-r--r-----   1 fd_pwn root   50 Jun 11  2014 flag
-rw-------   1 root   root  128 Oct 26  2016 .gdb_history
dr-xr-xr-x   2 root   root 4096 Dec 19  2016 .irssi
drwxr-xr-x   2 root   root 4096 Oct 23  2016 .pwntools-cache
```

fdにSGIDがついている所から、flagファイルと同じfd_pwnの権限で実行できる模様。fdのソースコードであるfd.cを見てみる

```bash
fd@prowl:~$ cat fd.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}

```

引数をファイルディスクリプタ(fd)に代入してread()で何か読み込んでいる模様。
そのあと、strcmpで判定をしてsystemでflagを開く。
このプログラムはfd_pwn権限で動くのでsystemコールを読んだらflagが開くという流れみたい。

いずれにしてもこっちからいじれそうな変数はfdのみみたい。
ということで、ファイルディスクリプタについて調べる。

以下、STDINのmanを調べた結果である。


> On program startup, the integer file descriptors associated with the streams stdin, stdout, and stderr are  0,1,  and  2, respectively.  The preprocessor symbols STDIN_FILENO, STDOUT_FILENO, and STDERR_FILENO are definedwith these values in <unistd.h>.  (Applying freopen(3) to one of these streams can change the file  descriptornumber associated with the stream.)


要約すると以下のようになる
* fdによるモードの変化
  * stdin = 0
  * stdout = 1
  * stderr = 2

つまり、fdの値を0にしてしまえば、入力になるので"LETMEWIN"を入力してflagをゲットできる。
"int fd = atoi( argv[1] ) - 0x1234;"なので0x1234の１０進数である4660を入力すれば良い。



```bash
fd@prowl:~$ ./fd 4660
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```

get出来た。
