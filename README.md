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

## Compile asm code :
```
nasm -f elf64 -F stabs code.asm ; ld -o code.bin code.o
```
----
## To Do :

### server 

- clean exit quand on reçoit ```Erreur de reception. Aucune donnée reçu.``` dans la boucle while True
- rendre le code plus jolie si possible

### client : 

- bien faire le fork
- sys_write de stdout vers l'attanquant (server)
- résoudre le problème de reception d'uniquement 8 caractères

### script poly/metamorphique :

- reprendre le script du S1
- ajouter le polymorphisme au métamorphisme
- calculer et afficher la final du shellcode 