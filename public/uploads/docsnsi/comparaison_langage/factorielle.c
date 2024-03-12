#include<stdio.h>
#include<stdlib.h>

int factorielle ( int n ) {
  if ( n == 0 || n == 1 ) {
    return 1;
  }
  else {
    int result = 1;
    int i = 0;
    while (i < n) {
      i = i + 1;
      result = result * i;
    }
    return result;
  }
}

int main(int argc, char *argv[] ) {
  int n = atoi(argv[1]);
  printf("%d", factorielle(n) );
} 
  
