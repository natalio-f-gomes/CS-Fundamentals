
from ast import main


def buying_house():
    anual_salary = float(input("Enter your anual salary? "))
    monthly_salary = anual_salary /12
    weekly_salary = anual_salary/52
    print(f"Your Weekly salary is about {weekly_salary}")

    house_cost = float(input("What is the price of the house that you are looking for? "))
    portion_down_payment = house_cost * 0.25 + 20000
    print(f"The down payment for the house is about {portion_down_payment} including closing cost")


    money_saved_weekely = float(input("How much money do you save weekly: "))
    portion_saved = float(input("Money Saved: "))
    weeks_until_down_payment = portion_down_payment-portion_saved
    yearly_saved = money_saved_weekely * 52
    print(str(round(weeks_until_down_payment/yearly_saved)) + " Years to buy you dream home")

if __name__ == "__main__":
    buying_house()
