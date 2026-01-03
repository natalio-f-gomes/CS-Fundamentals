from asyncio import exceptions
from pytube import YouTube
from tkinter import *

from tkinter import messagebox
class Functions:
    def __init__(self,master):
        master.title("YouTube Downloader")
        master.geometry("850x600")
        icon = PhotoImage(file = "image.png")
        master.iconphoto(False,icon)
        master.minsize(650,600)
        master.maxsize(650,600)
        master.config(background="#ff4500")
        title = Label(master, text = "YouTube Downloader", width = 30, font=("Amasis MT Pro Medium", 20),bg="#ff4500")
        title.grid(row = 0, column = 1, columnspan = 3)


        self.title = Label(master, text = "YouTube Downloader", width = 30, font=("Amasis MT Pro Medium", 20),bg="#ff4500")
        self.title.grid(row = 0, column = 1, columnspan = 3)

        self.description_lbl = Label(master, text = "Please enter the url below and choose the quality of de video you would like to download! ",font=("Amasis MT Pro Medium",10),bg="#ff4500" ,width = 80,height=3)
        self.description_lbl.grid(row = 1, column = 1, columnspan = 3)

        self.url = Entry(master, width = 40)
        self.url.grid(row = 2, column = 1, columnspan = 3, padx = 10, pady = 10)

        self.search = Button(master, text = "Search", width = 15, command = self.vid_search,bg="#ff4500")
        self.search.grid(row = 2, column = 3, columnspan = 2, padx = 20, pady = 10)

        self.video_title_lbl = Label(text = "Video Title:",bg="#ff4500")
        self.video_title_lbl.grid(row =3, column =2, columnspan = 2, padx = 10, pady = 10)

        self.video_title = Entry(master, width = 70,bg="#ff4500")
        self.video_title.grid(row = 4, column = 2, columnspan = 2, padx = 10, pady = 10)

        self.video_author_lbl = Label(text = "Author:",bg="#ff4500")
        self.video_author_lbl.grid(row =3, column =1, columnspan = 1, padx = 10, pady = 10)

        self.video_author = Entry(master, width = 20,bg="#ff4500")
        self.video_author.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 10)

        self.views_lbl = Label(text = "Views:",bg="#ff4500")
        self.views_lbl.grid(row =5, column =1, columnspan = 1, padx = 10, pady = 10)

        self.views_entry = Entry(master, width = 15,bg="#ff4500")
        self.views_entry.grid(row = 6, column = 1, columnspan = 1, padx = 10, pady = 10)

        self.lower_quality_btn = Button(text = "Download Lower Quality",bg="#ff4500", command = self.get_audio_only )
        
        self.lower_quality_btn.grid(row =5, column =2, columnspan = 2, padx = 10, pady = 10)

        self.higher_quality_btn = Button(text = " Download Higher Quality",bg="#ff4500",command = self.get_higher_quality)
        self.higher_quality_btn.grid(row =6, column =2, columnspan = 2, padx = 10, pady = 10)

        self.higher_quality_btn = Button(text = " Download MP3",bg="#ff4500",command = self.get_audio_only)
        self.higher_quality_btn.grid(row =7, column =2, columnspan = 2, padx = 10, pady = 10)

        self.disc_lbl = Label(master, text = "Description",bg="#ff4500")
        self.disc_lbl.grid(row =8, column = 1, columnspan = 3, padx = 10, pady = 10)

        self.disc_ = Text(master,bg="#ff4500", width= 75, height=10)
        self.disc_.grid(row =9, column = 1, columnspan = 3, padx = 10, pady = 10)
        

    def vid_search(self):
    
        self.video_title.delete(0, END)
        self.views_entry.delete(0,END)

        self.vid_url = self.url.get()
        self.video = YouTube(self.vid_url)

        self.vid_title = self.video.title
        self.vid_views = self.video.views
        self.author = self.video.author
        self.desciption = self.video.description

        self.video_title.insert(INSERT, self.vid_title)
        self.views_entry.insert(INSERT, self.vid_views)
        self.video_author.insert(INSERT,self.author)
        self.disc.insert(INSERT, self.desciption)
         
    def get_lower_quality(self):
        self.master.update()
        vid_url = self.url.get()
        video = YouTube(vid_url)
        video = video.streams.get_lowest_resolution()
        #self.pb.start()
        video.download("C:/Users/natal/Desktop\Projects/Graphical User Interface/Youtube Downloader/MP4 LOWER QUALITY")
        messagebox.showinfo('Download Info', "Download Completed")

    def get_higher_quality(self):
        vid_url = self.url.get()
        video = YouTube(vid_url)
        video = video.streams.get_highest_resolution()
        video.download("C:/Users/natal/Desktop\Projects/Graphical User Interface/Youtube Downloader/MP4 HIGH QUALITY")
        messagebox.showinfo('Download Info',"Download Completed")
    def get_audio_only(self):
        vid_url = self.url.get()
        video = YouTube(vid_url)
        mp3 = video.streams.filter(only_audio=True).first()
        mp3.download("C:/Users/natal/Desktop/Projects/Graphical User Interface/Youtube Downloader/Audio")
        messagebox.showinfo('Download Info',"MP3 Download Completed")
