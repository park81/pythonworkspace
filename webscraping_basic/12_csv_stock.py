import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #각 줄마다 Enter들어간다 newline=""빼면 / 엑셀에서 한글 깨지면 utf-8-sig 로 바꾸기
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
#["N", "종목명", .....]
print(type(title))
writer.writerow(title)


for page in range(1, 5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    # with open("stock.html", "w", encoding="utf8") as f:
    #     f.write(soup.prettify()) #html 문서를 예쁘게 출력
    data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <=1: #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] #strip() -> 불필요한공백 제거
        writer.writerow(data) #data를 list 형태로 넣어주면 된다.