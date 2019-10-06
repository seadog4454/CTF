# 内容
armのアセンブラを読み解く問題。
まず、サーバーに接続してみる。

```bash
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
Last login: Sat Jul 20 11:38:18 2019 from 126.209.18.0
pulseaudio: pa_context_connect() failed
pulseaudio: Reason: Connection refused
pulseaudio: Failed to initialize PA contextaudio: Could not init `pa' audio driver
ALSA lib confmisc.c:768:(parse_card) cannot find card '0'
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_card_driver returned error: No such file or directory
ALSA lib confmisc.c:392:(snd_func_concat) error evaluating strings
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
ALSA lib confmisc.c:1251:(snd_func_refer) error evaluating name
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4771:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2266:(snd_pcm_open_noupdate) Unknown PCM default
alsa: Could not initialize DAC
alsa: Failed to open `default':
alsa: Reason: No such file or directory
ALSA lib confmisc.c:768:(parse_card) cannot find card '0'
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_card_driver returned error: No such file or directory
ALSA lib confmisc.c:392:(snd_func_concat) error evaluating strings
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
ALSA lib confmisc.c:1251:(snd_func_refer) error evaluating name
ALSA lib conf.c:4292:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4771:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2266:(snd_pcm_open_noupdate) Unknown PCM default
alsa: Could not initialize DAC
alsa: Failed to open `default':
alsa: Reason: No such file or directory
audio: Failed to create voice `lm4549.out'
Uncompressing Linux... done, booting the kernel.
[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 3.11.4 (acez@pondicherry) (gcc version 4.7.3 (Sourcery CodeBench Lite 2013.05-24) ) #5 Sat Oct 12 00:15:00 EDT 2013
[    0.000000] CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=00093177
[    0.000000] CPU: VIVT data cache, VIVT instruction cache
[    0.000000] Machine: ARM-Versatile PB
[    0.000000] Memory policy: ECC disabled, Data cache writeback
[    0.000000] sched_clock: 32 bits at 24MHz, resolution 41ns, wraps every 178956ms
[    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 16256
[    0.000000] Kernel command line: 'root=/dev/ram rw console=ttyAMA0 rdinit=/sbin/init oops=panic panic=1 quiet'
[    0.000000] PID hash table entries: 256 (order: -2, 1024 bytes)
[    0.000000] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
[    0.000000] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
[    0.000000] Memory: 59760K/65536K available (2522K kernel code, 150K rwdata, 656K rodata, 112K init, 93K bss, 5776K reserved)
[    0.000000] Virtual kernel memory layout:
[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
[    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
[    0.000000]     vmalloc : 0xc4800000 - 0xff000000   ( 936 MB)
[    0.000000]     lowmem  : 0xc0000000 - 0xc4000000   (  64 MB)
[    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
[    0.000000]       .text : 0xc0008000 - 0xc0322cc8   (3180 kB)
[    0.000000]       .init : 0xc0323000 - 0xc033f22c   ( 113 kB)
[    0.000000]       .data : 0xc0340000 - 0xc0365b20   ( 151 kB)
[    0.000000]        .bss : 0xc0365b20 - 0xc037d2bc   (  94 kB)
[    0.000000] NR_IRQS:224
[    0.000000] VIC @f1140000: id 0x00041190, vendor 0x41
[    0.000000] FPGA IRQ chip 0 "SIC" @ f1003000, 13 irqs
[    0.000000] Console: colour dummy device 80x30
[    0.018793] Calibrating delay loop... 519.78 BogoMIPS (lpj=2598912)
[    0.315961] pid_max: default: 32768 minimum: 301
[    0.316895] Mount-cache hash table entries: 512
[    0.323387] CPU: Testing write buffer coherency: ok
[    0.328681] Setting up static identity map for 0xc0265c80 - 0xc0265cbc
[    0.338409] NET: Registered protocol family 16
[    0.339919] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.344814] Serial: AMBA PL011 UART driver
[    0.346362] dev:f1: ttyAMA0 at MMIO 0x101f1000 (irq = 44) is a PL011 rev1
[    0.353419] console [ttyAMA0] enabled
[    0.354462] dev:f2: ttyAMA1 at MMIO 0x101f2000 (irq = 45) is a PL011 rev1
[    0.354942] dev:f3: ttyAMA2 at MMIO 0x101f3000 (irq = 46) is a PL011 rev1
[    0.355352] fpga:09: ttyAMA3 at MMIO 0x10009000 (irq = 70) is a PL011 rev1
[    0.361854] bio: create slab <bio-0> at 0
[    0.369513] Switched to clocksource timer3
[    0.378203] NET: Registered protocol family 2
[    0.383300] TCP established hash table entries: 512 (order: 0, 4096 bytes)
[    0.383610] TCP bind hash table entries: 512 (order: -1, 2048 bytes)
[    0.383923] TCP: Hash tables configured (established 512 bind 512)
[    0.384558] TCP: reno registered
[    0.384772] UDP hash table entries: 256 (order: 0, 4096 bytes)
[    0.385054] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
[    0.386827] NET: Registered protocol family 1
[    0.389354] RPC: Registered named UNIX socket transport module.
[    0.389534] RPC: Registered udp transport module.
[    0.389693] RPC: Registered tcp transport module.
[    0.389843] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.394465] Trying to unpack rootfs image as initramfs...
[    0.588490] Freeing initrd memory: 1584K (c2000000 - c218c000)
[    0.588857] NetWinder Floating Point Emulator V0.97 (double precision)
[    0.594997] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
[    0.595965] msgmni has been set to 119
[    0.621789] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 254)
[    0.622197] io scheduler noop registered
[    0.622393] io scheduler deadline registered
[    0.622633] io scheduler cfq registered (default)
[    0.623416] clcd-pl11x dev:20: PL110 rev0 at 0x10120000
[    0.625527] clcd-pl11x dev:20: Versatile hardware, VGA display
[    0.664114] Console: switching to colour frame buffer device 80x60
[    0.680474] brd: module loaded
[    0.681481] physmap platform flash device: 04000000 at 34000000
[    0.690492] physmap-flash.0: Found 1 x32 devices at 0x0 in 32-bit bank. Manufacturer ID 0x000000 Chip ID 0x000000
[    0.691134] Intel/Sharp Extended Query Table at 0x0031
[    0.691768] Using buffer write method
[    0.700246] smc91x.c: v1.1, sep 22 2004 by Nicolas Pitre <nico@fluxnic.net>
[    0.714276] eth0: SMC91C11xFD (rev 1) at c496e000 IRQ 57 [nowait]
[    0.714629] eth0: Ethernet addr: 52:54:00:12:34:56
[    0.715952] mousedev: PS/2 mouse device common for all mice
[    0.719698] TCP: cubic registered
[    0.719853] NET: Registered protocol family 17
[    0.720580] NET: Registered protocol family 37
[    0.720839] VFP support v0.3: implementor 41 architecture 1 part 10 variant 9 rev 0
[    0.730791] Freeing unused kernel memory: 112K (c0323000 - c033f000)
cttyhack: can't open '/dev/ttyS0': No such file or directory
sh: can't access tty; job control turned off
[    0.818110] input: AT Raw Set 2 keyboard as /devices/fpga:06/serio0/input/input0
/ $ [    1.418163] input: ImExPS/2 Generic Explorer Mouse as /devices/fpga:07/serio1/input/input1
```

