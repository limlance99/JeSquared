#include <stdio.h>
// this is a comment, '//' must be followed by a white space(easy parsing) 

int summ0n ( int j3j3X, float j3j3Y ) { // INT function that accepts one integer and one float 
j3j3X = 5 ; 
int j3j3Y ; // duplicate 
return 5.5 ; // must be INT 
} 

int summ0n ( ){ // function already declared 
notARealFunctionm0n() ; // undeclared function 
return 0 ; 
} 
int main () { // main function 
int j3j3B ; 
float j3j3D ; 
j3j3B = 5.5 + 1 - 4.5 * 3 ; // invalid syntax, you can only 
// do operations of the same type 
j3j3B = j3j3C + 1 ; // undeclared variable in operation 

int j3j3D ; // var already been declared 
j3j3C = 4.5 ; // undeclared variable 
if (j3j3B > 1) { 
j3j3B = j3j3B / 0 ; // zero division error 
} else { 
j3j3C = j3j3B + j3j3B ; // undeclared function 
while (j3j3B != j3j3D){ 
j3j3B = j3j3B + 1 ; 
} 
} 
scanf("%d", &j3j3D) ; // INT i/o but float variable 
// scanf("%d", j3j3B) ; // syntax error - no ampersand for j3j3B 
printf("%f", j3j3B) ; // FLOAT i/o but int variable printf("\n");

summ0n (j3j3D, j3j3B) ; // incorrect parameters passed 
summ0n(j3j3B,j3j3D,j3j3B,j3j3D) ; // too many parameters 
return 0 ; 
} 
