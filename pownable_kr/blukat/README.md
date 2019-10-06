# 内容
まずはログインしてみる。

```bash
ssh blukat@pwnable.kr -p2222
blukat@pwnable.kr's password:
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
Last login: Thu Oct  3 11:58:51 2019 from 80.246.136.146
blukat@prowl:~$ ls
blukat  blukat.c  password
blukat@prowl:~$ ls -la
total 36
drwxr-x---   4 root blukat     4096 Aug 16  2018 .
drwxr-xr-x 114 root root       4096 May 19 15:59 ..
-r-xr-sr-x   1 root blukat_pwn 9144 Aug  8  2018 blukat
-rw-r--r--   1 root root        645 Aug  8  2018 blukat.c
dr-xr-xr-x   2 root root       4096 Aug 16  2018 .irssi
-rw-r-----   1 root blukat_pwn   33 Jan  6  2017 password
drwxr-xr-x   2 root root       4096 Aug 16  2018 .pwntools-cache
blukat@prowl:~$ cat password
cat: password: Permission denied
blukat@prowl:~$ ./blukat
guess the password!
fads
wrong guess!
blukat@prowl:~$ cat blukat.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
char flag[100];
char password[100];
char* key = "3\rG[S/%\x1c\x1d#0?\rIS\x0f\x1c\x1d\x18;,4\x1b\x00\x1bp;5\x0b\x1b\x08\x45+";
void calc_flag(char* s){
        int i;
        for(i=0; i<strlen(s); i++){
                flag[i] = s[i] ^ key[i];
        }
        printf("%s\n", flag);
}
int main(){
        FILE* fp = fopen("/home/blukat/password", "r");
        fgets(password, 100, fp);
        char buf[100];
        printf("guess the password!\n");
        fgets(buf, 128, stdin);
        if(!strcmp(password, buf)){
                printf("congrats! here is your flag: ");
                calc_flag(password);
        }
        else{
                printf("wrong guess!\n");
                exit(0);
        }
        return 0;
}
```

passwordファイルにある文字列と標準入力が同じならフラグが落ちてくる見たい。
このプログラムを見た限りだと、overflowもできなさそうだし、どうやって、フラグをゲットするのかよく分からない。

# 解答
試行錯誤した結果、今回ログインしたユーザーのグループがpasswordやblukatと同じであることが分かった。

```bash
blukat@prowl:~$ id
uid=1104(blukat) gid=1104(blukat) groups=1104(blukat),1105(blukat_pwn)
blukat@prowl:~$  ls -la
total 36
drwxr-x---   4 root blukat     4096 Aug 16  2018 .
drwxr-xr-x 114 root root       4096 May 19 15:59 ..
-r-xr-sr-x   1 root blukat_pwn 9144 Aug  8  2018 blukat
-rw-r--r--   1 root root        645 Aug  8  2018 blukat.c
dr-xr-xr-x   2 root root       4096 Aug 16  2018 .irssi
-rw-r-----   1 root blukat_pwn   33 Jan  6  2017 password
drwxr-xr-x   2 root root       4096 Aug 16  2018 .pwntools-cache
```

つまり、ユーザーでpasswordファイルを開けるということになる？

```bash
blukat@prowl:~$ cat password
cat: password: Permission denied
blukat@prowl:~$ vim password →　vimで開けたwwww
```

なんかvimでも開けてしまった・・・。
これでフラグを得ることができる。

```bash
blukat@prowl:~$  cat ./password | ./blukat
guess the password!
congrats! here is your flag:
```

否定的な文字が出ても、信じてはいけない！！
