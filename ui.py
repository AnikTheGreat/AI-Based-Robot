from tkinter import *
from tkinter import messagebox
import nltk
from PIL import ImageTk, Image
from itertools import count


# Object Game
def og(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cup.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: correct_og(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Table ", command=lambda: wrong_og(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og(ag):
    game_page(ag)

def next_btn_og(ag):
    og1(ag)

def correct_og(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_og(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: og(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()


# Object Game 1
def og1(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\table.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: wrong_og1(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Table ", command=lambda: correct_og1(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og1(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og1(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og1(ag):
    game_page(ag)

def next_btn_og1(ag):
    og2(ag)

def correct_og1(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_og1(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og1(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og1(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: og1(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of Object Game 1

# Object Game 2
def og2(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\chair.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Cup or", command=lambda: wrong_og2(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Chair ", command=lambda: correct_og2(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_og2(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_og2(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_og2(ag):
    game_page(ag)

def next_btn_og2(ag):
    game_page(ag)

def correct_og2(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_og2(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_og2(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_og2(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: og2(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of Object Game 2


# End of Object Game



# Alphabet Game
def alp_game(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\u.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It is?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) U or", command=lambda: correct_ag(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) A ", command=lambda: wrong_ag(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_ag(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_ag(root), height=3, width=26, bd=6).place(x=450, y=480)


def back_btn_ag(ag):
    game_page(ag)

def next_btn_ag(ag):
    game_page(ag)

def correct_ag(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_ag(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_ag(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_ag(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: alp_game(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of ALphabet Game

# Mood Game
def mg(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\happy.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It She?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Happy or", command=lambda: correct_mg(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Sad ", command=lambda: wrong_mg(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_mg(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_mg(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_mg(ag):
    game_page(ag)

def next_btn_mg(ag):
    mg1(ag)

def correct_mg(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_mg(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_mg(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_mg(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: mg(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()

# Mood Game 1
def mg1(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\sad.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Label(root, text="It She?", font=("Courier", 20)).place(x=660, y=100)
    Button(root, text="(a) Happy or", command=lambda: wrong_mg1(root), height=3, width=26, bd=6).place(x=660, y=140)
    Button(root, text="(b) Sad ", command=lambda: correct_mg1(root), height=3, width=26, bd=6).place(x=660, y=200)

    Button(root, text="Back", command=lambda: back_btn_mg1(root), height=3, width=26, bd=6).place(x=0, y=480)
    Button(root, text="Next", command=lambda: next_btn_mg1(root), height=3, width=26, bd=6).place(x=450, y=480)

def back_btn_mg1(ag):
    game_page(ag)

def next_btn_mg1(ag):
    game_page(ag)

def correct_mg1(ag):
    ag.destroy()
    root = Tk()
    root.title("Correct Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\tik.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Back", command=lambda: back_btn_mg1(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_mg1(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_mg1(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\cross.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Try Again", command=lambda: mg1(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End Mood Game 1
# End of Mood Game


def exit(r):
    r.destroy()
    global a
    a = 0

def game_page(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("1100x550")

    photo = PhotoImage(file=r"C:\Users\mdsaz\Desktop\Tkinter_Interface\Photos\base.gif")
    label = Label(image=photo)
    label.image = photo
    label.pack()

    Button(root, text="Alphabet Game", command=lambda: alp_game(root), height=3, width=26, bd=6).place(x=750, y=300)
    Button(root, text="Mood Game", command=lambda: mg(root), height=3, width=26, bd=6).place(x=750, y=200)
    Button(root, text="Object Game", command=lambda: og(root), height=3, width=26, bd=6).place(x=750, y=100)
    root.mainloop()


# GIPHY PLAY
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


a = 1
while a == 1 :
    root = Tk()
    root.title("Home Page")
    root.geometry("500x380")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\giphy.gif')

    Button(root, text="EXIT", command=lambda: exit(root), height=3, width=26, bd=6).place(x=10, y=300)
    Button(root, text="GAME PAGE", command=lambda: game_page(root), height=3, width=26, bd=6).place(x=290, y=300)
    root.mainloop()