ログインしたら、よくわからないlogを出力した。
logを見るとbootって単語があるから、ログインするたび仮想環境を立てている？
まぁいいか。
とりあえず続き。

```bash
/ $ ls
bin      dev      flag     linuxrc  root     sys
boot     etc      leg      proc     sbin     usr
/ $ cat flag
cat: can't open 'flag': Permission denied
/ $ ./leg
Daddy has very strong arm! : aaaaaa
I have strong leg :P
/ $
```

I have strong legってなに？何のスラング？足が達者ってなんだ？
よくわからんけど、とりあえず、サイトに提示されているｃ言語とアセンブリのソースを見ていこう。
まずはc言語から。
* scpでバイナリをダウンロードしようとしたけど、ログインするたびbootするもんだから、ダウンロードできない。
* まぁ今回はバイナリいらないからいいんだけどね

```c
#include <stdio.h>
#include <fcntl.h>
int key1(){
	asm("mov r3, pc\n");
}
int key2(){
	asm(
	"push	{r6}\n"
	"add	r6, pc, $1\n"
	"bx	r6\n"
	".code   16\n"
	"mov	r3, pc\n"
	"add	r3, $0x4\n"
	"push	{r3}\n"
	"pop	{pc}\n"
	".code	32\n"
	"pop	{r6}\n"
	);
}
int key3(){
	asm("mov r3, lr\n");
}
int main(){
	int key=0;
	printf("Daddy has very strong arm! : ");
	scanf("%d", &key);
	if( (key1()+key2()+key3()) == key ){
		printf("Congratz!\n");
		int fd = open("flag", O_RDONLY);
		char buf[100];
		int r = read(fd, buf, 100);
		write(0, buf, r);
	}
	else{
		printf("I have strong leg :P\n");
	}
	return 0;
}

```
ｃ言語のソースを見ると、key1(),key2(),key3()の戻り値の和が入力値と同じならflagがゲットできる模様。
アセンブラは最初のlogを確認すると、以下のようにCPUがarmであることがわかるため、アセンブラはarmの命令セットになる。

