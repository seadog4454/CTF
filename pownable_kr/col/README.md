入力からhash値0x21DD09ECになるような値を２０文字入力しろと言う問題。
最初の問題と同じく、systemコールでflagを読めるようにしている。

* col.c
```c
include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```

# フローチャート
1. 引数が２０文字だとcheck_passwordに飛ぶ
2. 引数の20文字をint型に変換する
	* この時、charは1バイト、intは4バイトなので、intは５つの配列を持つことなる。
  * また、例えば、"0xEC 0x09 0xDD 0x21"といった文字列がある場合は、intにするとき、0x21CC09ECとつながる模様。
3. ５つの配列をforで回してインクリメントする
4. インクリメントした結果と指定されたhash値があっていれば、flagゲット

# 回答手順
最後のところから逆算していけばおのずと答えが分かる。
1. 指定されたhash値を10進数にする
2. hash値を5で割る(/5)ことで、int配列１つ分を計算する。
3. hash値を5で除算した値(mod 5)と、hash値を割った値(/5)を足すことで、hash値が割り切れなかった時の値を算出する。
4. 2,3で計算した値を16進数にする
5. リトルエンディアンで値を挿入する。

# ソースコード
```python
# ５回インクリメントしたら0x21DD09ECになるような20バイトの文字を探す
if __name__ == '__main__':
  hashcode = '0x21DD09EC'
  print("hachcode = " + hashcode)
  hashint = int(hashcode, 16)
  quo = int(hashint/5) # 5で割れば１配列で必要なバイト数が分かる
  re = int(hashint % 5) # そもそもhashcodeが5で割り切れないため、余りを算出する
  quoh = hex(quo)
  reh = hex(re + quo)
  print("quo　：　21DD09EC/5 = " + quoh )
  print("re　：　21DD09EC%5 + quo = " + reh )
  print("re + quo*4 = " + hex(quo * 4 + quo + re) )
```

# 回答
```bash
$ python3 solve.py
hachcode = 0x21DD09EC
quo　：　21DD09EC/5 = 0x6c5cec8
re　：　21DD09EC%5 + quo = 0x6c5cecc
re + quo*4 = 0x21dd09ec

$ ssh col@pwnable.kr -p2222
col@pwnable.kr's password:
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
Last login: Tue Jul  9 01:51:30 2019 from 37.111.13.145
col@prowl:~$ ls -la
total 36
drwxr-x---   5 root    col     4096 Oct 23  2016 .
drwxr-xr-x 114 root    root    4096 May 19 15:59 ..
d---------   2 root    root    4096 Jun 12  2014 .bash_history
-r-sr-x---   1 col_pwn col     7341 Jun 11  2014 col
-rw-r--r--   1 root    root     555 Jun 12  2014 col.c
-r--r-----   1 col_pwn col_pwn   52 Jun 11  2014 flag
dr-xr-xr-x   2 root    root    4096 Aug 20  2014 .irssi
drwxr-xr-x   2 root    root    4096 Oct 23  2016 .pwntools-cache
col@prowl:~$ cat ./col.c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
col@prowl:~$
col@prowl:~$ python -c 'print "\xc8\xce\xc5\x06" * 4 + "\xcc\xce\xc5\x06"' | ./col
usage : ./col [passcode]
close failed in file object destructor:
sys.excepthook is missing
lost sys.stderr
col@prowl:~$ ./col $(python -c 'print "\xc8\xce\xc5\x06" * 4 + "\xcc\xce\xc5\x06"' )
daddy! I just managed to create a hash collision :)
```

フラグゲット。
ただ、最初にパイプで行けなかった理由は何なんだろうと考えてしまう・・・。
