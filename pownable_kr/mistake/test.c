#include<stdio.h>
#include<string.h>

int main(void){
  char s[11] = "abcdefghij";
  printf("%s\n", s);
  for(int i = 0; i < strlen(s); i++){
    printf("%x ", s[i]);
  }
  printf("\n");
  int reverse = 1;
  char s2[11];

  for(int i = 0; i < strlen(s); i++){
    s2[i] = s[i] ^ reverse;
    printf("%x ", s2[i]);
  }
  printf("\n");
  printf("%s\n", s2);
  return 0;
}
