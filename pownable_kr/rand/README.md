# 内容
rand関数の脆弱性をつく問題。今回はidaを使ってもわからないため、gdbで動的解析を行う。
* rand関数は定数では無いため、静的解析であるidaでは見つけることが出来ない。

実際に問題を見ていく。


```bash
ssh random@pwnable.kr -p2222
random@pwnable.kr's password:
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
Last login: Wed Jul 17 02:59:23 2019 from 118.238.217.72
random@prowl:~$ ls
flag  random  random.c
random@prowl:~$ cat flag
cat: flag: Permission denied
random@prowl:~$ ./random
44444
Wrong, maybe you should try 2^32 cases.
random@prowl:~$ ./random
tefas
Wrong, maybe you should try 2^32 cases.
random@prowl:~$ cat random.c
#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();        // random value!

        unsigned int key=0;
        scanf("%d", &key);

        if( (key ^ random) == 0xdeadbeef ){
                printf("Good!\n");
                system("/bin/cat flag");
                return 0;
        }

        printf("Wrong, maybe you should try 2^32 cases.\n");
        return 0;
}

random@prowl:~$
```

このプログラムでは、疑似乱数のシード値が設定されていないため、rand関数の値は常に同じになってしまう。
* シード値　：　疑似乱数算出時、初期値のこと。

そのため、gdbでrandから出力される値を監視する。
この値さえわかれば、key値を求めることが出来る。
理由は A^B = C →　B^C = Aだから

* 因みに、c言語において、シード値を設定するにはsrandを用いる。
以下に、randのmanの一部分を示す。


```
DESCRIPTION
       The  rand()  function returns a pseudo-random integer in the range 0 to RAND_MAX inclusive (i.e., the mathe‐
       matical range [0, RAND_MAX]).

       The srand() function sets its argument as the seed for a  new  sequence  of  pseudo-random  integers  to  be
       returned by rand().  These sequences are repeatable by calling srand() with the same seed value.

       If no seed value is provided, the rand() function is automatically seeded with a value of 1.
```

# gdbによるrand値の確認
* gdbの使い方
	* disassemble ：　ディスアセンブル
	* break	：　ブレイクポイント　アドレス値には必ずアスタリスクをつける。
	* run　：　実行
	* print　：　画面出力。　レジスタは**$eax**などのようにドルマークを前につける

以下、randomの実行結果。
関数の戻り値はeaxに入るため、アドレス値0x400606番のeaxを確認すれば良い。
* x86では戻り値はeaxレジスタに入ります。
* 理由は知らないがアセンブラのシンタックスがAT&Tになっている。
* 直すときは以下のコマンドを打つ
> set disassembly-flavor intel
* AT&Tのままなら
> set disassembly-flavor att
* スタイルを確認したいなら
> show disassembly-flavor

```bash
random@prowl:~$ gdb random
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from random...(no debugging symbols found)...done.
(gdb) disassemble main
Dump of assembler code for function main:
   0x00000000004005f4 <+0>:     push   %rbp
   0x00000000004005f5 <+1>:     mov    %rsp,%rbp
   0x00000000004005f8 <+4>:     sub    $0x10,%rsp
   0x00000000004005fc <+8>:     mov    $0x0,%eax
   0x0000000000400601 <+13>:    callq  0x400500 <rand@plt>
   0x0000000000400606 <+18>:    mov    %eax,-0x4(%rbp)
   0x0000000000400609 <+21>:    movl   $0x0,-0x8(%rbp)
   0x0000000000400610 <+28>:    mov    $0x400760,%eax
   0x0000000000400615 <+33>:    lea    -0x8(%rbp),%rdx
   0x0000000000400619 <+37>:    mov    %rdx,%rsi
   0x000000000040061c <+40>:    mov    %rax,%rdi
   0x000000000040061f <+43>:    mov    $0x0,%eax
   0x0000000000400624 <+48>:    callq  0x4004f0 <__isoc99_scanf@plt>
   0x0000000000400629 <+53>:    mov    -0x8(%rbp),%eax
   0x000000000040062c <+56>:    xor    -0x4(%rbp),%eax
   0x000000000040062f <+59>:    cmp    $0xdeadbeef,%eax
   0x0000000000400634 <+64>:    jne    0x400656 <main+98>
   0x0000000000400636 <+66>:    mov    $0x400763,%edi
   0x000000000040063b <+71>:    callq  0x4004c0 <puts@plt>
   0x0000000000400640 <+76>:    mov    $0x400769,%edi
   0x0000000000400645 <+81>:    mov    $0x0,%eax
   0x000000000040064a <+86>:    callq  0x4004d0 <system@plt>
   0x000000000040064f <+91>:    mov    $0x0,%eax
   0x0000000000400654 <+96>:    jmp    0x400665 <main+113>
   0x0000000000400656 <+98>:    mov    $0x400778,%edi
   0x000000000040065b <+103>:   callq  0x4004c0 <puts@plt>
   0x0000000000400660 <+108>:   mov    $0x0,%eax
   0x0000000000400665 <+113>:   leaveq
   0x0000000000400666 <+114>:   retq
End of assembler dump.
(gdb) break *0x400606
Breakpoint 1 at 0x400606
(gdb) run
Starting program: /home/random/random

Breakpoint 1, 0x0000000000400606 in main ()
(gdb) print $eax
$1 = 1804289383
(gdb) print $eax^0xdeadbeef
$2 = 3039230856
(

```
よって3039230856がkeyの値であるkとが分かった。

# 結果
先ほど判明したkey値を入力してみる

```bash
random@prowl:~$ ./random
3039230856
Good!
Mommy, I thought libc random is unpredictable...
random@prowl:~$
```

フラグゲット。