```
CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=00093177
```

ということで、key1()から順に解いていく。

# key1()
r3レジスタにpcの値を入れているだけ。
なので、pcの値さえ分かればクリア。
* pc：プログラムカウンタ
* プログラムカウンタ　：　次の命令するメモリの番地を保持するレジスタ（たぶんあってる。）

```c
int key1(){
	asm("mov r3, pc\n");
}
```

プログラムカウンタの値を見るにはアドレス番地を確認する必要があるため、アセンブラを見ていく。

```asm
(gdb) disass main
Dump of assembler code for function main:
   0x00008d3c <+0>:	push	{r4, r11, lr}
   0x00008d40 <+4>:	add	r11, sp, #8
   0x00008d44 <+8>:	sub	sp, sp, #12
   0x00008d48 <+12>:	mov	r3, #0
   0x00008d4c <+16>:	str	r3, [r11, #-16]
   0x00008d50 <+20>:	ldr	r0, [pc, #104]	; 0x8dc0 <main+132>
   0x00008d54 <+24>:	bl	0xfb6c <printf>
   0x00008d58 <+28>:	sub	r3, r11, #16
   0x00008d5c <+32>:	ldr	r0, [pc, #96]	; 0x8dc4 <main+136>
   0x00008d60 <+36>:	mov	r1, r3
   0x00008d64 <+40>:	bl	0xfbd8 <__isoc99_scanf>
   0x00008d68 <+44>:	bl	0x8cd4 <key1>
   0x00008d6c <+48>:	mov	r4, r0
   0x00008d70 <+52>:	bl	0x8cf0 <key2>
   0x00008d74 <+56>:	mov	r3, r0
   0x00008d78 <+60>:	add	r4, r4, r3
   0x00008d7c <+64>:	bl	0x8d20 <key3>
   0x00008d80 <+68>:	mov	r3, r0
   0x00008d84 <+72>:	add	r2, r4, r3
   0x00008d88 <+76>:	ldr	r3, [r11, #-16]
   0x00008d8c <+80>:	cmp	r2, r3
   0x00008d90 <+84>:	bne	0x8da8 <main+108>
   0x00008d94 <+88>:	ldr	r0, [pc, #44]	; 0x8dc8 <main+140>
   0x00008d98 <+92>:	bl	0x1050c <puts>
   0x00008d9c <+96>:	ldr	r0, [pc, #40]	; 0x8dcc <main+144>
   0x00008da0 <+100>:	bl	0xf89c <system>
   0x00008da4 <+104>:	b	0x8db0 <main+116>
   0x00008da8 <+108>:	ldr	r0, [pc, #32]	; 0x8dd0 <main+148>
   0x00008dac <+112>:	bl	0x1050c <puts>
   0x00008db0 <+116>:	mov	r3, #0
   0x00008db4 <+120>:	mov	r0, r3
   0x00008db8 <+124>:	sub	sp, r11, #8
   0x00008dbc <+128>:	pop	{r4, r11, pc}
   0x00008dc0 <+132>:	andeq	r10, r6, r12, lsl #9
   0x00008dc4 <+136>:	andeq	r10, r6, r12, lsr #9
   0x00008dc8 <+140>:			; <UNDEFINED> instruction: 0x0006a4b0
   0x00008dcc <+144>:			; <UNDEFINED> instruction: 0x0006a4bc
   0x00008dd0 <+148>:	andeq	r10, r6, r4, asr #9
End of assembler dump.
(gdb) disass key1
Dump of assembler code for function key1:
   0x00008cd4 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008cd8 <+4>:	add	r11, sp, #0
   0x00008cdc <+8>:	mov	r3, pc
   0x00008ce0 <+12>:	mov	r0, r3
   0x00008ce4 <+16>:	sub	sp, r11, #0
   0x00008ce8 <+20>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008cec <+24>:	bx	lr
End of assembler dump.
(gdb) disass key2
Dump of assembler code for function key2:
   0x00008cf0 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008cf4 <+4>:	add	r11, sp, #0
   0x00008cf8 <+8>:	push	{r6}		; (str r6, [sp, #-4]!)
   0x00008cfc <+12>:	add	r6, pc, #1
   0x00008d00 <+16>:	bx	r6
   0x00008d04 <+20>:	mov	r3, pc
   0x00008d06 <+22>:	adds	r3, #4
   0x00008d08 <+24>:	push	{r3}
   0x00008d0a <+26>:	pop	{pc}
   0x00008d0c <+28>:	pop	{r6}		; (ldr r6, [sp], #4)
   0x00008d10 <+32>:	mov	r0, r3
   0x00008d14 <+36>:	sub	sp, r11, #0
   0x00008d18 <+40>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008d1c <+44>:	bx	lr
End of assembler dump.
(gdb) disass key3
Dump of assembler code for function key3:
   0x00008d20 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008d24 <+4>:	add	r11, sp, #0
   0x00008d28 <+8>:	mov	r3, lr
   0x00008d2c <+12>:	mov	r0, r3
   0x00008d30 <+16>:	sub	sp, r11, #0
   0x00008d34 <+20>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008d38 <+24>:	bx	lr
End of assembler dump.
(gdb) 

```

