filepointer = open("binary.txt", "r")
contents = filepointer.read()
binary_list = contents.split(" ")

list_of_eight_bytes = []
eight_byte_cnt = 1
byte4tmp = ""

print(binary_list)

# split 8byte
for byte in binary_list:
    byte4tmp = byte + byte4tmp
    if eight_byte_cnt == 8: #if count 8 bytes, initialize.
        list_of_eight_bytes.append(byte4tmp)
        byte4tmp = ""
        eight_byte_cnt = 1
        continue
    eight_byte_cnt += 1

#if eight_byte_cnt != 0:
list_of_eight_bytes.append(byte4tmp)

print(list_of_eight_bytes)

reverse = list_of_eight_bytes[::-1]
list_cnt = 0
for byte in reverse:
    reverse[list_cnt] = "movq $0x" + byte + ", %rax"
    print(reverse[list_cnt])
    print("push %rax")
    list_cnt += 1
