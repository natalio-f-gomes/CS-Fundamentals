#include <stdio.h>

int factorial(int num){
    int total = 1;;
    for(int i = 1; i <=num;i++){
        total *= i;
    }
    return total;
}

int main(){
    int num;
    printf("Enter a number to get the factorial of it: ");
    scanf("%d", &num);

    int factorial_result = factorial(num);
    printf("The factorial of the num %d is %d",num,factorial_result);

    return 0;

}