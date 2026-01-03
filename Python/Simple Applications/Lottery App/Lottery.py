"""
    Comp 151 – Computer Science I (Fall 2021)
    Homework 02
    (20 points)

    Due Date: Friday, Oct 08

    Problem
    Write a program to simulate the lottery game. The program should firstly prompt for four single-digit winning
    numbers and then prompt for four single-digit lottery numbers. Each digit in the number is in the range between 0~9.
    The program should determine which prize the user wins according to the following rule:
    • The user wins the first prize if all of the input numbers and the lottery numbers match in exact order.
    • The user wins the second prize if any three of the input numbers and the lottery numbers match in exact order.
    • The user wins the third prize if any two of the input numbers and the lottery numbers match in exact order.
    • The user wins the fourth prize if any one of the input numbers and the lottery numbers matches in exact order.

"""
class Lottery:

    def __init__(self, nums: list, guesses: list):
        self.nums = nums
        self.guesses = guesses

        self.score = 0
        for i,j in zip(nums,guesses):
            if (i==j):
                self.score+=1
    def set_prize(self):
        if self.score == 4:
            return "You win the first prize"
        if self.score == 3:
            return "You win the second prize"
        if self.score == 2:
            return "You win the third prize"
        if self.score == 1:
            return "You win the fourth prize"
        if self.score == 0:
            return "Best luck next time"









