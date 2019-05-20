#include <stdio.h>
int fibm0n( int j3j3x) { 
float j3j3c ; 
if (j3j3x == 0) { 
return 0 ; 
} 
if (j3j3x == 1) { 
return 1 ; 
} 

int j3j3a ; 
int j3j3b ; 
j3j3a = j3j3x - 1 ; 
j3j3b = j3j3x - 2 ; 
return fibm0n(j3j3a) + fibm0n(j3j3b) ; 
} 

int main () { 
int j3j3a ; 
int j3j3b ; 
int j3j3temp ; 

scanf("%d", &j3j3a) ; 
j3j3b = 1 ; 

while (j3j3b <= j3j3a) { 
j3j3temp = fibm0n(j3j3b) ; 
printf("%d", j3j3temp) ; printf("\n");
j3j3b = j3j3b + 1 ; 
} 

return 0 ; 
} 
