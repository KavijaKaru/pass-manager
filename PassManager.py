import tkinter


class Master:

    def __init__(self):
        self.master = tkinter.Tk()
        self.master.geometry("300x532+600+200")
        self.master.title("PassManager")
        self._frame = None
        backgroundImg = tkinter.PhotoImage(file="background.png")
        self.background = backgroundImg
        self.switch_frame(StartPage(self.master, self.background))

    def run_main_loop(self):
        self.master.mainloop()

    def switch_frame(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame
        self._frame.place(relwidth=1, relheight=1)


class Database:

    @staticmethod
    def database_check():
        with open("database.txt", 'w') as _:
            pass
        with open("database.txt", 'r') as data:
            content = data.readlines()
            if not content:
                return False
            else:
                return True

    @staticmethod
    def append_content(platform, password):
        with open("database.txt", "w") as db:
            print("Platform: {} \tPassword: {}".format(platform, password), file=db)

    @staticmethod
    def viewContent():
        with open("database.txt", 'r') as data:
            content = data.readlines()
            return content


def StartPage(root, img):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    tkinter.Label(image=img).place(relwidth=1, relheight=1)
    data = Database()
    if data.database_check():
        pass
    else:
        tkinter.Label(text="Welcome Back!", font="Helvetica 18").grid(row=0, column=2)
        # include button get started

    return frame


def GetStarted(root):
    frame = tkinter.Frame(root, relief='sunken', background='gray')

    # should include a background
    # should have entry to get the Master password
    # store Master password in th database in the first line
    # Save button
    # After clicking save should be redirected to startPage
    return frame


def showPage(root):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    # list of passwords and relevant platforms
    # Add new password button
    # button should direct to AddPass page
    return frame


def AddPass(root):
    frame = tkinter.Frame(root, relief='sunken', background='gray')
    # should include two entries
    # save details in database
    # should include a save button
    # should be directed to showPage

    return frame


master = Master()
master.run_main_loop()
