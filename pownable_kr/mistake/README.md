# 内容
まず、sshで接続して問題を見てみる。

```bash
$ ssh mistake@pwnable.kr -p2222
mistake@pwnable.kr's password:
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
Last login: Mon Jul 22 21:19:26 2019 from 118.238.217.72
mistake@prowl:~$ ls
flag  mistake  mistake.c  password
mistake@prowl:~$ ls -la
total 44
drwxr-x---   5 root        mistake 4096 Oct 23  2016 .
drwxr-xr-x 114 root        root    4096 May 19 15:59 ..
d---------   2 root        root    4096 Jul 29  2014 .bash_history
-r--------   1 mistake_pwn root      51 Jul 29  2014 flag
dr-xr-xr-x   2 root        root    4096 Aug 20  2014 .irssi
-r-sr-x---   1 mistake_pwn mistake 8934 Aug  1  2014 mistake
-rw-r--r--   1 root        root     792 Aug  1  2014 mistake.c
-r--------   1 mistake_pwn root      10 Jul 29  2014 password
drwxr-xr-x   2 root        root    4096 Oct 23  2016 .pwntools-cache
mistake@prowl:~$ ./mistake
do not bruteforce...
ddddddddddddd
^C
mistake@prowl:~$ cat ./mistake.c
#include <stdio.h>
#include <fcntl.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char* s, int len){
        int i;
        for(i=0; i<len; i++){
                s[i] ^= XORKEY;
        }
}

int main(int argc, char* argv[]){

        int fd;
        if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
                printf("can't open password %d\n", fd);
                return 0;
        }

        printf("do not bruteforce...\n");
        sleep(time(0)%20);

        char pw_buf[PW_LEN+1];
        int len;
        if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
                printf("read error\n");
                close(fd);
                return 0;
        }

        char pw_buf2[PW_LEN+1];
        printf("input password : ");
        scanf("%10s", pw_buf2);

        // xor your input
        xor(pw_buf2, 10);

        if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
                printf("Password OK\n");
                system("/bin/cat flag\n");
        }
        else{
                printf("Wrong Password\n");
        }

        close(fd);
        return 0;
}

mistake@prowl:~$ ./mistake
do not bruteforce...
123456789t
input password : 123456789t
Wrong Password
mistake@prowl:~$
```

入力した文字列が２つある。これを文字列a, bと置くと、以下のような状態でflagが開くことが分かる。
* a = 文字数10の入力1
* b = 文字列10の入力2を1でxorしたもの。つまり平文を反転したもの
* a == bならflagゲット

と、言うことで、まず、aの値を適当に考える。

# 解答
今回、aは以下の値に設定した。
> a = "abcdefghij"(10文字)

次にbについて検討する。
bはxorは２回すると元の値に戻る性質を利用すると、
aを1でxorしたものを考えれば良いことが分かる。
> a ^ b = c　→　c ^ b = a (二回xorすると、元に戻る)

> "abcdefghij" ^ 1  = c → c ^ 1 = "abcdefghij" 

今回はc言語でxorを求めてみた。

```c
#include<stdio.h>
#include<string.h>

int main(void){
  char s[11] = "abcdefghij";
  printf("%s\n", s);
  for(int i = 0; i < strlen(s); i++){
    printf("%x ", s[i]);
  }
  printf("\n");
  int reverse = 1;
  char s2[11];

  for(int i = 0; i < strlen(s); i++){
    s2[i] = s[i] ^ reverse;
    printf("%x ", s2[i]);
  }
  printf("\n");
  printf("%s\n", s2);
  return 0;
}
```

実行結果から、"abcdefghij"の反転は"`cbedgfihk"であることが分かった。

```bash
$ ./a.out
abcdefghij
61 62 63 64 65 66 67 68 69 6a
60 63 62 65 64 67 66 69 68 6b
`cbedgfihk
```

# 解答

```bash
mistake@prowl:~$ ./mistake
do not bruteforce...
abcdefghij
input password : `cbedgfihk
Password OK
Mommy, the operator priority always confuses me :(
```

フラグゲット
