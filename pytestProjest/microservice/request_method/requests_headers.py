import requests
import urllib3

urllib3.disable_warnings()

url = 'https://video.fjjieyu.com:8443/login'
url_login = 'https://weihei.jieyutest.com:11000/auth-service/auth/login'

#构建json格式参数字典
json = {
            'code': "112233",
            'password': "Joyusing@2024",
            'username': "admin"
            }

#构建请求头字典
headers = {
    'Content-Type':'application/json',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'

}

# response = requests.get(url)
#发送带请求头和json格式参数的post请求,verify=False临时禁用证书验证
response = requests.post(url_login, data=json, headers=headers, verify=False)
print(response.text)
print(response.request.headers)





