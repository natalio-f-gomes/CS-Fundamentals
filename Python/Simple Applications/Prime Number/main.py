"""
        Date: 10/18/2021
        Author: Natalio Gomes
        Problem:
        A positive whole number n>2 is prime if no number between 2 and square root of n evenly divides n.
        Write a program that accepts a value of n as input and determines if the value is prime.
        If n is not prime, your program should quit as soon as it finds a value that evenly divides n.

        The following are examples of running the program:
        Enter a number: 9
        The number 9 is not a prime number.
"""

# Create a function that determines a prime number,
# and it takes a parameter that is the number that we are going to work with.
import math

class Prime_Number:
    def __init__(self, n: int):
        self.n = n
        self.sqrt = math.floor(math.sqrt(self.n))
        self.prime_num = False

    def check_num(self):
        if n > 2:
            for i in range(2, self.sqrt + 1):
                if self.n % i == 0:
                    self.prime_num = True
            if self.prime_num:
                return f"The number {self.n} is not a prime number "
            else:
                return f"The number {self.n} is a prime number "
        return "The number has to be greater than 2"



# Get input from the user
n = eval(input("Enter a number: "))
# If we are outputting a code from this file "hw03.py", so this file is the main script.
if __name__ == "__main__":
    # call the function and pass n as num parameter
        obj = Prime_Number(n)
        obj.check_num()


