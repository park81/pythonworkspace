import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키 엔터를 위해 필요

browser = webdriver.Chrome() #다른 위치에 있으면 해당 위치에 맞게 넣어야한다. 같은경로면 "./chromedriver.exe" 필요없다.

# 1. naver로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

# 4. 로그인 버튼 클릭
elem = browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)


# 7. 브라우저 종료
#brower.close() # 탭 종료
browser.quit() #전체 브라우저 종료