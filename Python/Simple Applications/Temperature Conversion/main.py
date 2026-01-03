"""
    -Program purpose: Implement Celsius to Fahrenheit conversion
    -Date: 2020/09/15
    -Author: Enping Li
"""
import math
import math as m

# c to f
# the freezing point temperature in Celsius is 0, in fathering is 32
# the boiling point temperature in Celsius is 100, in faint is 212
def convert_to_Farheint():
    c = eval(input("Enter Celsius degree: "))
    f = 9 / 5 * c + 32  # Formula
    print(f"The Fahrenheit degree is {f}")


def convert_to_Celcius():
    f = eval(input("Enter Celsius temperature: "))
    c = (f - 32) * 5 / 9  # Formula
    print(c)


def body_mass_index():
    w = eval(input("What is your weight?\nPlease enter the unit in Kg \nA: "))
    h = eval(input("What is your height? \nPlease enter the unit in meters\nA: "))
    BMI = w / h ** 2
    print(f"Body mass Index of : {BMI}")
    if 18.5 > BMI > 24.9:
        print("Not Ideal for health")
    else:
        print("You are in an ideal shape")


if __name__ == "__main__":
    body_mass_index()
    # It is the same as what number itself 3 times equal 8

