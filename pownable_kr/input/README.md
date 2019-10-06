# 内容
プログラムを読み解いて、mainの最後まで通す問題

```bash
$ ssh input2@pwnable.kr -p2222
input2@pwnable.kr's password:
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
Last login: Wed Jul 17 21:11:31 2019 from 118.238.217.72
input2@prowl:~$ ls
flag  input  input.c
input2@prowl:~$ cat flag
cat: flag: Permission denied
input2@prowl:~$ ./input
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
input2@prowl:~$ ./input fdsaf
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
input2@prowl:~$ cat input.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char* argv[], char* envp[]){
        printf("Welcome to pwnable.kr\n");
        printf("Let's see if you know how to give input to program\n");
        printf("Just give me correct inputs then you will get the flag :)\n");

        // argv
        if(argc != 100) return 0;
        if(strcmp(argv['A'],"\x00")) return 0;
        if(strcmp(argv['B'],"\x20\x0a\x0d")) return 0;
        printf("Stage  clear!\n");

        // stdio
        char buf[4];
        read(0, buf, 4);
        if(memcmp(buf, "\x00\x0a\x00\xff", 4)) return 0;
        read(2, buf, 4  );
        if(memcmp(buf, "\x00\x0a\x02\xff", 4)) return 0;
        printf("Stage 2 clear!\n");

        // env
        if(strcmp("\xca\xfe\xba\xbe", getenv("\xde\xad\xbe\xef"))) return 0;
        printf("Stage 3 clear!\n");

        // file
        FILE* fp = fopen("\x0a", "r");
        if(!fp) return 0;
        if( fread(buf, 4, 1, fp)!=1 ) return 0;
        if( memcmp(buf, "\x00\x00\x00\x00", 4) ) return 0;
        fclose(fp);
        printf("Stage 4 clear!\n");

        // network
        int sd, cd;
        struct sockaddr_in saddr, caddr;
        sd = socket(AF_INET, SOCK_STREAM, 0);
        if(sd == -1){
                printf("socket error, tell admin\n");
                return 0;
        }
        saddr.sin_family = AF_INET;
        saddr.sin_addr.s_addr = INADDR_ANY;
        saddr.sin_port = htons( atoi(argv['C']) );
        if(bind(sd, (struct sockaddr*)&saddr, sizeof(saddr)) < 0){
                printf("bind error, use another port\n");
                return 1;
        }
        listen(sd, 1);
        int c = sizeof(struct sockaddr_in);
        cd = accept(sd, (struct sockaddr *)&caddr, (socklen_t*)&c);
        if(cd < 0){
                printf("accept error, tell admin\n");
                return 0;
        }
        if( recv(cd, buf, 4, 0) != 4 ) return 0;
        if(memcmp(buf, "\xde\xad\xbe\xef", 4)) return 0;
        printf("Stage 5 clear!\n");

        // here's your flag
        system("/bin/cat flag");
        return 0;
}

input2@prowl:~$
```

# ファイルの作成
正直、これが一番つまずいた・・・。
まず、この問題はstageが5まである時点で、pythonなどのワンライナーで書くのは厳しい。
だから、ファイルを作成しないといけないんだが、ファイルが作れず、悲しみに明け暮れた。
```bash
input2@prowl:~$ vim sol.py
書き込もうとすると　→　Can't open file for writing になる
```

* 解決方法　：　tmpディレクトリに新しいディレクトリを作成してそこでファイルを作る
* 注意　：　ディレクトリが既に存在する場所にファイルは作成できない。なぜなら、パーミッションが自分ではないから。

