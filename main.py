# pip install pytube3
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as mb
import os

class Window:
    def __init__(self):
        self.w = 500
        self.h = 300
        self.title = "Youtube Video Downloader"

    def build(self):
        self.win = Tk()
        self.win.geometry(f"{self.w}x{self.h}")
        self.win.resizable(0, 0)
        self.win.title(self.title)

        self.createComponents()
        self.showVideos()
        self.win.mainloop()

    def createComponents(self):
        self.frame =  Frame(self.win)
        self.label = Label(self.frame, text="Enter URL", font="Helvetica 12").grid(row=0, column=0, padx=6)
        self.urlBox = Entry(self.frame, font="Helvetica 12", width=38)
        self.urlBox.grid(row=0, column=1, ipady=2)
        self.getBtn = Button(self.frame, text="Get", font="Cursive 10", command=self.get).grid(row=0, column=2, padx=10, ipadx=8)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, columnspan=12)

    def get(self):
        url = self.urlBox.get()
        if url is not None:
            video = YouTube(url)

            self.streams = video.streams.filter()
            resolutions = []
            types = ['mp4', 'webm']
            for stream in self.streams:
                resolutions.append(stream.resolution)

            self.frmDownload = Frame(self.win)

            self.typeVar = StringVar(self.frmDownload)
            self.typeVar.set(types[0])
            self.typeOpts = OptionMenu(self.frmDownload, self.typeVar, *types)
            self.typeOpts.grid(row=0, column=0, padx=0)

            self.resVar = StringVar(self.frmDownload)
            self.resVar.set(resolutions[0])
            self.resOpts = OptionMenu(self.frmDownload, self.resVar, *resolutions)
            self.resOpts.grid(row=0, column=1, padx=0)

            self.downloadBtn = Button(self.frmDownload, text="Download", command=self.download).grid(row=0, column=2, padx=0)
            self.frmDownload.grid(row=2, columnspan=12)

    def download(self):
        res = self.resVar.get()
        type = self.typeVar.get()
        for stream in self.streams:
            if res in str(stream) and type in str(stream):
                stream.download('./videos')
            else:
                break
        mb.showerror("Error", "Sorry No Resolution Available!")
        self.showVideos()

    def showVideos(self):
        try:
            os.scandir('./videos')
        except Exception as e:
            os.mkdir('./videos')
        files = os.scandir('./videos')
        self.frmVideos = Frame(self.win)
        Label(self.frmVideos, text="Downloaded Videos").grid(row=0, column=0)
        i = 1
        for file in files:
            if '.mp4' in file.name or '.webm' in file.name or '.mp3' in file.name:
                Label(self.frmVideos, text=file.name[:45]).grid(row=i, column=0 ,columnspan=12)
                i += 1

        files.close()
        self.frmVideos.grid(row=3, columnspan=12)


if __name__ == "__main__":
    win = Window()
    win.build()
