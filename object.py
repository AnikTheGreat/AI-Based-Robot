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



# Object Game
def og(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cup.gif')

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: correct_og(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Table ", command=lambda: wrong_og(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og(ag):
    ag.destroy()

def next_btn_og(ag):
    og1(ag)

def correct_og(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_og(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: og(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()


# Object Game 1
def og1(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\le.gif')

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: wrong_og1(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Table ", command=lambda: correct_og1(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og1(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og1(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og1(ag):
    ag.destroy()

def next_btn_og1(ag):
    og2(ag)

def correct_og1(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_og1(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og1(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og1(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: og1(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of Object Game 1

# Object Game 2
def og2(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\chair.gif')

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: wrong_og2(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Chair ", command=lambda: correct_og2(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og2(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og2(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og2(ag):
    ag.destroy()

def next_btn_og2(ag):
    ag.destroy()

def correct_og2(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_og2(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og2(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og2(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: og2(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of Object Game 2


# End of Object Game

root = Tk()
og(root)
root.mainloop()