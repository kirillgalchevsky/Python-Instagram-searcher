import tkinter
from typing import ParamSpecKwargs
import webbrowser
import time
from tkinter import *
from tkinter import Entry

if __name__ == '__main__':
    app = Tk()
    app.geometry("600x400")
    app.title("inst_searcher")

    text = Text(app, width=20, height=1)
    text.insert(END,"")
    text.pack()

    def copy():
        username.config(text=""+text.get(1.0, "end-1c"))


    btnCopy = Button(app, text="copy", command=copy)
    btnCopy.pack()

    username = Label(app, text="")
    username.pack()

    def find():
        URL = "https://www.instagram.com/{0}/".format(username.cget("text"))
        webbrowser.open(URL, new=1)

    btnFind = Button(app, text="find", command=find)
    btnFind.pack()

    app.mainloop()
