#include <stdio.h> 

int maksimal(int a, int b){ 
// Lengkapi Function ini
int max = a;
if (b > max){
    max = b;
}
return max;
} 

int minimal(int a, int b){ 
// Lengkapi Function ini 
int min = a;
if (b < min){
    min = b;
}
return min;
} 

int main(){ 
int batas = 0; 
int maks = -100000; 
int minim = 100000; 
int bilangan; 
scanf("%d", &bilangan); 
while(batas < bilangan){ 
int nilai; 
scanf("%d", &nilai); 
maks = maksimal(maks, nilai); 
minim = minimal(minim, nilai); 
batas++; 
} 
printf("%d %d",maks,minim); 
return 0;
}