from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Thông tin sinh viên")

Label(root, text="Họ tên:").grid(row=0, column=0)
Label(root, text="Ngày sinh:").grid(row=1, column=0)
Label(root, text="MSSV:").grid(row=2, column=0)
Label(root, text="Ngành học:").grid(row=3, column=0)

ten = Entry(root, width=30)
ns = Entry(root, width=30)
mssv = Entry(root, width=30)
nganh = Entry(root, width=30)

ten.grid(row=0, column=1)
ns.grid(row=1, column=1)
mssv.grid(row=2, column=1)
nganh.grid(row=3, column=1)

def submit():
    info = f"Họ tên: {ten.get()}\nNgày sinh: {ns.get()}\nMSSV: {mssv.get()}\nNgành: {nganh.get()}"
    messagebox.showinfo("Thông tin sinh viên", info)

Button(root, text="Submit", command=submit).grid(row=4, column=1)

root.mainloop()
