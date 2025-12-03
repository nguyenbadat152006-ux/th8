from tkinter import *

# a) Tao cua so do hoa
window = Tk()
window.title("Demo Tkinter")
window.geometry('350x200')  # kich thuoc cua so

# Label hien thi chu
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)


# c) Ham xu ly su kien khi bam nut
def clicked():
    lbl.configure(text="Button was clicked !!")  # thay doi noi dung label


# b) Them widget Button
# d) Thay doi mau nen (bg) va mau chu (fg)
btn = Button(window, 
             text="Click Me", 
             bg="lightblue",   # mau nen
             fg="red",         # mau chu
             command=clicked)  # goi ham clicked khi nhan nut

btn.grid(column=1, row=0)


# vong lap giao dien
window.mainloop()
