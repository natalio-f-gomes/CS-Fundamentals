#include <stdio.h>

float celsius_to_fahrenheit(float temperature){
	float formula = (temperature*9/5)+32;
	return formula;

}

float fahrenheit_to_celsius(float temperature){
	float formula = (temperature -32)* 5/9;
	return formula;
}
int main(){
	
	int choice;
	do
	{
		printf("Welcome to Temperature Converter:\n ");
        printf("1 - Convert Celsius to fahrenheit\n");
        printf("2 - Convert fahrenheit to celsius\n ");
        printf("3 - EXIT\n");
        printf("Answer: ");

		scanf("%d", &choice);
		if (choice == 1)
		{
			float temperature;
			printf("Please enter the temperature in celsius:\nA: ");
			scanf("%f", &temperature);

			float fahrenheit = celsius_to_fahrenheit(temperature);
			printf("The temperature %f in celsius is %f in fahrenheit.\n",temperature , fahrenheit);
        }
		else if (choice==2)
		{
			float temperature;
			printf("Please enter the temperature in fahrenheit:\nA: ");
			scanf("%f", &temperature);

			float celsius =fahrenheit_to_celsius(temperature);
			printf("The temperature %f in fahrenheit is %f in celsius.\n",temperature , celsius);	
		}
		else if (choice!= 3)
		{
			
            printf("Invalid choice. Please try again.\n");
		}

		}while(choice != 3);
		return 0;

return 0;
	}	
	


