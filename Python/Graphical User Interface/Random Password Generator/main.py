from tkinter import *
import random
import string

app = Tk()
app.geometry("500x175")
app.minsize(500,175)
app.maxsize(500,175)
app.title("Password Generator")
app.welcome = Label(text = 'Welcome to Password Generator')
app.welcome.pack()
class window:
    def __init__(self,master):
        

        self.generate_Button = Button(app, text = "Generate Password",command = self.generate_password)
        self.generate_Button.pack()

        self.Show_pass = Entry(app)
        self.Show_pass.pack(padx=10,pady = 10)

    def generate_password(self):
        self.Show_pass.delete(0,END)
        characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        password = ''.join(random.choice(characters)for i in range(1,13))
        self.Show_pass.insert(0,password)
        
window_obj = window(app)

app.mainloop()
