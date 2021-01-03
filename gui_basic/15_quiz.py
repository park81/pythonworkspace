import os
from tkinter import *

root = Tk()

root.title("제목 없음 - Windows 메모장")
#root.geometry("640x480") #가로 * 세로

root.geometry("640x480+300+100") #가로 * 세로 + x좌표 + y좌표

root.resizable(True, True) # 너비, 높이 값 변경 불가 (창 크기 변경 불가)

menu = Menu(root)

#열기, 저장 피일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8")  as file:
            txt.delete("1.0", END) #텍스트 삭제 
            txt.insert(END,file.read()) #텍스트 읽기

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) #모든 내용 가져와 저장
    
#파일 메뉴
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기", command=open_file)
menu_file.add_command(label = "저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기",command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill ="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
txt = Text(root, yscrollcommand = scrollbar.set)

txt.pack(side="left",fill="both",expand ="true")
#text.grid(row=0, column = 0, sticky=N+E+W+S)

scrollbar.config(command=txt.yview) #scrollbar와 text 매칭 시켜준다.


root.config(menu=menu)
root.mainloop()