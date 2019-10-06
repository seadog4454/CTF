# 内容
以下の値をROT3しろって内容

## シーザー暗号とは？
アルファベットを３文字分シフト(前もしくは後)して暗号文を作る。

[wikipediaより参照](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%BC%E3%82%B6%E3%83%BC%E6%9A%97%E5%8F%B7)

また、これの上位互換でROT13というものもある。

[wikipediaより参照](https://ja.wikipedia.org/wiki/ROT13)

上でROT3しろって言ってるのは、3文字シフトしろと言う意味。

# 解答
以下のようにROTするスクリプトを書いた。


```python
def caesar(text):
  res = ""
  for ch in text:
    ascii = ord(ch)
    if (ascii < ord('A') or ascii > ord('Z') ) and ( ascii < ord('a') or ascii > ord('z') ):
      res += ch
      continue
    res += chr( ord(ch) - 3 )    
  return res
  

def main():
  flag = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"
  res = caesar(flag)
  print(res)

if __name__ == '__main__':  
  main()
```


```bash 
$ python3 sol.py
 cpaw{Caesar_cipher_is_classical_cipher}
```

フラグゲット
