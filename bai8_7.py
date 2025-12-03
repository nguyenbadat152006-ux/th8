import tkinter
import random

# Danh sách các màu
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 120  # Thay đổi thời gian chơi từ 30s thành 120s

# Hàm bắt đầu game
def startGame(event):
    global timeleft
    if timeleft == 120:  # Bắt đầu countdown khi game bắt đầu
        countdown()
    nextColour()

# Hàm chọn và hiển thị màu tiếp theo
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()

        # Kiểm tra nếu nhập đúng màu
        if e.get().lower() == label.cget("fg").lower():
            score += 2  # Mỗi lần đúng cộng 2 điểm
        elif e.get():  # Nếu nhập sai và không rỗng
            score -= 1  # Mỗi lần sai trừ 1 điểm

        e.delete(0, tkinter.END)

        random.shuffle(colours)
        # Thay đổi chữ hiển thị và màu chữ
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

# Hàm countdown
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# Tạo cửa sổ GUI
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("400x250")

# Label hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Label điểm
scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Label thời gian
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Label hiển thị màu
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Entry nhập màu
e = tkinter.Entry(root)
e.pack()
e.focus_set()

# Bắt sự kiện nhấn Enter
root.bind('<Return>', startGame)

root.mainloop()
