# from distutils.log import info
# from encodings import utf_8
# from fileinput import filename
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import camelot
# import os
# import sys

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

root = Tk()

root.title('Auto lunch menu')
root.resizable(False, False)
root.geometry('350x150')

def get_menu(index, filename):
    tables = camelot.read_pdf(filename)
    res = []
    day = "- thứ " + str(index + 1) + " -"
    res.append('/poll "Trưa nay ' + day + ' ăn gì" ')

    for i, item in enumerate(tables[0].df[index]):
        if i > 0 and i < 11:
            res.append('"' + item + '", ')
    
    filename = "menu-thu-" + str(index + 1) + ".txt"
    out = open(filename, "w+", encoding="utf_8")
    for line in res:
        out.write(line)
    out.close()

def open_file():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*,*')
    )

    file = fd.askopenfilename(
        title='Open file',
        initialdir='/',
        filetypes=filetypes
    )

    get_menu(1, file)
    get_menu(2, file)
    get_menu(3, file)
    get_menu(4, file)
    get_menu(5, file)

    showinfo(
        title='Completed',
        message='Complete generating menu from file ' + file
    )

btn_open = Button(root, text='Open PDF file', command=lambda: open_file(), relief=GROOVE, borderwidth=5)
btn_open.pack(expand=True)

root.mainloop()