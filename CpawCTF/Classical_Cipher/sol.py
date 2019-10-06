
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
