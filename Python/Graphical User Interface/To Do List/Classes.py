import pickle
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font


class Functions:
    def __init__(self,master):
        master.title("To Do masterlication")
        icon = PhotoImage(file = "C:/Users/natal/Desktop/Projects/To Do List/tasks.png")
        master.iconphoto(False,icon)
        master.geometry("800x500")
        master.maxsize(1000,500)
        master.minsize(1000,500)

        #Define our font
        self.my_font = Font(
            family="ADMIRATION PAINS",
            size = 30,
            weight="bold")

        #create frame
        self.my_frame = Frame(master,width=1000,bg="black")

        self.my_frame.pack(pady=10,padx=10)
        #create listbox
        self.my_list = Listbox(self.my_frame,
        font = self.my_font,
        width=25,
        height=5,
        bg = "SystemButtonFace",
        bd = 0,
        fg="#464646",
        highlightthickness=0,
        selectbackground="#a6a6a6",
        activestyle="none")
        self.my_list.pack(side=LEFT,fil = BOTH,pady=20)


        #Create a scroll bar
        self.my_scrollbar = Scrollbar(self.my_frame,background="#000000")
        self.my_scrollbar.pack(side=RIGHT,fill=BOTH)
        #Add scroll bar into the mylist
        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        #Entry box
        self.my_entry  = Entry(master,font=("Helvetica",24))
        self.my_entry.pack(pady=20)

        self.button_frame = Frame(master)
        self.button_frame.pack(pady=20)
        self.my_menu=Menu(master)
        master.config(menu=self.my_menu)

        self.file_menu = Menu(self.my_menu,tearoff=False)
        self.my_menu.add_cascade(label = "File", menu = self.file_menu)

        self.file_menu.add_command(label="Save List", command=self.save_list)
        self.file_menu.add_command(label="Open List", command=self.open_list)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Clear List", command=self.delete_list)


        self.delete_button = Button(self.button_frame, text="Delete Item", command=self.delete_item,bg="#FF0000")
        self.add_button = Button(self.button_frame, text="Add Item", command=self.add_item,bg="#39FF14")
        self.cross_button = Button(self.button_frame, text="Cross Item", command=self.cross_item,bg = "#00FFFF")
        self.uncross_button = Button(self.button_frame, text="Uncross Item", command=self.uncross_item,bg="#E44D2E")
        self.delete_cross_button = Button(self.button_frame, text="Delete Crossed Items", command=self.delete_crossed,bg="#00FFFF")

        self.delete_button.grid(row = 0,column=0,padx = 20)
        self.add_button.grid(row = 0,column=1,padx = 20)
        self.cross_button.grid(row = 0,column=2,padx = 20)
        self.uncross_button.grid(row = 0,column=3,padx = 20)
        self.delete_cross_button.grid(row = 0,column=4,padx = 20)



    def save_list(self):
        file_name = filedialog.asksaveasfilename(
            initialdir=("C:/Users/natal/Desktop/Projects"),title="Save File",
            filetypes=(("Dat Files","*dat"),("All Files","*")))
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f"{file_name}.dat"
                #delete crossed items before saving
                count = 0
                while count<self.my_list.size():
                    if self.my_list.itemcget(count,"fg") == "#dedede":
                        self.my_list.delete(self.my_list.index(count))
                    else:
                        count+=1
                #grab everything from the list
                stuff = self.my_list.get(0,END)
                #open the file
                output_file = open(file_name,'wb')#write to binary
                #add stuff to the file
                pickle.dump(stuff,output_file)

    def open_list(self):
        file_name = filedialog.askopenfilename(
            initialdir=("C:/Users/natal/Desktop/Projects"),title="Open File",
            filetypes=(("Dat Files","*dat"),("All Files","*")))
        if file_name:
            #delete currently oepn list
            self.my_list.delete(0,END)
            #open the file
            input_file = open(file_name,'rb') # read binary

            #load the date from the file
            stuff = pickle.load(input_file)

            #outputstuff to the screen
            for item in stuff:
                self.my_list.insert(END,item)

    def delete_list(self):
        self.my_list.delete(0,END)

    def delete_item(self):
        self.my_list.delete(ANCHOR)
    def add_item(self):
        if self.my_entry.get()=="":
            messagebox.showinfo(title="Alert", message="The entry Box is empty")
        else:
            self.my_list.insert(END, self.my_entry.get())
            self.my_entry.delete(0,END)
    def cross_item(self):
        try:
        #Cross off item
            self.my_list.itemconfig(
                self.my_list.curselection(),
                fg="#dedede")
                    #Get rid of selection bar
            self.my_list.select_clear(0,END)
        except TclError:
            self.messagebox.showerror("Empty Selection","Must select an item in order to cross them")
    def uncross_item(self):
        try:
                #Cross off item
            self.my_list.itemconfig(
                self.my_list.curselection(),
                    fg="#464646")
                    #Get rid of selection bar
            self.my_list.select_clear(0,END)
        except TclError:
            self.messagebox.showerror("Empty Selection","Must select a cross item in order to uncross them")

    def delete_crossed(self):
        count = 0
        while count<self.my_list.size():
            if self.my_list.itemcget(count,"fg") == "#dedede":
                self.my_list.delete(self.my_list.index(count))
            else:
                count+=1
    
