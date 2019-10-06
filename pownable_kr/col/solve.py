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
  

