from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True #크롬을 백그라운드에서 뜨게 만듬 
options.add_argument("window-size=1920x1080")
#아래 내용 입력 안하면 headless라고 나온다. user agent 바꿀때도 때론 있다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()


# match() 처음부터 일치하는지
# search() 일치하는게 있는지
# findall() 일치하는 것 모두 리스트로
# Requests 웹페이지 읽어오기 -> 빠르다, 동적 웹 페이지 X # 주어진 url 을 통해 받아온 html 에 원하는 정보가 있을 때 사용하면 좋다.
# Selenium 웹페이지 자동화 -> 느리다, 동적 웹 페이지 O # 로그인, 어떤 결과에 대한 필터링 등 어떤 동작을 해야하는 경우
# Selenium -> 크롬 버전에 맞는 chromedriver.exe 가 반드시 있어야 한다.
# find_element(s)_by_id id로 찾기
# find_element(s)_by_class_name class name 으로 찾기
# find_element(s)_by_link_text 링크 text로 찾기
# find_element(s)_by_xpath xpath로 찾기

# click() 클릭
# send_keys() clear() 글자 입력
# selenium 기다림도 필요 - WebDriverWait

# 막 쓰면 안돼요
# 무분별한 웹 크롤링 / 웹 스크래핑은 대상 서버에 부하
# -> 계정 / IP 차단
# 데이터 사용 주의
# -> 이미지, 텍스트 등 데이터 무단 활용 시 저작권 등 침해 요소, 법적 제재
# robots.txt
# -> 법적 효력X, 대상 사이트의 권고, 해당 사항은 왠만하면 사용 X
