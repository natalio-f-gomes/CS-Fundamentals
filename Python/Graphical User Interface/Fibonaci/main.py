from tkinter import *
from tkinter import messagebox
app = Tk()
app.title("Fibonnaci Calculator")
app.geometry('1100x500')
welcome = Label(app, text = 'Welome to Find out Fibonacci', padx = 30,pady = 30)
welcome.grid(row = 0, column = 1)

class Window:
    def __init__(self,master):
        self.check_lbl = Label(master, text = "Enter the numbers of terms you would like to display: ", padx = 10,pady = 5)
        self.check_lbl.grid(row = 1, column =0)

        self.check_entry = Entry(master,width = 20)
        self.check_entry.grid(row = 1, column = 1)


        self.num_frame = Frame(master)
        self.num_frame.grid(row = 1, column = 2)

        self.num_lst = Listbox(self.num_frame,
                font = 'arial',
                width = 30,
                height = 15,
                bg = 'SystemButtonFace',
                bd = 1,
                fg = '#464646',
                highlightthickness = 1,
                selectbackground='green',
                activestyle='none')
        self.num_lst.grid(row =1, column = 2,padx = 5,pady = 5)

        self.my_scrollbar = Scrollbar(self.num_frame)
        self.my_scrollbar.grid( row = 1, column = 3,sticky=N+S+E)

        self.num_lst.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command = self.num_lst.yview)

        check_button = Button(master, text = "Check", command = self.fibonacci, width = 20, padx = 0)
        check_button.grid(row = 2, column = 0,columnspan = 2, rowspan = 2)

    def fibonacci(self):
        self.num_lst.delete('0', END)
        nterms = int(self.check_entry.get())
        a,b = 0,1
        count = 0

        if nterms<=0:
            messagebox.showinfo("Find Out Fibonacci","Please Enter a number greater than 0")
        elif nterms ==1:
            self.num_lst.insert(INSERT,b)
        else:
            while count<nterms:
                self.num_lst.insert(END,a)
                print(a)
                nth = a +b
                a = b
                b = nth
                count+=1

window_obj = Window(app)
app.mainloop()

