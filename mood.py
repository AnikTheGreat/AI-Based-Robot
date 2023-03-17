from tkinter import *
from PIL import ImageTk, Image
from itertools import count

class ImageLabel(Label):
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
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def mg(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\happy.gif')

    Label(root, text="It She?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Happy or", command=lambda: correct_mg(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Sad ", command=lambda: wrong_mg(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_mg(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_mg(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_mg(ag):
    ag.desrtroy()

def next_btn_mg(ag):
    mg1(ag)

def correct_mg(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_mg(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_mg(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_mg(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: mg(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()

# Mood Game 1
def mg1(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\sad.gif')

    Label(root, text="It She?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Happy or", command=lambda: wrong_mg1(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Sad ", command=lambda: correct_mg1(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_mg1(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_mg1(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_mg1(ag):
    ag.destroy()

def next_btn_mg1(ag):
    ag.destroy()

def correct_mg1(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_mg1(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_mg1(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_mg1(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: mg1(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End Mood Game 1
# End of Mood Game

root = Tk()
mg(root)
root.mainloop()