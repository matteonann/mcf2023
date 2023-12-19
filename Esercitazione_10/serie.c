#include <stdio.h>
#include <math.h>


// Somma primi n numeri naturali
int fibonacci(int n){

  if(n == 1 || n ==2)
    return 1;
  else {
    double termn = 1;
    double termn1 = 1;
    double termn2 = 1;
    for( int i=3; i<=n; ++i) {
      termn2 = termn1;
      termn1 = termn;
      termn = termn1 + termn2;
    }
    return termn/termn1; 
  }
}