key1だけ抜き出し考えてみる。


```asm
(gdb) disass key1
Dump of assembler code for function key1:
   0x00008cd4 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008cd8 <+4>:	add	r11, sp, #0
   0x00008cdc <+8>:	mov	r3, pc
   0x00008ce0 <+12>:	mov	r0, r3
   0x00008ce4 <+16>:	sub	sp, r11, #0
   0x00008ce8 <+20>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008cec <+24>:	bx	lr
```

ｃのコードではkey1()内に **mov r3, pc** 以外なかったので、ほかの部分は初期化処理と考えるべき。
でも、オペコードがわからないままは気持ち悪いので、一応わからないオペコードだけ調べる。

* bx　：　分岐命令。jmpとかrtnとかに似てる感じかな？armの公式サイトの日本語訳には以下のように書いてあるんだけど、日本語でokって感じですね。
分岐って言ってるぐらいだし、bがbranch(綴りあってる？)を意味しているってことだけはわかった。

[http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Cihfddaf.html](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Cihfddaf.html)

```
B
分岐命令です。

BL
リンク付き分岐命令です。

BLX
リンク付き分岐と命令セットの切り替えを行う命令です。
```

* lr ：　リンクレジスタ。リターンアドレスを保持。
* r11 ：　フレームポインタ(fp)。ベースポインタみたいなもの？といかベースとの違いってあるのか？
* r0　：　戻り値
* sp　：　スタックポインタ
* add　：　加算命令。
    * 第一オペランド　：　加算結果の保持
    * 第二オペランド　：　計算元
    * 第三オペランド  ；　計算元
