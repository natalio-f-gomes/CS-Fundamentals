#include <stdio.h>
#include <math.h>
int check_prime_number(int num)
{
	
	int square_root = sqrt(num);
	for(int i=0;i<=square_root;i++)
		{
		if(num%i == 0){
		return 0;
		}
		}
	return 1;
}
int main()
{
    int num;
    printf("Enter a number to check if it is prime: ");
    scanf("%d", &num);
    if(check_prime_number(num))
    {
        printf("%d is a prime number\n", num);
    }
    else
    {
        printf("%d is not a prime number\n", num);
    }
    return 0;
}