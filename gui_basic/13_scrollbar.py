from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

#스크롤 바는 스크롤바와 스크롤바 위젯이 되는것을 하나의 Frame에 넣는것이 관리편하다.

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill ="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1,32) :
    listbox.insert(END, str(i) + "일") #1일, 2일 ...

listbox.pack(side="left")

scrollbar.config(command=listbox.yview) #scrollbar와 listbox 매칭 시켜준다.



root.mainloop()