import datetime
from threading import Thread
from tkinter import*
from  time import *
from tkinter import messagebox
import time
import winsound

def update():
    time_string = strftime("%I : %M : %S %p")
    time_label.config(text=time_string)
    time_label.after(1000,update)# or window.after because window alos has after function

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

def countdown():
    x = int(Entry_box.get())
    for i in range(int(x),0,-1):
        seconds =int(x%60)
        minutes = int(x/60) % 60
        hours = int(x/3600)
        time.sleep(1)
        x-=1
        display_timelabel.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        if (x == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            display_timelabel.config(text=f"00: 00: 00")
        window.update()

def start():
    global stop
    stop = False
    
    x = 0
    while not stop:
        seconds =int(x%60)
        minutes = int(x/60) % 60
        hours = int(x/3600)
        x+=1
        time.sleep(1)
        stopwatch_label_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        window.update()
    
        
def stopfunc():
    global stop
    stopwatch_label_display.config(text=f"00: 00: 00")
    stop = True

# Use Threading

def alarm():
    # Infinite Loop
    while True:
        window.update()
        # Set Alarm
        set_alarm = f"{hour_Entry.get():02}:{minutes_Entry.get():02}:00"


        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(set_alarm, current_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Time's Up")
window = Tk()
window.title("Digital Clock")
window.geometry("700x400")
window.configure(bg="#00FFFF")

date_label = Label(window,width = 20,height=2,bg = "#00FFFF")
date_label.grid(column=1, row=0)

day_label = Label(window,width = 10,height=2,bg = "#00FFFF")
day_label.grid(column=1, row=2)

time_label = Label(window,width = 10,height=2,bg = "#00FFFF")
time_label.grid(column=1, row=3)


countdown_label_intro = Label(window,text="Countdown",width = 10,height=2,bg = "#00FFFF")
countdown_label_intro.grid(column=0, row=4)

countdown_label = Label(window,text="Please enter the time in seconds",width = 35,height=2,bg = "#00FFFF")
countdown_label.grid(column=0, row=5)


Entry_box = Entry(window, width=20)
Entry_box.grid(column=0, row=6,pady=10)

display_timelabel = Label(window,width=15,bg = "#e5e4e2")
display_timelabel.grid(column=0, row=8,pady=10)

countdown_btn = Button(window, text="Countdown",width=10,command=countdown)
countdown_btn.grid(column=0, row=7)

#-------------------
stopwatch_label_intro = Label(window,text="Stopwatch",width = 10,height=2,bg = "#00FFFF")
stopwatch_label_intro.grid(column=1, row=4)

stopwtach_btn_start = Button(window, text="Start",width=10,command=start)
stopwtach_btn_start.grid(column=1, row=5)

stopwatch_label_display = Label(window,width = 20,height=2,bg = "#00FFFF")
stopwatch_label_display.grid(column=1, row=6)


stopwtach_btn_stop = Button(window, text="Stop",width=10,command=stopfunc)
stopwtach_btn_stop.grid(column=1, row=7)

#-------
Alarm_label_intro = Label(window,text="Alarm",width = 20,height=2,bg = "#00FFFF")
Alarm_label_intro.grid(column=2, row=4, columnspan=2)

hour_label =  Label(window,text="Hour",width = 5,height=2,bg = "#00FFFF")
hour_label.grid(column = 2, row = 5)

minues_label =  Label(window,text="Minutes",width = 5,height=2,bg = "#00FFFF")
minues_label.grid(column = 3, row = 5)

hour_Entry =  Entry(window,width = 5,bg = "#00FFFF")
hour_Entry.grid(column = 2, row = 6)

minutes_Entry =  Entry(window,width = 5,bg = "#00FFFF")
minutes_Entry.grid(column = 3, row = 6)

set_alarm_btn = Button(window, text="Set Alarm",width=10,command=alarm)
set_alarm_btn.grid(column=2, row=7, columnspan=2)




update()

window.mainloop()
