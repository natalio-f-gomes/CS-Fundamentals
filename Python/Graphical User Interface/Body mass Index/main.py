
from tkinter import *
app = Tk()
app.title("BMI Calculator")
app.geometry("700x500")
welcome = Label(app,text = "Welcome to body mass index Calculator",pady = 20, padx = 20)
welcome.grid(row = 0, column = 0, columnspan = 2)

class BMI():
    def __init__(self,window_tk):
        self.w = Label(window_tk, text = "Weitgh in Kilograms",pady = 20, padx = 20)
        self.w.grid(row = 1, column = 0)

        self.h = Label(window_tk, text = "Height in meters",pady = 20, padx = 20)
        self.h.grid(row = 2, column = 0)

        #ENTRIES
        self.w_entry = Entry(window_tk)
        self.w_entry.grid(row = 1, column = 2)

        self.h_entry = Entry(window_tk)
        self.h_entry.grid(row = 2, column = 2)


        self.calculate_button = Button(window_tk, text = "Calculate BMI", command = self.calculate_bmi)
        self.calculate_button.grid(row = 3, column = 1, columnspan = 2)

        self.show_result = Entry(window_tk,width = 30)
        self.show_result.grid(row = 4, column =1, columnspan = 2)

    def calculate_bmi(self):
        self.show_result.delete(0,END)
        heitgh = float(self.h_entry.get())
        weight = float(self.w_entry.get())
        bmi = weight/heitgh**2
        if bmi < 18.5:
            self.show_result.insert(INSERT,"UNDERWEIGHT")
        elif bmi >18.5 and bmi < 24.9:
            self.show_result.insert(INSERT,"IDEAL SHAPE")
        else:
            self.show_result.insert(INSERT,"OVERWEIGHT")


        


obj = BMI(app)
app.mainloop()
