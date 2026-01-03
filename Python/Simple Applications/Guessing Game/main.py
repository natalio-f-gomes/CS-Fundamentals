from random import randint

my_number = int(input("Enter your number: "))
Number = randint(1,100)
guess = 0



while True:
    PC = input("I guess the number " + str(Number)+ " ,was that correct? \n")
    if PC == "NO" and Number != my_number:
        guess +=1
        answer = input("HIGHER OR LOWER? ").upper()
        if answer == "LOWER":
            Number = randint(1, Number)
            
        elif answer == "HIGHER":
            Number = randint(Number, 100)
    elif PC == "YES":
        print("I guessed " + str(Number) + " in " + str(guess) + " guesses")
        break
    else:
        print("YES or NO")
else:
    pass
from mimetypes import guess_extension
import random

def GuessGame():
  guesses = 0
  
  pc = random.randint(1,20)
  
  while True:
    guesses+=1
    user = int(input("Enter a number between 0 and 20: "))
    if user == pc:
      print(f"You guessed the correct number in {guesses} attempts")
      break
    elif user> pc:
      print("Too high ")
      
    else:
      print("Too low")

    print(pc)
  
GuessGame()
