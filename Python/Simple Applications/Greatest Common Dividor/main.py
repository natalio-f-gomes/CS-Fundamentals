"""
        Euclidean Algorithm: get the greatest common divisor( GCD)(n1,n2)
        input: n1 and n2 are integers

"""


class GCD:

    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
        print(f'The greatest common divisor between {n1} and {n2} is:', end=" ")
        # If the user inputs zero as the second number, the program won't work
        while n2 != 0:
            # Create a temporary variable and assign it to first number because we later will use it
            self.t = n1
            # Same thing for n2
            n1 = n2
            # N2 is calculates the remainder of t on n1
            n2 = self.t % n1

        print(n1)


num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter a number: "))
obj = GCD
obj(num1, num2)
