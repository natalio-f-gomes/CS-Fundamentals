from tkinter import *
import sqlite3
from getpass import getpass

app = Tk()
app.title("Password Saver")
app.geometry("1200x700")
app.minsize(1450, 500)
app.maxsize(1450,500)
app.configure(bg='#E60026')

# connect or create connection with database
conn = sqlite3.connect("PasswordSaver.db")
# create cursor
c = conn.cursor()

# Creating the table. It has to be only one time
'''
c.execute("""CREATE TABLE PasswordSaver(
    website text,
    e_username text,
    password text)
    """)

'''

# Create frame


def update():
    conn = sqlite3.connect("PasswordSaver.db")
    c = conn.cursor()
    ID = ID_NUMBER.get()
    sql = """UPDATE PasswordSaver SET
        website = ?,
        e_username = ?,
        password = ?
        WHERE oid = ?"""
    websinfo = (website_box_editor.get(), email_box_editor.get(), password_box_editor.get(), ID_NUMBER.get())
    c.execute(sql, websinfo)

    conn.commit()
    conn.close()
    editor.destroy()


def window_editor():
    global editor
    editor = Tk()
    editor.title("Information Update")
    editor.geometry("500x200")

    conn = sqlite3.connect("PasswordSaver.db")
    c = conn.cursor()
    ID = ID_NUMBER.get()
    c.execute("SELECT * FROM PasswordSaver WHERE oid = " + ID)
    records = c.fetchall()

    global website_box_editor
    global email_box_editor
    global password_box_editor

    # Labels for the new window
    info = Label(editor, text="Please Enter the Information that you want to change")
    info.grid(row=0, column=0, columnspan=2)

    website_label_editor = Label(editor, text="Website")
    website_label_editor.grid(row=1, column=0, pady=10, padx=50)

    email_label_editor = Label(editor, text="Email or Username")
    email_label_editor.grid(row=2, column=0, pady=10, padx=50)

    password_label_editor = Label(editor, text="Password")
    password_label_editor.grid(row=3, column=0, pady=10, padx=50)

    # Grids

    website_box_editor = Entry(editor, width=30)
    website_box_editor.grid(row=1, column=1, pady=2, padx=50)

    email_box_editor = Entry(editor, width=30)
    email_box_editor.grid(row=2, column=1, pady=2, padx=50)

    password_box_editor = Entry(editor, width=30)
    password_box_editor.grid(row=3, column=1, pady=2, padx=50)

    for i in records:
        website_box_editor.insert(0, i[0])
        email_box_editor.insert(0, i[1])
        password_box_editor.insert(0, i[2])

    update_bnt = Button(editor, text="Save Information", command=update)
    update_bnt.grid(row=4, column=0, columnspan=2)
    editor.mainloop()


def add_info():
    conn = sqlite3.connect("PasswordSaver.db")
    c = conn.cursor()
    # Insert information onto table
    c.execute("INSERT INTO PasswordSaver VALUES(:website, :email,:password)",
              {
                  'website': website_box.get(),
                  'email': email_box.get(),
                  'password': password_box.get()

              }

              )
    boxes = [website_box.get(), email_box.get(), password_box.get()]

    conn.commit()
    conn.close()

    website_box.delete(0, END)
    email_box.delete(0, END)
    password_box.delete(0, END)


# Create  quesry or a show information function

def show_info():
    conn = sqlite3.connect("PasswordSaver.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM PasswordSaver")
    informations = c.fetchall()

    my_frame = Frame(app)
    my_frame.grid(row=1, column=6, rowspan=5, columnspan=2, padx=5, pady=5 )
    global my_list
    my_list = Listbox(my_frame,
                      font='arial',
                      width=18,
                      height=5,
                      bg='SystemButtonFace',
                      bd=0,
                      fg='#464646',
                      highlightthickness=0,
                      selectbackground='green',
                      activestyle='none')

    # create scrollbar
    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.grid(row=1, column=7, sticky=N + S + E)

    my_list.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=my_list.yview)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6]
    for i in informations:
        my_list.insert(END, "Website: " +i[0])
    my_list.grid(row=1, column=7, padx=5, pady=5)
    conn.commit()
    conn.close()


# Window editor

# Create a delete funtion
def delete_record():
    conn = sqlite3.connect("PasswordSaver.db")
    c = conn.cursor()
    c.execute("DELETE FROM PasswordSaver WHERE oid = " + ID_NUMBER.get())

    conn.commit()
    conn.close()


# Labels
welcome = Label(app,
                text="Welcome to Password Saver \n Please provide the information about the latest website that you've sing up to", font=('arial', 20), padx=10, pady=10, bg='#E30022'
            )
welcome.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

website_label = Label(app, text="Website", bg='#E30022', fg='#0abab5')
website_label.grid(row=1, column=0, pady=10, padx=50)

email_label = Label(app, text="Email or Username", bg='#E30022', fg='#0abab5')
email_label.grid(row=2, column=0, pady=10, padx=50)

password_label = Label(app, text="Password", bg='#E30022', fg='#0abab5')
password_label.grid(row=3, column=0, pady=10, padx=50)

Iden_number = Label(app, text="ID Number", bg='#E30022', fg='#0abab5')
Iden_number.grid(row=2, column=2, columnspan=2)

# Grids

website_box = Entry(app, width=30)
website_box.grid(row=1, column=1, pady=2, padx=50)

email_box = Entry(app, width=30)
email_box.grid(row=2, column=1, pady=2, padx=50)


password_box = Entry(app,width=5)
password_box.configure(show = "*")
password_box.grid(row=3, column=1, pady=2, padx=50)

ID_NUMBER = Entry(app, width=5)
ID_NUMBER.grid(row=2, column=3, columnspan=2)

# Buttons3
# ADD Button
add_bnt = Button(app, text="Add information", bg='#E30022', fg='#000000', command=add_info)
add_bnt.grid(row=4, column=1)

# Show Button
show_btn = Button(app, text="Show Records", bg='#E30022', command=show_info, fg='#000000')
show_btn.grid(row=1, column=2, columnspan=2)

# Delte button
delete_bnt = Button(app, text='Delete Information',bg='#E30022', command=delete_record, fg='#000000')
delete_bnt.grid(row=5, column=2, columnspan=2)

# Update Button
save_bnt = Button(app, text="Update", bg='#E30022', command=window_editor, fg='#000000')
save_bnt.grid(row=4, column=2)



app.mainloop()
