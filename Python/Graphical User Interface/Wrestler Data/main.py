from tkinter import *
import csv

app = Tk()
app.title("Wrestler data")
app.geometry("600x250")
app.maxsize(600,250)
app.minsize(600,250)
weclome = Label(app,  text = "Welcome to Wrestler data")
weclome.pack()

user_in = Entry()
user_in.pack()

def Search():

    def Wretler_data(data):
            total = int(data[1])+int(data[2])+int(data[3])
            wins = round(int(data[1])/int(total) * 100)
            losses = round(int(data[2])/int(total) * 100)
            draws = round(int(data[3])/int(total) * 100)
            print_win = f"Wins percentage: {wins}%"
            print_loss = f"Losses percentage {losses}%"
            print_draw = f"Draws percentage {draws}%"
            show.delete(1.0,END)
            show.insert(INSERT,(f"{print_win}\n{ print_loss}\n{print_draw}"))
    with open("Wrestler Data\Wrestler.csv",'r') as csv_file:
        CSV_READER = csv.reader(csv_file,delimiter = ',')
        found = False
        for row in CSV_READER:
            if user_in.get() == row[0]:
                Wretler_data(row)
                found = True
        if not found:
            show.insert(INSERT,(f"User Not found"))

search = Button(app,text = "Search User",command = Search)
search.pack()

show = Text(app,width=25, height=3, font=('arial', 20))
show.pack()
app.mainloop()

