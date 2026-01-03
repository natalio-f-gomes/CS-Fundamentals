#include <stdio.h>

void  greeting(char name[])
{
printf("Hello %s\n", name);
}

int sum(int num)
{
int i;
int count = 0;
for (i = 1;i<= num; i++){
 count = count + i;
}
return count;
}

int main(int agrc, char* argv[]){
//greeting("Natalio");
//sum of all natural number
int n;
printf("Enter a integer to calculate the its sum: \n");
scanf("%d",&n);
if (n<0){
	printf("Enter a positive integer to calculate the its sum: \n");
	scanf("%d",&n);
}
int ans = sum(n);
printf("The sum of natural numbers up to %d is %d\n",n,ans);
return 0;
}
