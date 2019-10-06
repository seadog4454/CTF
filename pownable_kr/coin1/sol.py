import socket
import time
import re


def sol2(client, cnt):
  res = client.recv(2 ** 4)
  print(res)
  
  N = re.search(rb'N=([0-9]+)' , res).group(1).decode('utf-8')
  C = re.search(rb'C=([0-9]+)' , res).group(1).decode('utf-8')
  print("N = " + str(N) + ", C = " + str(C) )


  left = 0
  right = int(N)
  mid = int(int(N)/2)
    
  i = left
  j = mid + 1

  for chanceCnt in range(1, int(C) + 2 ):
    print("chance = " + str(chanceCnt) )
    msg = ""
    for indexCnt in range(i, j):
      msg += str(indexCnt) + " "
    print("msg = " + msg)
    msg += "\n"
    client.send( msg.encode('utf-8') )
    res = client.recv(2 ** 4).decode('utf-8')
    #res = re.search(rb'[0-9]+' , res).group(0).decode('utf-8')
    print("responce = " + str(res).replace("\n", "") )
    
    if res.find("Correct!") != -1:
      break

    if int(res)%10 == 0:
      i = j
      j = j + int((right-j)/2)
    elif int(res) == 9:
      continue
    else:
      right = j
      j = i + int( (j - i) / 2 )

    if i == j and j != right:
      j += 1
    if i == j  and j == right:
      i -= 1
    print("i = " + str(i) + ", j = " + str(j) + ", right = " + str(right) + "\n")   

def sol():
  port = 9007
  host = "pwnable.kr"
  #host = '127.0.0.1'
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  res = client.recv(2 ** 11)
  cnt = 0
  while True:
    print(str(cnt))
    sol2(client, cnt)
    cnt += 1
    if cnt > 99:
      res = client.recv(2 ** 11).decode('utf-8')
      print(res)
      break
  client.close()

def main():
  sol()

if __name__ == '__main__':
  main()
