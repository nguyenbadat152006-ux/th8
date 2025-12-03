import tkinter as tk

def ShowChoice():
    print("Giá trị lựa chọn:", v.get())

root = tk.Tk()
root.title("RadioButton vs Indicator Example")
root.geometry("300x300")

# Biến lưu giá trị lựa chọn
v = tk.IntVar()
v.set(1)  # Khởi tạo mặc định

languages = ["Python", "Perl", "Java", "C++", "C"]

# --------- RadioButton truyền thống ---------
tk.Label(root, text="RadioButton truyền thống:", pady=5).pack(anchor=tk.W)

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

# --------- RadioButton dạng indicator (nút nhấn) ---------
tk.Label(root, text="RadioButton dạng nút nhấn:", pady=10).pack(anchor=tk.W)

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,  # Chuyển thành nút nhấn
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
