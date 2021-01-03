from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo=PhotoImage(file="gui_basic/img.png")
label2 = Label(root,image=photo)
label2.pack() # label을 단순히 글자나 그림을 넣어준다.

def change():
    label1.config(text="또 만나요") #글자 변경 config

    global photo2 #전역변수로 선언하지 않으면 garbage Collection이 불필요하다고 지우기 때문에 전역변수로  저장 필요
    photo2=PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)



btn = Button(root, text="클릭", command = change)
btn.pack()


root.mainloop()
