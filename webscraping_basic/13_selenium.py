from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키 엔터를 위해 필요

browser = webdriver.Chrome() #다른 위치에 있으면 해당 위치에 맞게 넣어야한다. 같은경로면 "./chromedriver.exe" 필요없다.
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back() # 뒤로가기
# browser.forward() #앞으로 가기
# browser.refresh() #새로고침
elem = browser.find_element_by_id("query")

elem.send_keys("나도코딩") #Keys는 엔터를 위해 존재
elem.send_keys(Keys.ENTER)

elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")

browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩") #Keys는 엔터를 위해 존재
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()
browser.close() #현재 열려있는 Tab만 종료
browser.quit() #현재 열려있는 모든 브라우져 종료
