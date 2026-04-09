import requests

url = "http://localhost:8088/lEARN/phpforsec/board/delete.php"
id = int()

data = {
    'post_id': id
}
re = requests.post(url=url, data=data)
print(re.text)
