# 内容
"id0-rsa.pub"という文字列をsha256でハッシュ化し、その結果をmd5でハッシュ化する問題。
入門と言うことで、問題の指示に従って回答した。

# 使用するコマンド
* sha256sum　：　sha256のハッシュ化
* md5sum　：　md5のハッシュ化

# 解答
ワンライナーで書くのに苦戦した。
awkなんて使うことないし・・・。 
* 最後のハイフンはいらない。
```bash
printf "id0-rsa.pub" | sha256sum | awk -F " " '{printf $1}' | md5sum
b25d449d86aa07981d358d3b71b891de  -
```
フラグゲット
