from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #Entry는 엔터가 입력 불가 -> ID나 로그인 등할때 사용하면 굿
e.pack()
e.insert(0,"한 줄만 입력해요") #글이 아무것도 없을땐 END나 0이나 시작위치 동일

def btncmd():

    #내용 출력
    print(txt.get("1.0",END))#처음부터 끝까지 모든 내용 가져온다. 1:라인1부터, 0:컬럼기준 0번쨰 위치부터 가져와라,END까지
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0, END)

btn = Button(root, text="클릭", command = btncmd)
btn.pack()


root.mainloop()