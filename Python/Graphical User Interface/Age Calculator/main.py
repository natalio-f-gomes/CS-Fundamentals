from tkinter import *
from datetime import date

app = Tk()
app.title("Age Calculator")
app.geometry('370x300')
app.minsize(370,300)
app.maxsize(370,300)

class AgeCal:
    def __init__(self,tkinterwindow):
        self.welcome = Label(tkinterwindow, text = "Calculate your age",pady = 20,padx = 20)
        self.welcome.grid(row=0, column = 1,columnspan=2)

        self.year = Label(tkinterwindow,text = "Birth Year",padx = 20)
        self.year.grid(row = 1, column = 0)

        self.month = Label(tkinterwindow,text = "Birth Month")
        self.month.grid(row = 2, column = 0)

        self.day = Label(tkinterwindow,text = "Birth Day")
        self.day.grid(row = 3, column = 0)


        #Entries
        self.year_entry = Entry(tkinterwindow, )
        self.year_entry.grid(row = 1, column = 1)

        self.month_entry = Entry(tkinterwindow)
        self.month_entry.grid(row = 2, column = 1)

        self.day_entry = Entry(tkinterwindow)
        self.day_entry.grid(row = 3, column = 1)

        self.show = Text(tkinterwindow,width = 4, height=1, font = ('arial',40))
        self.show.grid(row = 5, column = 1, columnspan=2)

        self.Calculate = Button(app,text = "Calculate", command = self.calculate)
        self.Calculate.grid(row = 4, column = 1, columnspan=2)

    #Buttom
    def calculate(self):
        self.show.delete('1.0',END)
        today = date.today()
        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        day = int(self.day_entry.get())
        AGE  = today.year - year -((today.month,month)<( today.day,day))
        self.show.insert(INSERT,AGE)

    #definbe a function to check the error missing
        
test = AgeCal(app)
app.mainloop()
