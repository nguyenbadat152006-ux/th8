from tkinter import *
from tkinter import messagebox

def NewFile():
    messagebox.showinfo("New", "New File!")

def About():
    messagebox.showinfo("About", "This is a simple example of a menu")

def OpenFile():
    messagebox.showinfo("Open", "You selected: Open File")

def Exit():
    root.quit()

def InsText():
    messagebox.showinfo("Insert Text", "You selected: Insert Text")

def InsPic():
    messagebox.showinfo("Insert Picture", "You selected: Insert Picture")

root = Tk()
root.title("tk")

menu = Menu(root)
root.config(menu=menu)

# ----- File menu -----
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# ----- Insert menu -----
insmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insmenu)
insmenu.add_command(label="Text", command=InsText)
insmenu.add_command(label="Picture", command=InsPic)

# ----- Help menu -----
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
