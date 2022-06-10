# XOR_Reverse_Shellcode
XOR_Reverse_Shellcode with client (victime) and server (attacker) in python <br>

## Two main programms 
 - client (victime) : tcp bind shellcode with (normally) a xor en/decrytion
 - server (attacker) : listener in python with xor en/decryption

----

## Client 

sys_socket <br>
sys_connect <br>
sys_read <br> 
sys_fork <br>
sys_execve <br>

----

## to compile asm code :
```
nasm -f elf64 -F stabs code.asm ; ld -o code.bin code.o
```
