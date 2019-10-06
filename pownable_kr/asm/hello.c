#include <stdio.h>
#include <unistd.h>
#include<fcntl.h>

void func(){
 int fd = open("this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong", O_RDONLY);

 char buff[100];
 int rc = read(fd, buff, 99);
 printf("%s\n", buff);
}

int main(){
  printf("Hello world!\n");
  func();
  return 0;
}
