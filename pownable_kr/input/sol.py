import subprocess
import os
import socket

def main():
	
	# stage 1
	agt = []
	for i in range(0,99):
		agt.append("A")
	agt[ord("A")-1] = ""
	agt[ord("B")-1] =  "\x20\x0a\x0d"
	agt[ord("C")-1] = str(49153) # dynamic / private port number
	print agt[1:]
	ans = ["/home/input2/input"]+agt 
	print len(ans)
	
	# stage 2
	stg21 = "\x00\x0a\x00\xff"
	stg22 = "\x00\x0a\x02\xff"
	
	# crete two pipe to communicate stdin, stderr
	stg21r, stg21w = os.pipe()	
	stg22r, stg22w  = os.pipe()
	
	os.write(stg21w, "\x00\x0a\x00\xff" )
	os.write(stg22w,  "\x00\x0a\x02\xff" )	


	# stage 3
	os.environ['\xde\xad\xbe\xef'] = '\xca\xfe\xba\xbe'
		
	# stage 4
	f = open("\x0a",mode="w")
	f.write("\x00\x00\x00\x00")
	f.close()

	# system call
	ret = subprocess.Popen(ans, stdin=stg21r, stderr=stg22r)
	
	# stage 5
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = int(agt[ord("C")-1])
	s.connect(('127.0.0.1', port))
	s.send('\xde\xad\xbe\xef')

if __name__ == '__main__':
	main()
