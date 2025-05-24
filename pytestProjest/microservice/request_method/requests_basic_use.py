import requests

#目标url
url = 'https://video.fjjieyu.com:8443/login'
url_login = 'https://video.fjjieyu.com:8443/auth-service/auth/login'
json = {
            'code': "112233",
            'loginType': "1",
            'password': "Joyusing@2024",
            'username': "admin"
            }

#向目标url发送get请求
# response = requests.get(url)
response = requests.post(url_login, json)

# print(response.encoding)
# #打印源码的str类型数据
# print(response.text)
#
# #修改编码格式
# response.encoding = 'utf-8'
# #打印修改后的数据
# print(response.text)
#
# print(response.encoding)
#
# #response.content是存储的bytes类型的响应源码，可以进行decode操作
# print(response.content.decode())

#常见的响应对象参数和方法

# #响应的url
# print(response.url)
#
# #状态码
# print(response.status_code)

#响应对象的请求头
print(response.request.headers)

#响应对象的响应头
print(response.headers)

#打印请求携带的cookies
print(response.request._cookies)

#打印响应中携带的cookies
print(response.cookies)





