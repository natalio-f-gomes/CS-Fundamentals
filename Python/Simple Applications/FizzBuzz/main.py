import string
def fizzbuzz(num):
    
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num% 5 == 0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print("Not devisable for either of 3 or 5")

fizzbuzz(151)