```bash
input2@prowl:~$ cd /tmp
input2@prowl:/tmp$ ls
ls: cannot open directory '.': Permission denied
input2@prowl:/tmp$ mkdir -pv ooo →　オプションを指定するとなぜかファイルが作成できない。
input2@prowl:/tmp$ cd ooo
input2@prowl:/tmp/ooo$ vim sol.py →　ファイルが作成できない
input2@prowl:/tmp/ooo$
input2@prowl:/tmp/ooo$
input2@prowl:/tmp/ooo$ ls →　ファイルが作成できないので、もちろんlsでも出ない
input2@prowl:/tmp/ooo$ ls -la
total 128
drwxrwxr-x    2 otp  otp    4096 Jun 20 21:57 .
drwxrwx-wt 1860 root root 122880 Jul 17 23:09 ..
input2@prowl:/tmp/ooo$ vim sol.py
input2@prowl:/tmp/ooo$ cd ../
input2@prowl:/tmp$ mkdir aaa →　オプション指定なしだとうまくファイルが作成できる
mkdir: cannot create directory ‘aaa’: File exists →　しかし、ディレクトリがあったようだ。
input2@prowl:/tmp$ mkdir iii → 再度ディレクトリを作成する
input2@prowl:/tmp$ cd iii
input2@prowl:/tmp/iii$ ls
input2@prowl:/tmp/iii$ vim sol.py  →　うまくいった。
```

因みに、vimでファイルを作成すると、以下のようなエラーが出るが気にしなくてよい。

```bash
Can't write viminfo file /home/input2/.viminfo!
```

# stage1
引数が１００文字で、ascii番号A(65)とB(64)に指定された文字を入力すると、突破できる。

```c
// argv
if(argc != 100) return 0;
if(strcmp(argv['A'],"\x00")) return 0;
if(strcmp(argv['B'],"\x20\x0a\x0d")) return 0;
printf("Stage  clear!\n");
```

pythonで答えを書いてみる

```python
import subprocess

def main():
        agt = "A" * 64 + "\x00\x00\x00\x00" + "\x00\x20\x0a\x0d" + "A" * 33
        subprocess.call(["/home/input2/input", agt])

if __name__ == '__main__':
        main()
```

しかし、なぜか失敗する。

```bash
input2@prowl:/tmp/iii$ python sol.py
Traceback (most recent call last):
  File "sol.py", line 26, in <module>
    main()
  File "sol.py", line 13, in main
    s=subprocess.call(["/home/input2/input", agt])
  File "/usr/lib/python2.7/subprocess.py", line 523, in call
    return Popen(*popenargs, **kwargs).wait()
  File "/usr/lib/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/usr/lib/python2.7/subprocess.py", line 1343, in _execute_child
    raise child_exception
TypeError: execv() arg 2 must contain only strings
```

エラーの意味がよくわからない。
全部strの気がするのだが・・・。
バイトから変換されていない？

とりあえず再修正

```python
mport subprocess

def main():
        agt = "A" * 64 + "" + "\x20\x0a\x0d" + "A" * 33
        subprocess.call(["/home/input2/input", agt])
if __name__ == '__main__':
        main()
```

しかし、Stage clear!がでない。
結局うまくいっていない・・・。

```bash
nput2@prowl:/tmp/iii$ python sol.py
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then
```

考えてみたら引数が100だから、文字列じゃないことに気づく・・・。
ということで、引数のリストを作る。

* argcは一番最初の引数にプログラム名が入るため、入力する文字は99文字で良い

```python
import subprocess

def main():
        agt = []
        for i in range(0,99):
                agt.append("A")
        agt[ord("A")-1] = ""
        agt[ord("B")-1] =  "\x20\x0a\x0d"
        print agt[1:]
        ans = ["/home/input2/input"]+agt
        print len(ans)
        subprocess.call( ans )

if __name__ == '__main__':
        main()

```bash
input2@prowl:/tmp/iii$ python sol.py
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '', ' \n\r', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
100
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
```

今度はうまくいった。

# stage2
パイプの問題

```c
// stdio
char buf[4];
read(0, buf, 4);
if(memcmp(buf, "\x00\x0a\x00\xff", 4)) return 0;
read(2, buf, 4  );
if(memcmp(buf, "\x00\x0a\x02\xff", 4)) return 0;
printf("Stage 2 clear!\n");
```

readの値がstdinとstderrに設定されているので、ここにパイプをつないで、指定された値を挿入すればよい。
* パイプは２つ必要(stdin, stderr)
* os.pipe()では読み込みと書き込みのペアを返すらしいので二つ用意する。以下python docs
```

os.pipe()

    パイプを作成します。読み込み、書き込みに使うことの出来るファイル記述子のペア (r, w) を返します。新しいファイル記述子は 継承不可 です。

    Availability: Unix, Windows。

    バージョン 3.4 で変更: 新しいファイル記述子が継承不可になりました。

