from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from turtle import title
from unicodedata import name
root = Tk()
root.title("Hello")
root.geometry("1000x800")
icon = PhotoImage(file = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fexpenses_5501384&psig=AOvVaw07tLdNtxBs7FMrYuxTV3ei&ust=1667250298861000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJiX8b_tiPsCFQAAAAAdAAAAABAE")
root.iconphoto(False,icon)

class window:
    def __init__(self,master):
        #adding frame into the main window
        myFrame = Frame(master, width = 700)
        myFrame.pack()

        self.name = Label(myFrame, text = "Name", width = 15, bg="cyan",height=2, font = ("arial",14))
        self.name.grid(row = 0, column = 0, padx= 40, pady=10)

        self.date = Label(myFrame, text = "Date", width = 15, bg="cyan",height=2, font = ("arial",14))
        self.date.grid(row = 1, column = 0, padx= 40, pady=10)

        self.description = Label(myFrame, text = "Description", width = 15, bg="cyan",height=2, font = ("arial",14))
        self.description.grid(row = 2, column = 0, padx= 40, pady=10)

        self.exepense = Label(myFrame, text = "Expense", width = 15, bg="cyan",height=2, font = ("arial",14))
        self.exepense.grid(row = 3, column = 0, padx= 40, pady=10)

        #______________entry boxes_____________________
        self.name_entry = Entry(myFrame,  width = 15, bg="cyan", font = ("arial",25))
        self.name_entry.grid(row = 0, column = 1, padx= 10, pady=10)

        self.date_entry = Entry(myFrame,  width = 15, bg="cyan",font = ("arial",25))
        self.date_entry.grid(row = 1, column = 1, padx= 10, pady=10)

        self.description_entry = Entry(myFrame,  width = 15, bg="cyan", font = ("arial",25))
        self.description_entry.grid(row = 2, column = 1, padx= 10, pady=10)

        self.exepense_entry = Entry(myFrame, text = "Expense", width = 15, bg="cyan", font = ("arial",25))
        self.exepense_entry.grid(row = 3, column = 1, padx= 10, pady=10)       

        self.submitButton = Button(myFrame, text = "Submit", command=self.add_details, width = 20, bg="cyan", font = ("arial",13))
        self.submitButton.grid(row = 4, column = 0, padx= 10, pady=10)

        self.deleteButton = Button(myFrame, text = "Delete", command=self.delete, width = 20, bg="cyan", font = ("arial",13))
        self.deleteButton.grid(row = 4, column = 1, padx= 20, pady=10)


        self.bottomFrame = Frame(master, width = 700)
        self.bottomFrame.pack()

        self.my_scrollbar = Scrollbar(self.bottomFrame,background="#000000")
        self.my_scrollbar.pack(side=RIGHT,fill=BOTH)
        #Add scroll bar into the mylist
        

        self.my_font = Font(
            family="ADMIRATION PAINS",
            size = 20,
            weight="bold")

        self.my_list = Listbox(self.bottomFrame,
            font = self.my_font,
            width=50,
            height=10,
            bg = "#FF6700",
            bd = 0,
            fg="#f8f8ff",
            highlightthickness=0,
            selectbackground="#a6a6a6",
            activestyle="none")
        self.my_list.pack()

        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        self.viewdetailsbtn = Button(self.bottomFrame, text = "View Detais", command=self.show_details, width = 20, bg="cyan", font = ("arial",13))
        self.viewdetailsbtn.pack(pady = 10)

    def add_details(self):
        if self.name_entry.get() =="" or self.date_entry.get() == "" or self.description_entry.get() =="" or  self.exepense_entry.get() == "":
            messagebox.showinfo("Alert","One of the container is empty")
            
        else:
            self.my_list.insert(END, f"{self.name_entry.get()} - {self.date_entry.get()} - {self.description_entry.get()}-{self.exepense_entry.get()}")
            self.name_entry.delete(0,END)
            self.date_entry.delete(0,END)
            self.description_entry.delete(0,END)
            self.exepense_entry.delete(0,END)
    def delete(self):
        if self.my_list.get(ANCHOR):
            self.my_list.delete(ANCHOR)
        else:
            messagebox.showinfo("Alert","Must select something in order to delete it")
    
    def show_details(self):
        if self.my_list.get(ANCHOR):
            self.n_window = Tk()
            self.n_window.title("Details")
            self.n_window.geometry("830x400")
            self.n_window.maxsize(830,400)
            self.n_window.minsize(830,400)
            details = self.my_list.get(ANCHOR).split("-")
            name = details[0]
            date = details[1]
            description = details[2]
            amount = details[3]

            self.name = Label(self.n_window, text = "Name of the Merchendiser", width = 30, bg="cyan",height=2, font = ("arial",14))
            self.name.grid(row = 0, column = 0, padx= 40, pady=10)

            self.date = Label(self.n_window, text = "Date of the shop", width = 30, bg="cyan",height=2, font = ("arial",14))
            self.date.grid(row = 1, column = 0, padx= 40, pady=10)

            self.description = Label(self.n_window, text = "Description of services/product", width = 30, bg="cyan",height=2, font = ("arial",14))
            self.description.grid(row = 2, column = 0, padx= 40, pady=10)

            self.exepense = Label(self.n_window, text = "Expense", width = 30, bg="cyan",height=2, font = ("arial",14))
            self.exepense.grid(row = 3, column = 0, padx= 40, pady=10)
            #____________________________________
            
            self.name_info = Label(self.n_window, text = name, width = 30, bg="cyan",height=2, font = ("arial",14))
            self.name_info.grid(row = 0, column = 1, padx= 40, pady=10)

            self.date_info = Label(self.n_window, text = date, width = 30, bg="cyan",height=2, font = ("arial",14))
            self.date_info.grid(row = 1, column = 1, padx= 40, pady=10)

            self.description_info = Label(self.n_window, text = description, width = 30, bg="cyan",height=2, font = ("arial",14))
            self.description_info.grid(row = 2, column = 1, padx= 40, pady=10)

            self.exepense_info = Label(self.n_window, text = f"${amount}", width = 30, bg="cyan",height=2, font = ("arial",14))
            self.exepense_info.grid(row = 3, column = 1, padx= 40, pady=10)

            self.closebtn = Button(self.n_window,text = "Terminate Window", width = 30, bg="red",height=2, font = ("arial",10), command=self.n_window.destroy)
            self.closebtn.grid(row = 4, column = 0, columnspan=2)

            self.n_window.mainloop()
        else:
            messagebox.showinfo("Alert","Must select something in order to view the details")
    
e = window(root)
root.mainloop()
