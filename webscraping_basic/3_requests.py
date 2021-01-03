import requests

res=requests.get("http://google.com")

#print("응답코드 :", res.status_code) #200 이면 정상

# if res.status_code == requests.codes.ok: #200이 ok
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 " , res.status_code, "]")
res.raise_for_status() #에러가 생기면 진행지니 않음.(오류를 내밷고 여기서 끝냄)

print(len(res.text))

with open("mygoolge.html","w",encoding="utf8") as f:
    f.write(res.text)