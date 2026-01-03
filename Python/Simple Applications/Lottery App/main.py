import Lottery

w1, w2, w3, w4 = eval(input("Set Winning numbers: "))
d1, d2, d3, d4 = eval(input("Buy Ticket number: "))
set_nums = [w1, w2, w3, w4]
guessed_nums = [d1,d2,d3,d4]
obj = Lottery(set_nums, guessed_nums)
print(obj.set_prize())
