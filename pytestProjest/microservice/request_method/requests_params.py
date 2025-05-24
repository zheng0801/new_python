import requests
import urllib3

urllib3.disable_warnings()

url = 'https://weihei.jieyutest.com:11000/system-service/system/user/list'

headers ={
    'authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEyMzg4MytmMDhhOGVkYzNiMWU0YmJkYjg3MmNlOTAwYmZkNDYzMiJ9.3E4J2sue7WnfAMic2aNZ4LO3faMo1z24OsKSFxb84HcF3VKELcj5wNi-2K1RkRgERmqdxsmESLdQd-sMq-XUyQ'
}

#创建get参数字典
data = {
    'pageNum':'1',
    'pageSize':'10',
    'beginTime':'',
    'endTime':'',
    'page':"1"
}

response = requests.get(url, headers=headers, params=data, verify=False)
with open('user_list.txt', 'w', encoding='utf-8') as file:
    file.write(response.content.decode())
