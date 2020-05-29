import pyglet
import tkinter

pyglet.font.add_file('font 1.ttf')
pyglet.font.add_file('font 3.otf')


class Master:

    def __init__(self):
        self.master = tkinter.Tk()
        self.master.geometry("300x432+600+200")
        self.master.title("PassManager")
        self._frame = None
        backgroundImg = tkinter.PhotoImage(file="background.png")
        self.background = backgroundImg
        self.switch_frame(StartPage(self, self.master, self.background))

    def run_main_loop(self):
        self.master.mainloop()

    def switch_frame(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame
        self._frame.place(relwidth=1, relheight=1)


class Database:

    def __init__(self):
        self.content = []

    def database_check(self):
        try:
            with open("database.txt", 'r') as data:
                self.content = data.readlines()
                if not self.content:
                    return False
                else:
                    return True
        except FileNotFoundError:
            with open("database.txt", 'w') as _:
                return False

    @staticmethod
    def append_content(password, platform=None):
        with open("database.txt", "a") as db:
            print("Platform: {} \tPassword: {}".format(platform, password), file=db)

    def viewContent(self):
        with open("database.txt", 'r') as data:
            outputString = " "
            self.content = data.readlines()
            for line in self.content:
                outputString += line
            return outputString


def StartPage(in_self, root, img):
    frame = tkinter.Frame(root, relief='sunken', background="#CD6155" )
    tkinter.Label(frame, image=img).place(relwidth=1, relheight=1)
    data = Database()
    if data.database_check():
        tkinter.Label(frame, text="Welcome Back!", font="{Stabillo Medium} 40", fg="white", background="purple").grid \
            (row=0, column=0, columnspan=2)
        tkinter.Label(frame, text="Master Password ", background='#806ce9', font="MOMCAKE").grid(row=2, column=0)
        masterPass = tkinter.Entry(frame, background='#806ce9', relief='groove', borderwidth=5, font="MOMCAKE")
        masterPass.grid(row=3, column=0)

        def CheckPass():
            with open("database.txt", "r") as db:
                content = db.readline().strip("\n")
                if content == masterPass.get():
                    in_self.switch_frame(showPage(in_self, root))
                else:
                    tkinter.Label(frame, text="Please try again :(").grid(row=4, column=0)

        tkinter.Button(frame, text="OK", background='#806ce9', font="MOMCAKE", command=CheckPass).grid(row=5, column=0)

    else:
        tkinter.Label(frame, text="Get Started!", font="{Stabillo Medium} 50", fg="white", background="#9B59B6").grid \
            (row=0, column=2)
        tkinter.Button(frame, text="Create Account", background='#806ce9', font="MOMCAKE", command=lambda:
        in_self.switch_frame(GetStarted(in_self, root, img))).grid(row=1, column=2)

    return frame


def GetStarted(in_self, root, img):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    tkinter.Label(frame, image=img).place(relwidth=1, relheight=1)
    tkinter.Label(frame, text="Name").grid(row=1, column=1)
    tkinter.Entry(frame).grid(row=2, column=1)
    tkinter.Label(frame, text="New Master Password").grid(row=3, column=1)
    store_master = tkinter.Entry(frame)
    store_master.grid(row=4, column=1)
    tkinter.Button(frame, text="Save", command=lambda: store_and_redirect()).grid(row=5, column=1)

    def store_and_redirect():
        with open("database.txt", "a") as db:
            print(store_master.get(), file=db)
        in_self.switch_frame(StartPage(in_self, root, img))

    return frame


def showPage(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    # frame.rowconfigure(0, weight=100000)
    # frame.rowconfigure(1, weight=100)
    show_text = tkinter.Text(root, height=20, font="{Stabillo Medium}")
    show_text.grid(row=1, column=0)
    DataBase = Database()
    show_text.insert(tkinter.END, DataBase.viewContent())
    tkinter.Button(root, text="Add Password", command=lambda: in_self.switch_frame(AddPass(in_self, root))).grid(row=2, column=0, sticky="sw")
    return frame


def AddPass(in_self, root):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    tkinter.Label(frame, text="Platform").grid(row=0, column=0)
    plat = tkinter.Entry(frame)
    plat.grid(row=1, column=0)
    tkinter.Label(frame, text="Password").grid(row=2, column=0)
    _pass = tkinter.Entry(frame)
    _pass.grid(row=3, column=0)
    tkinter.Button(frame, text="Save", command=lambda: addPassFunc()).grid(row=4, column=0)

    def addPassFunc():
        data = Database()
        data.append_content(platform=plat.get(), password=_pass.get())
        in_self.switch_frame(showPage(in_self, root))

    return frame


master = Master()
master.run_main_loop()
