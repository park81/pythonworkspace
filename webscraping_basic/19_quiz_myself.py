import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키 엔터를 위해 필요
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome() #다른 위치에 있으면 해당 위치에 맞게 넣어야한다. 같은경로면 "./chromedriver.exe" 필요없다.

browser.get("http://daum.net")

browser.find_element_by_class_name("tf_keyword").send_keys("송파 헬리오시티")
time.sleep(1)
#browser.find_element_by_class_name("ico_pctop btn_search").click()
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()
count = 0
try:
    #elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"txt_ac")))
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='estateCollTabContentsResult']/div/table/tbody")))
    #lst=list(elem.text)
    #print(elem.text[1].strip())
    lst=elem.text.strip().split("\n")
    for i in range(0,len(lst)-4,5):
        count+=1
        print("========== 매물 {} ==========".format(count))
        print("거래: ", lst[i])
        print("면적: ", lst[i+1], "(공급/전용)")
        print("가격: ", lst[i+2],"(만원)")
        print("동: ", lst[i+3])
        print("층: ", lst[i+4])

    # for value in elem.text:
    #     print(value)

finally:
    
    browser.quit()



