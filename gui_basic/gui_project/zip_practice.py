kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

print(list(zip(kor, eng))) # 두개 합치기

mixed =[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

print(list(zip(*mixed))) #앞에꺼 끼리 뒤에꺼 끼리 분리