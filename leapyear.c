#include <stdio.h>
// start this off nice 


int main () { 

// declaring two variables: j3j3x and j3j3y 
int j3j3x ; 
int j3j3y ; 

// getting input and storing it in the two variables 
scanf ("%d", &j3j3x) ; 
scanf ("%d", &j3j3y) ; 

// while loop that iterates over every number from j3j3x to j3j3y 
while (j3j3x <= j3j3y) { 
// if divisible by 4, or 
if (j3j3x % 4 == 0) { 
if (j3j3x % 100 != 0) { 
printf ("%d", j3j3x) ; printf("\n");
} 
} else { 

// if divisible by 100 and 400, print the number 
if (j3j3x % 100 == 0 && j3j3x % 400 == 0) { 
printf ("%d", j3j3x) ; printf("\n");
} 
} 

// iterate by 1 
j3j3x = j3j3x + 1 ; 
} 

return 0 ; 
} 

