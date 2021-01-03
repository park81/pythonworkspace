import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #res.text를 lxml 파서를 통해서 BeautifulSoup 객제로 만들어 가지고 있다.
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup는 모든 html 정보를 가지고 있으며 처음에 발견된 a 엘리먼트를 뿌려줌 #soup 객체에서 처음 발견되는 a elemnet 출력
# print(soup.a.attrs) #속성을 본다. (attribute?) / a element의 속성 정보 출력
# print(soup.a["href"]) #href정보만 가져온다. a element의 href 속성 '값' 정보를 출력할수있다.

#print(soup.find("a", attrs = {"class": "Nbtn_upload"})) #attrs는 조건 -> class가 Nbtn_upload 인 녀석에 대해서 찾아줘 # class값이 Nbtn_upload인 a element를 찾아줘 
#print(soup.find(attrs = {"class": "Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

#print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling #next_sibling -> 다음 형제로 넘어간다. / 두번 next이유-> 공백이 있으면 다다음이 되기 때문에
# rank3 = rank2.next_sibling.next_sibling

# print(rank3.a.get_text())
# rank2= rank3.previous_sibling.previous_sibling #위의 형제 호출
# print(rank2.a.get_text())

#print(rank1.parent) #부모 호출

# rank2 = rank1.find_next_sibling("li") #다음조건이 있는 다음 항목을 찾는다.
# print(rank2.a.get_text())
#print(rank1.find_next_siblings("li")) #다음 항목 형제들을 모두 찾아온다. siblings

webtoon = soup.find("a", text="두번째 생일-35화 눈물샤워")
print(webtoon)