* イミディエイト　：　シャープ(#)の次に記述する。　例、　#0

これらを理解したうえにソースをもう一度見てみる。
そうすると、
ソースでは、関数に引数も変数もない。つまり、スタックは0なため、r11に0を足して最後に0を引き、そして、リターンアドレス先にジャンプするだけの処理であることがわかる。

とまぁ、話が脱線してしまったので、問題の **mov r3, pc** を見ていく。
pcとは先ほども言った通り、次の命令のメモリ番地を保持している。
そのため、次のアドレスの **0x00008ce0** が正解だと思ったのだが、違うらしい。
armの公式ドキュメントでは以下のように書かれている。

[http://infocenter.arm.com/help/topic/com.arm.doc.dui0473gj/Babbdajb.html(http://infocenter.arm.com/help/topic/com.arm.doc.dui0473gj/Babbdajb.html)

```
現在実行中の命令のアドレスは、PC にはストアされません。通常、現在実行中の命令のアドレスは、ARM 命令では PC-8、Thumb 命令では PC-4 になります。
```

つまり、 **現在のメモリ番地 = PC - 8** ってこと？そうしたら、PCは現在のアドレスの８バイト先ってことになるんだけど・・・。
それだと、**mov r0, r3** は **mov r3, pc** の4バイト先だからこれ呼ばれなくね？
本当にわけわからん・・・・。
これで、どうやってarmが動いているかわ知らんが、とりあえず、そういうことなんだろう。
気を取り直して、答えを算出。

> 現在のアドレス(0x00008cdc) ＋ 8 = 0x8ce4

# key2()
まずはソースを見ていく。


```c
int key2(){
	asm(
	"push	{r6}\n"
	"add	r6, pc, $1\n"
	"bx	r6\n"
	".code   16\n"
	"mov	r3, pc\n"
	"add	r3, $0x4\n"
	"push	{r3}\n"
	"pop	{pc}\n"
	".code	32\n"
	"pop	{r6}\n"
	);
}
```

```asm
(gdb) disass key2
Dump of assembler code for function key2:
   0x00008cf0 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008cf4 <+4>:	add	r11, sp, #0
   0x00008cf8 <+8>:	push	{r6}		; (str r6, [sp, #-4]!)
   0x00008cfc <+12>:	add	r6, pc, #1
   0x00008d00 <+16>:	bx	r6
   0x00008d04 <+20>:	mov	r3, pc
   0x00008d06 <+22>:	adds	r3, #4
   0x00008d08 <+24>:	push	{r3}
   0x00008d0a <+26>:	pop	{pc}
   0x00008d0c <+28>:	pop	{r6}		; (ldr r6, [sp], #4)
   0x00008d10 <+32>:	mov	r0, r3
   0x00008d14 <+36>:	sub	sp, r11, #0
   0x00008d18 <+40>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008d1c <+44>:	bx	lr
End of assembler dump.
```


また、.codeとかいうわけのわからないオペコードが出てきた。
しかも、実際のアセンブリにはそんなオペコード無いし・・・。
しかし、公式のサイトで調べてみると、このコードはディスアセンブリした時は出てこないことが分かった。

[http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Ciaeahej.html](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Ciaeahej.html)

```
ARM ディレクティブと CODE32 ディレクティブは同じ意味です。 これらは、UAL 構文か Thumb-2 以前の ARM アセンブラ言語構文のいずれかを使用して、後に続く命令を ARM 命令として解釈するようアセンブラに指示します。

THUMB ディレクティブは、UAL 構文を使用して、後に続く命令を Thumb 命令として命令を解釈するようにアセンブラに指示します。

THUMBX ディレクティブは、UAL 構文を使用して、後に続く命令を Thumb-2EE 命令として解釈するようにアセンブラに指示します。

CODE16 ディレクティブは、UAL 以前のアセンブリ言語構文を使用して、後に続く命令を Thumb 命令として解釈するようにアセンブラに指示します。


これらのディレクティブをアセンブルしても、命令は生成されません。 また、状態が変更されるわけでもありません。 これらのディレクティブは、ARM、Thumb、または Thumb-2EE の命令を適切にアセンブルするようアセンブラに指示し、必要に応じてパディングを挿入するだけです。
```

文面に書かれているTHUMBってなによってことなんだが、どうやら、armは処理効率を上げるために、16bitの命令セットが用意されているらしい。
以下公式ドキュメント。

[http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0473bj/CEGBEIJB.html](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0473bj/CEGBEIJB.html)

```
ARMv4T 以降のアーキテクチャでは、Thumb と呼ばれる 16 ビットの命令セットが定義されています。この命令セットでは、32 ビット ARM 命令セットのほとんどの機能を使用できますが、一部の処理にはより多くの命令が必要になります。Thumb 命令セットでは、パフォーマンスと引き換えに優れたコード密度を実現しています。
```

そんでもって、これを切り替えるためにはBX命令が必要になる。
以下、公式ドキュメント

[http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0489fj/Cihfddaf.html](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0489fj/Cihfddaf.html)

```
BX Rm と BLX Rm を使用すると Rm のビット [0] からターゲットの状態を得ることができます。

Rm のビット [0] が 0 の場合、プロセッサは ARM 状態に切り替わるか、ARM 状態が維持されます。

Rm のビット [0] が 1 の場合、プロセッサは Thumb 状態に切り替わるか、Thumb 状態が維持されます。
```

これを理解したうえでもう一度ソースを読んでみると、以下のコードは次の命令からはthumbの命令に変わりますよというように読み取れる。

```asm
0x00008cfc <+12>:	add	r6, pc, #1
0x00008d00 <+16>:	bx	r6
```

そして、thumb命令に入ると、r3にpcを代入した後、4を足している。

```asm
0x00008d04 <+20>:	mov	r3, pc
0x00008d06 <+22>:	adds	r3, #4
```

この時重要になってくるのがpcの値なのだが、これはarmの時と違い、thumb命令時のpcは現在のアドレス+4になる。
先ほども載せたが、公式ドキュメントには以下のように記述されている。

```
現在実行中の命令のアドレスは、PC にはストアされません。通常、現在実行中の命令のアドレスは、ARM 命令では PC-8、Thumb 命令では PC-4 になります。
```

よってr3の値は以下のようになる。

> 0x00008d04 + 4 + 4 = 0x8d0c

そして、そのあと、スタックにpush,popしている。

```
0x00008d08 <+24>:	push	{r3}
0x00008d0a <+26>:	pop	{pc}
0x00008d0c <+28>:	pop	{r6}
```

ここで、重要になってくるのが、**pop {pc}** 。
pop命令時にpcがオペランドで指定されたとき、thumbか、armに分岐する。
分岐方法はアドレスの最後が0か1かで変わる。
以下、公式ドキュメント。

[http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Babefbce.html](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0204ij/Babefbce.html)

```
この命令は、スタックから PC にポップされたアドレスへの分岐を発生させます。一般的には、サブルーチンからの復帰に使用します。サブルーチンでは LR がサブルーチン開始位置でスタックにプッシュされます。

ARMv5T 以降には以下のような特徴があります。

ビット [1:0] は 0b10 にできません。

ビット [0] が 1 なら、Thumb 状態で実行が継続します。

ビット [0] が 0 なら、ARM 状態で実行が継続します。
```

今回のr3レジスタは二進数にすると以下になることから、ここでarmに戻ることがわかる。

> 0x8d0c = 1000110100001100

最後はr3レジスタを戻り値r0に代入して終了

```
0x00008d10 <+32>:	mov	r0, r3
0x00008d14 <+36>:	sub	sp, r11, #0
0x00008d18 <+40>:	pop	{r11}		; (ldr r11, [sp], #4)
0x00008d1c <+44>:	bx	lr
```

と、いうことで、戻り値は以下になる。

> 0x8d0c

# key3()
まず、ソースを見ていく。

```c
int key3(){
	asm("mov r3, lr\n");
}
```

```asm
(gdb) disass key3
Dump of assembler code for function key3:
   0x00008d20 <+0>:	push	{r11}		; (str r11, [sp, #-4]!)
   0x00008d24 <+4>:	add	r11, sp, #0
   0x00008d28 <+8>:	mov	r3, lr
   0x00008d2c <+12>:	mov	r0, r3
   0x00008d30 <+16>:	sub	sp, r11, #0
   0x00008d34 <+20>:	pop	{r11}		; (ldr r11, [sp], #4)
   0x00008d38 <+24>:	bx	lr
End of assembler dump.
```

lr→r3→r0という感じで代入されているのがわかる。
このことから、lrの値がわかればよい。

lrは先ほども申したがリンクレジスタの略で、リターンアドレスを保持している。
ということで、main関数のkey3()が呼ばれた後のアドレス値が答え。
以下main関数のアセンブリの抜粋。

```asm
0x00008d68 <+44>:	bl	0x8cd4 <key1>
0x00008d6c <+48>:	mov	r4, r0
0x00008d70 <+52>:	bl	0x8cf0 <key2>
0x00008d74 <+56>:	mov	r3, r0
0x00008d78 <+60>:	add	r4, r4, r3
0x00008d7c <+64>:	bl	0x8d20 <key3>
0x00008d80 <+68>:	mov	r3, r0
```

よって答えは以下
> 0x8d80

# 答え
key1(), key2(), key3()の戻りの和を計算すると以下になる。

> 0x8ce4 + 0x8d0c + 0x8d80 = 0x1a770


実際に答えとして入力するときは１０進数に直す。
なぜなら、scanfはint型だから。

> 0x1a770 = 108400

```bash
/ $ ./leg
Daddy has very strong arm! : 108400
Congratz!
My daddy has a lot of ARMv5te muscle!
/ $
```

フラグゲット。