```

以下、追加分
```python
        # stage 2
        stg21 = "\x00\x0a\x00\xff"
        stg22 = "\x00\x0a\x02\xff"

        # crete two pipe to communicate stdin, stderr
        stg21r, stg21w = os.pipe()
        stg22r, stg22w  = os.pipe()

        os.write(stg21w, "\x00\x0a\x00\xff" )
        os.write(stg22w,  "\x00\x0a\x02\xff" )


        # stage 3
        os.environ['\xde\xad\xbe\xef'] = '\xca\xfe\xba\xbe'


        ret = subprocess.Popen(ans, stdin=stg21r, stderr=stg22r)
```

うまくいった。

```bash
$ python sol.py
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '', ' \n\r', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
100
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
Stage 2 clear!
```

# stage3
環境変数を追加するだけ。

```c
        // env
        if(strcmp("\xca\xfe\xba\xbe", getenv("\xde\xad\xbe\xef"))) return 0;
        printf("Stage 3 clear!\n");
```

pythonで書くと以下のようになる。

```python
 # stage 3
        os.environ['\xde\xad\xbe\xef'] = '\xca\xfe\xba\xbe'
```

実行したら、なぜかstage4までクリアしてる・・・。
意味わからん。

```bash
$ python sol.py
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '', ' \n\r', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
100
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
Stage 2 clear!
Stage 3 clear!
Stage 4 clear!
```

# stage4
stage3でなぜかクリアできてしまったが、とりあえず書いてみる。
指定されたファイルを作成して書き込むだけ。

```c
        // file
        FILE* fp = fopen("\x0a", "r");
        if(!fp) return 0;
        if( fread(buf, 4, 1, fp)!=1 ) return 0;
        if( memcmp(buf, "\x00\x00\x00\x00", 4) ) return 0;
        fclose(fp);
        printf("Stage 4 clear!\n");
```

pythonで書くと以下になる。

```python
 # stage 4
        f = open("\x0a",mode="w")
        f.write("\x00\x00\x00\x00")
        f.close()
```

実行したら、うまくいった。

```bash
input2@prowl:/tmp/iii$ python sol.py
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '', ' \n\r', '49153', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
100
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
Stage 2 clear!
Stage 3 clear!
Stage 4 clear!
```
# stage5
ネットに接続して特定の値を送信するだけ。
通信するポートはプライベートポート番号ならどこでもいい気がする。
接続先はローカルアドレス。

```c

        // network
        int sd, cd;
        struct sockaddr_in saddr, caddr;
        sd = socket(AF_INET, SOCK_STREAM, 0);
        if(sd == -1){
                printf("socket error, tell admin\n");
                return 0;
        }
        saddr.sin_family = AF_INET;
        saddr.sin_addr.s_addr = INADDR_ANY;
        saddr.sin_port = htons( atoi(argv['C']) );
        if(bind(sd, (struct sockaddr*)&saddr, sizeof(saddr)) < 0){
                printf("bind error, use another port\n");
                return 1;
        }
        listen(sd, 1);
        int c = sizeof(struct sockaddr_in);
        cd = accept(sd, (struct sockaddr *)&caddr, (socklen_t*)&c);
        if(cd < 0){
                printf("accept error, tell admin\n");
                return 0;
        }
        if( recv(cd, buf, 4, 0) != 4 ) return 0;
        if(memcmp(buf, "\xde\xad\xbe\xef", 4)) return 0;
        printf("Stage 5 clear!\n");
```

pythonで書くと以下のようになる。

```python
 # stage 5
        s = socket.socket(socket.af_inet, socket.sock_stream)
        port = int(agt[ord("c")-1])
        s.connect(('127.0.0.1', port))
        s.send('\xde\xad\xbe\xef')

```

実行したら、bindエラーでなぜか怒られたけど、なぜかフラグがゲットできたので良しとしよう。

```bash
input2@prowl:/tmp/iii$ python sol.py
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '', ' \n\r', '49153', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
100
Stage 5 clear!
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
Stage 2 clear!
Stage 3 clear!
Stage 4 clear!
bind error, use another port
Mommy! I learned how to pass various input in Linux :)
```

フラグゲット
