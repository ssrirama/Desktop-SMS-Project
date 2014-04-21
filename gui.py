__author__ = 'Tyler'
from tkinter import *

# from pickle import *
# file = open('bookshelf', 'r+')
# shelf = Pickler()
# librarian = Unpickler()
# try:
#     file = open('bookshelf', 'r+')
# except:
#     print("Sorry Not Sorry")

master = Tk()
toBeCalled = {}
m1 = PanedWindow(master)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="Please Enter a name and Phone ")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)


top = Entry(m2, text="Enter Name")
m2.add(top)
top.focus_set()
bottom = Entry(m2, text="Enter Phone Number")
m2.add(bottom)


def button1click():
    toBeCalled[top.get()] = bottom.get()
    print(top.get())


button1 = Button(master, text="Done", command=button1click)
button1.pack()
m1.add(button1)


mainloop()
# file.close()
print(toBeCalled)
