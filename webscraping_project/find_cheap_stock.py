import csv
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

filename = "총액_주식.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #각 줄마다 Enter들어간다 newline=""빼면 / 엑셀에서 한글 깨지면 utf-8-sig 로 바꾸기
writer = csv.writer(f)

for i in range(0,2):

    url_init = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page=".format(i)
  
    if i ==0:
        stock_name=["코스피"]
        writer.writerow(stock_name)
    else:
        stock_name=["코스닥"]
        writer.writerow(stock_name)
    #종목군 별 PER
    #reference = "바이오/제약	20~30	게임	20	5G	20	IT산업	10~15	스마트폰	10	자동차	8~10	건설/해운업 8	소프트웨어	30~40	2차전지	20	의료장비	20	반도체/장비	10	폐기물	10	기타제조업	8~10	금융/증권	3~8".split("\t")
    reference = "바이오/제약:20~30	게임:20	5G:20	IT산업:10~15	스마트폰:10	자동차:8~10	건설/해운업:8	소프트웨어:30~40	2차전지:20	의료장비:20	반도체/장비:10	폐기물:10	기타제조업:8~10	금융/증권:3~8".split("\t")
    #title = "종목명	2017.12	2018.12	2019.12	2020.12(E)	2019.06	2019.09	2019.12	2020.03	2020.06	2020.09(E)	시가총액	링크".split("\t")
    #print(type(title))
    writer.writerow(reference)

    for i in range(1,30):
        url=url_init+str(i)
        soup = create_soup(url)
        print(url)
        data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
        for row in data_rows:
            columns = row.find_all("td")

            if len(columns) <=1: #의미 없는 데이터는 skip
                continue
            else:
                if columns[10].get_text().strip()=="N/A":
                    continue
                elif float(columns[10].get_text().strip().replace(",","")) > 0:
                    name = columns[1].get_text().strip()
                    total_stock=columns[6].get_text().strip()
                    code_num = row.find("a",attrs={"class":"tltle"})["href"]
                    link = "https://finance.naver.com"+code_num
                    soup2 = create_soup(link)
                    print(name)
                    print(link)
                    if soup2.find("table",attrs={"class":"tb_type1 tb_num tb_type1_ifrs"}):
                        data_rows2 = soup2.find("table",attrs={"class":"tb_type1 tb_num tb_type1_ifrs"}).find("tbody").find_all("tr")
                    else:
                        continue
                    #print(data_rows2)

                    # with open("stock.html", "w", encoding="utf8") as f:
                    #    f.write(data_rows2.prettify()) #html 문서를 예쁘게 출력

                # data_rows2 = find("tbody")
                    #soup2.find("table", attrs = {"class":"tbl","id":"cTB25"})#.find("tbody").find_all("tr")
                # print(data_rows2)
                # print(data_rows2[4].get_text)
                    last=[]
                    for idx, row2 in enumerate(data_rows2):
                        columns2 = row2.find_all("td")

                        if len(columns2) <=1: #의미 없는 데이터는 skip
                            continue
                        else:
                            result= [column.get_text().strip() for column in columns2]
                            #print(result)
                            if idx == 1:
                                result.insert(0,name)
                                result.append(total_stock)
                                

                            last.append(result)          

                    if "-" in last[1]:
                        continue

                    elif "" in last[1]:
                        #마지막 분기 값이 없을 때
                        if "" != last[1][1] and "" != last[1][2] and "" != last[1][3] and "" != last[1][5] and "" != last[1][6] and "" != last[1][7] and "" != last[1][8] and "" != last[1][9] and "" != last[1][11]:

                            if int(40*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",","")))/3)>int(last[1][11].replace(",","")) and 0<int(last[1][7].replace(",","")) and 0<int(last[1][8].replace(",",""))and 0<int(last[1][9].replace(",","")) and (int(last[1][3].replace(",",""))<int(4*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",","")))/3)) and (0<int(4*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",","")))/3)):    
                                #################몇 분기인지 표시하는 라인 ########################################
                                data_rows3 = soup2.find("table",attrs={"class":"tb_type1 tb_num tb_type1_ifrs"}).find("thead").find_all("tr")[1]
                                data_result = data_rows3.find_all("th")
                                data_result2= [column.get_text().strip() for column in data_result]
                                data_result2.insert(0,"")
                                data_result2.append("시가총액")
                                data_result2.append("링크")
                                
                                #몇배수 인지 확인
                                #data_result2.append("배수")
                                #현재 PER
                                data_result2.append("PER")
                                #무슨 분야 인지
                                data_result2.append("분야")
                                #현재 주가
                                data_result2.append("현재주가")
                                #목표 주가
                                data_result2.append("목표주가")

                                writer.writerow(data_result2)
                                ####################################################################################
                                #E: 영업이익 , B: 자산(장부가치), P: 가격(주가) , R(ratio):비율 PER: 영업이익에 대한 주식가격의 비율 PS(Per share): 주식수로 나눈다. EPS:  순이익을 주식수로 나눈다. BPS: 순자산(총자산-부채)를 주식수로 나눈다.
                                last[1].append(link.strip())
                                #몇배수 인지 확인
                                #result_a = int(40*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",","")))/3)/int(last[1][11].replace(",",""))
                                #현재 PER가 몇인지
                                result_a = int(last[1][11].replace(",",""))/int(4*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",","")))/3)

                                last[1].append(result_a)
                                #무슨 업종인지 확인
                                what_kind = soup2.find("h4",attrs={"class":"h_sub sub_tit7"}).find("em").find("a").get_text()
                                last[1].append(what_kind)  
                                #현재 주가
                                current_price = int(soup2.find("table",attrs={"class":"tb_type1 tb_num"}).find("tbody").find_all("tr")[0].find_all("td")[0].get_text().strip().replace(",",""))
                                last[1].append(current_price)
                                #타겟 주가
                                target_price = int((10/result_a)*current_price)
                                last[1].append(target_price)
                                writer.writerow(last[1]) #data를 list 형태로 넣어주면 된다.
                                print(last[1])
                        else:
                            continue
                            #int(last[1][1].replace(",",""))<
                            #and int(last[1][8].replace(",",""))<int(last[1][9].replace(",",""))
                            #<int(last[1][4].replace(",","")
                    else:

                        #last[1]: 영업이익 부분 : 종목명[0] 2017.12[1] 2018.12[2] 2019.12[3] 2020.12[4] 2019.09[5] 2019.12[6] 2020.03[7] 2020.06[8] 2020.09[9] 2020.12[10] 시가총애[11]
                        #int(last[1][2].replace(",",""))<int(last[1][3].replace(",","")) and int(20*(int(last[1][8].replace(",",""))+int(last[1][9].replace(",",""))))>int(last[1][11].replace(",","")) and int(last[1][8].replace(",",""))<int(last[1][9].replace(",",""))<int(last[1][10].replace(",","")) and 0<int(last[1][4].replace(",","")):
                        #if int(20*(int(last[1][8].replace(",",""))+int(last[1][9].replace(",",""))))>int(last[1][11].replace(",","")) and int(last[1][8].replace(",",""))<int(last[1][9].replace(",",""))<int(last[1][10].replace(",","")) and 0< int(last[1][4].replace(",","")):
                        if int(10*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",",""))+int(last[1][10].replace(",",""))))>int(last[1][11].replace(",","")) and 0<int(last[1][7].replace(",","")) and 0<int(last[1][8].replace(",","")) and 0<int(last[1][9].replace(",",""))and 0<int(last[1][10].replace(",","")) and (int(last[1][3].replace(",",""))<int(last[1][4].replace(",",""))) and  (0<int(last[1][4].replace(",",""))):    
                            #################몇 분기인지 표시하는 라인 ########################################
                            data_rows3 = soup2.find("table",attrs={"class":"tb_type1 tb_num tb_type1_ifrs"}).find("thead").find_all("tr")[1]
                            data_result = data_rows3.find_all("th")
                            data_result2= [column.get_text().strip() for column in data_result]
                            data_result2.insert(0,"")
                            data_result2.append("시가총액")
                            data_result2.append("링크")
                            #몇배수 인지 확인
                            #data_result2.append("배수")
                            #현재 PER
                            data_result2.append("PER")

                            #무슨 분야 인지
                            data_result2.append("분야")
                            #현재 주가
                            data_result2.append("현재주가")
                            #목표 주가
                            data_result2.append("목표주가")


                            writer.writerow(data_result2)
                            ####################################################################################


                            last[1].append(link.strip())
                            #몇배수 인지 확인
                            #result_a = (10*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",",""))+int(last[1][10].replace(",",""))))/int(last[1][11].replace(",",""))
                            result_a = int(last[1][11].replace(",",""))/(1*(int(last[1][7].replace(",",""))+int(last[1][8].replace(",",""))+int(last[1][9].replace(",",""))+int(last[1][10].replace(",",""))))
                            last[1].append(result_a)
                            #무슨 업종인지 확인
                            what_kind = soup2.find("h4",attrs={"class":"h_sub sub_tit7"}).find("em").find("a").get_text()
                            last[1].append(what_kind)  
                            #현재 주가
                            current_price = int(soup2.find("table",attrs={"class":"tb_type1 tb_num"}).find("tbody").find_all("tr")[0].find_all("td")[0].get_text().strip().replace(",",""))
                            last[1].append(current_price)
                            #타겟 주가
                            target_price = int((10/result_a)*current_price)
                            last[1].append(target_price)
                            writer.writerow(last[1]) #data를 list 형태로 넣어주면 된다.
                            print(last[1])
                            

                else:
                    continue
    #break

# filename = "시가총액1-200.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="") #각 줄마다 Enter들어간다 newline=""빼면 / 엑셀에서 한글 깨지면 utf-8-sig 로 바꾸기
# writer = csv.writer(f)

# title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# #["N", "종목명", .....]
# print(type(title))
# writer.writerow(title)


# for page in range(1, 5):
#     res = requests.get(url+str(page))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text,"lxml")

#     data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
#     for row in data_rows:
#         columns = row.find_all("td")
#         if len(columns) <=1: #의미 없는 데이터는 skip
#             continue
#         data = [column.get_text().strip() for column in columns] #strip() -> 불필요한공백 제거
#         writer.writerow(data) #data를 list 형태로 넣어주면 된다.