k1=0
import ctypes,sys
STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
n=int(input())
while(1):
	for i in range(2*n-1):	
		if(i+1>n):
			k=2*n-i-1
		else:
			k=i+1
		ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, ((k+k1)//2)%16)
		for j in range(n-k):
			print(" ",end='')
		for j in range(2*k-1):
			if(j<=k-2):
				c=chr(65+j+k1)
			else:
				c=chr(65+2*k-j-2+k1)
			print(c,end='')
		print()
	import os
	os.system('cls')
	k1=(k1+1)%40
input()
