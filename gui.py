from main import * 
import tkinter as tk
from tkinter.constants import END, RIGHT, WORD, Y
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.geometry("640x400")
root.title("Kiểm tra email spam")
root.resizable(0, 0)
scrollbar = tk.Scrollbar(root)


def browsefunc():
    filename = askopenfilename(filetypes=(("txt files", "*.txt"), ))
    ent1.delete(0, tk.END)
    ent1.insert(0, filename)
    content = open(filename)
    ent2.configure(state="normal")
    ent2.delete('1.0', END)
    ent2.insert("1.0", content.read())
    ent2.configure(state="disabled")


def checkSpam(content,path):
    if len(content) <= 1:
        popup = tk.Toplevel()
        popup.geometry("300x80")
        popup.wm_title("Chưa input file")
        label = tk.Label(
            popup, text="Vui lòng trỏ đường dẫn tới file để kiểm tra")
        label.pack()
        button = tk.Button(popup, text="Đóng", font=40,
                           command=lambda: popup.destroy())
        button.pack()
    else:
        Spam = detectSpam(path)
        print(Spam)
        if Spam:
            popup = tk.Toplevel()
            popup.geometry("300x80")
            popup.wm_title("Kết quả")
            label = tk.Label(popup, text="Đây LÀ mail spam")
            label.pack()
            button = tk.Button(popup, text="Đóng", font=40,
                               command=lambda: popup.destroy())
            button.pack()
        else:
            popup = tk.Toplevel()
            popup.geometry("300x80")
            popup.wm_title("Kết quả")
            label = tk.Label(popup, text="Đây KHÔNG LÀ mail spam")
            label.pack()  
            button = tk.Button(popup, text="Đóng", font=40,
                               command=lambda: popup.destroy())
            button.pack()


label1 = tk.Label(root, text="Chọn đường dẫn tới file cần kiểm tra spam")
label1.pack()

ent1 = tk.Entry(root, font=20, width=60)
ent1.pack()

b1 = tk.Button(root, text="Chọn file", height=1, font=20, command=browsefunc)
b1.pack()

label2 = tk.Label(root, text="Nội dung file")
label2.pack()

ent2 = tk.Text(root, font=15, width=60, height=9,
               yscrollcommand=scrollbar.set)
scrollbar.config(command=ent2.yview)
scrollbar.pack(side=RIGHT, fill=Y)
ent2.pack()

b2 = tk.Button(root, text="Kiểm tra", font=20, height=1,
               command=lambda: checkSpam(ent2.get("1.0", END),ent1.get()))
b2.pack()

root.mainloop()
