#include <stdio.h>
// start this off nice 


int  main () { // MAIN 

int  j3j3x ; 
int  j3j3y ; 

scanf ("%d", &j3j3x) ; 
scanf ("%d", &j3j3y) ; 

while (j3j3x <= j3j3y) { 

if (j3j3x % 4 == 0) { 
printf ("%d", j3j3x) ; printf("\n");
} else { 

if (j3j3x % 100 == 0 && j3j3x % 400 == 0) { 
printf ("%d", j3j3x) ; printf("\n");
} 
} 


j3j3x = j3j3x + 1 ; 
} 

return  0 ; 
} 

