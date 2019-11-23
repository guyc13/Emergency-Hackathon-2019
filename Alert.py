import tkinter as tk
from itertools import count
from PIL import Image, ImageTk
import datetime
import winsound


duration = 1000
freq = 1000
NORM_FONT = ("Helvetica", 26)
alerts = {"A": "Fire Alert", "B":"survivor Alert!"}

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def popupmsg(msg,sensor):
    root = tk.Tk()
    root.wm_title("ALERT!!!")
    lbl = ImageLabel(root)
    label = tk.Label(root, background='grey', anchor='s', text=str(datetime.datetime.now().ctime())+'\n'
                                      + msg, font=NORM_FONT, width=50, fg='orange')
    label.pack(side="top", fill="x", pady=100)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    lbl.pack()
    if sensor=='A':
        lbl.load('fire.gif')
    elif sensor=='B':
        lbl.load('help.gif')
    root.mainloop()

def alert_sound():
    winsound.Beep(freq, duration)