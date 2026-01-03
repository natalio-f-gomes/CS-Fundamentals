from tkinter import *
import math

def button_press(num):
    global equation_text
    equation_text = equation_text+str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Undefined")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

    
def clear():
    global equation_text
    equation_label.set("")
    equation_text =""

def square_root():
    global equation_text
    number = (eval(equation_text))
    equation_label.set(math.sqrt(number))

def power_of_2():
    global equation_text
    n = eval(equation_text)
    equation_label.set(n*n)

def percentage():
    global equation_text
    n = eval(equation_text)
    equation_label.set(n/100)
def check_prime():
    global equation_text
    try:
        n = eval(equation_text)
        sqrt = math.floor(math.sqrt(n))
        prime_num = "True"
        
        if n > 2:
            for i in range(2, sqrt + 1):
                if n % i == 0:
                    prime_num = "False"
        else:
            equation_label.set("False")
        equation_label.set(prime_num)
    except SyntaxError:
        equation_label.set("Invalid Input!")

def check_factors():
    global equation_text
    try:
        n = eval(equation_text)
        factors = ""
        for i in range(1,n+1):
            if n%i==0:
                factors+=str(f"{i} ")
        equation_label.set(factors)
    except SyntaxError:
        equation_label.set("Invalid Input!")
window = Tk()
window.title("Calculator App")
window.geometry("500x350")
window.minsize(500,350)
window.maxsize(500,350)

equation_text = ""
equation_label = StringVar()

label = Label(window,textvariable= equation_label, width=28, font=("arial",20), background="#FF0800")
label.pack()

frame = Frame(window)
frame.pack()

frame2 = Frame(window)
frame2.pack()

button_1 = Button(frame,text = 1,height=2,width=4,font=35,
            command=lambda:button_press(1))
button_1.grid(row = 0, column=0 )

button_2 = Button(frame,text = 2,height=2,width=4,font=35,
            command=lambda:button_press(2))
button_2.grid(row = 0, column=1 )

button_3 = Button(frame,text = 3,height=2,width=4,font=35,
            command=lambda:button_press(3))
button_3.grid(row = 0, column=2 )

button_4 = Button(frame,text = 4,height=2,width=4,font=35,
            command=lambda:button_press(4))
button_4.grid(row = 1, column=0 )

button_5 = Button(frame,text = 5,height=2,width=4,font=35,
            command=lambda:button_press(5))
button_5.grid(row = 1, column=1 )

button_6 = Button(frame,text = 6,height=2,width=4,font=35,
            command=lambda:button_press(6))
button_6.grid(row = 1, column=2 )

button_7 = Button(frame,text = 4,height=2,width=4,font=35,
            command=lambda:button_press(7))
button_7.grid(row = 2, column=0 )

button_8 = Button(frame,text = 8,height=2,width=4,font=35,
            command=lambda:button_press(8))
button_8.grid(row = 2, column=1 )

button_9 = Button(frame,text = 9,height=2,width=4,font=35,
            command=lambda:button_press(9))
button_9.grid(row = 2, column=2 )

button_0 = Button(frame,text = 0,height=2,width=4,font=35,
            command=lambda:button_press(0))
button_0.grid(row = 3, column=0 )

plus = Button(frame,text = "+",height=2,width=4,font=35,
            command=lambda:button_press("+"))
plus.grid(row = 0, column=3 )

minus = Button(frame,text = "-",height=2,width=4,font=35,
            command=lambda:button_press("-"))
minus.grid(row = 1, column=3 )

multiply = Button(frame,text = "*",height=2,width=4,font=35,
            command=lambda:button_press("*"))
multiply.grid(row = 2, column=3 )

multiply = Button(frame,text = "/",height=2,width=4,font=35,
            command=lambda:button_press("/"))
multiply.grid(row = 3, column=3 )

equal = Button(frame,text = "=",height=2,width=4,font=35,
            command=equals)
equal.grid(row = 3, column=2 )

decimal = Button(frame,text = ".",height=2,width=4,font=35,
            command=lambda:button_press("."))
decimal.grid(row = 3, column=1 )

sqrt = Button(frame,text = "√",height=2,width=4,font=25,
            command=square_root)
sqrt.grid(row = 0, column=4 )

pow = Button(frame,text = "Pow",height=2,width=4,font=35,
            command=power_of_2)
pow.grid(row = 1, column=4 )

percentage_btn = Button(frame,text = "%",height=2,width=4,font=35,
            command=percentage)
percentage_btn.grid(row = 2, column=4 )


clear_btn = Button(frame,text = "C",height=2,width=4,font=35,
            command=clear)
clear_btn.grid(row = 3, column=4 )

check_factors_btn = Button(frame2,text = "Check Factors",height=2,width=10,font=25,
            command=check_factors)
check_factors_btn.grid(row = 0, column=0 )

check_factors_btn = Button(frame2,text = "Check Prime",height=2,width=10,font=25,
            command=check_prime)
check_factors_btn.grid(row = 0, column=1 )


window.mainloop()
