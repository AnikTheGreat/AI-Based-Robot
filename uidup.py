from tkinter import *
from PIL import ImageTk, Image
from itertools import count
import vlc
import time


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
    game_page(ag)

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
    game_page(ag)

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
    game_page(ag)

def next_btn_og2(ag):
    game_page(ag)

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



# Alphabet Game
def alp_game(r):
    r.destroy()
    root = Tk()
    root.title("Object Detect")
    root.geometry("900x545")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\capu.gif')

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

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ik.gif')

    Button(root, text="Back", command=lambda: back_btn_ag(root), height=3, width=26, bd=6).place(x=0, y=0)
    Button(root, text="Next", command=lambda: next_btn_ag(root), height=3, width=26, bd=6).place(x=440, y=0)
    root.mainloop()

def wrong_ag(ag):
    ag.destroy()
    root = Tk()
    root.title("Wrong Answer")
    root.geometry("640x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\cross.gif')

    Button(root, text="Try Again", command=lambda: alp_game(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()
# End of ALphabet Game

# Mood Game
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
    game_page(ag)

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
    game_page(ag)

def next_btn_mg1(ag):
    game_page(ag)

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


def exit(r):
    r.destroy()
    global a
    a = 0

def game_page(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("1100x550")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\game1.gif')

    Button(root, text="Alphabet Game", command=lambda: alp_game(root), height=3, width=26, bd=6).place(x=750, y=300)
    Button(root, text="Mood Game", command=lambda: mg(root), height=3, width=26, bd=6).place(x=750, y=200)
    Button(root, text="Object Game", command=lambda: og(root), height=3, width=26, bd=6).place(x=750, y=100)
    Button(root, text="Back", command=lambda: entertainment(root), height=3, width=26, bd=6).place(x=0, y=0)
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


def entertainment(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("1100x550")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\hi1.gif')

    Button(root, text="GAMES", command=lambda: game_page(root), height=3, width=26, bd=6).place(x=750, y=300)
    Button(root, text="RHYMES", command=lambda: play_rhymes(root), height=3, width=26, bd=6).place(x=750, y=200)
    Button(root, text="VIDEOS", command=lambda: play_Animation(root), height=3, width=26, bd=6).place(x=750, y=100)
    Button(root, text="Back", command=lambda: face(root), height=3, width=26, bd=6).place(x=0, y=0)
    root.mainloop()

def play_rhymes(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("1100x550")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\er.gif')

    Button(root, text="Five Little Ducks", command=lambda : duck(root), height=3, width=26, bd=6).place(x=750, y=300)
    Button(root, text="Twinkel Twinkel Little Star", command=lambda: twinkle(root), height=3, width=26, bd=6).place(x=750, y=200)
    Button(root, text="Jony Jony Yes Pappa", command=lambda: jony(root), height=3, width=26, bd=6).place(x=750, y=100)
    Button(root, text="Noton Noton Payra Guli", command=lambda: noton(root), height=3, width=26, bd=6).place(x=750, y=400)
    Button(root, text="Back", command=lambda: entertainment(root), height=3, width=26, bd=6).place(x=0, y=0)


def jony(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/rhymes3.mp3")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def twinkle(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/rhymes2.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)


def noton(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/rhymes4.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def duck(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/rhymes1.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def play_Animation(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("1100x550")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\ideo.gif')

    Button(root, text="Sweet Cocoon", command=lambda: animation1(root), height=3, width=26, bd=6).place(x=750, y=300)
    Button(root, text="Watermelon A Cautionary Tale", command=lambda: animation2(root), height=3, width=26, bd=6).place(x=750, y=200)
    Button(root, text="A Night Alone", command=lambda: animation3(root), height=3, width=26, bd=6).place(x=750, y=100)
    Button(root, text="gNomE", command=lambda: animation4(root), height=3, width=26, bd=6).place(x=750, y=400)
    Button(root, text="Back", command=lambda: entertainment(root), height=3, width=26, bd=6).place(x=0, y=0)

def animation1(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/animation1.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def animation2(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/animation2.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def animation3(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/animation3.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def animation4(ag):
    ag.destroy()
    root = Tk()
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Videos/animation4.mp4")
    media_player.set_media(media)
    media_player.play()
    time.sleep(30)
    media_player.stop()
    play_rhymes(root)

def face(ag):
    ag.destroy()
    root = Tk()
    root.title("Home Page")
    root.geometry("800x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\eye.gif')

    Button(root, text="EXIT", command=lambda: exit(root), height=3, width=26, bd=6).place(x=10, y=300)
    Button(root, text="ENTERTAINMENT", command=lambda: entertainment(root), height=3, width=26, bd=6).place(x=290, y=300)
    root.mainloop()


a = 1
while a == 1 :
    root = Tk()
    root.title("Home Page")
    root.geometry("800x480")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('Photos\IGEQ.gif')

    Button(root, text="MONITOR MODE", command=lambda: exit(root), height=3, width=26, bd=6).place(x=100, y=300)
    Button(root, text="INTERACTIVE MODE", command=lambda: face(root), height=3, width=26, bd=6).place(x=600, y=300)
    root.mainloop()


