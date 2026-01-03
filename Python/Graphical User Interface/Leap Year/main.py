from tkinter import *
app = Tk()
app.title("Leal Year")
app.geometry("500x200")
app.minsize(500,200)
app.maxsize(500,200)
welcome = Label(app, text = "Welcome to Leap It\nEnter a year and we'll tell you if it's Leap year or not.")
welcome.pack()

class Window:
    def __init__(self,master):
        self.year = Entry(master)
        self.year.pack()

        self.Check = Button(master, text = "Check", command = self.Leap)
        self.Check.pack()

        self.info = Entry(master)
        self.info.pack()

    def Leap(self):
        #Check error missing
        self.info.delete('0',END)
        value =  int(self.year.get())
        if (value %4) ==0:
            if value %100==0:
                if value%400==0:
                    self.info.insert(INSERT,'Leap')
                else:
                    self.info.insert(INSERT,'Not Leap')
            else:
                self.info.insert(INSERT,'Leap')
        else:
            self.info.insert(INSERT,'Not Leap') 
            
        

window_obj = Window(app)

app.mainloop()
