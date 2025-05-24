import requests

response = requests.get('https://video.fjjieyu.com:8443/login')
print(response.status_code)
print(response.text)
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print('没有json格式')
# print(response.json())


# response = requests.post(
#     'https://passport.baidu.com/v2/api/?login',
#     data={"username":"13546567864","password":"admin123"},
# )
# print(response.status_code)

params = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get('https://video.fjjieyu.com:8443/login', params = params)
print(response.url)
print(response.encoding)
print(response.content)
print(response.raw)
print(response.headers)
print(response.request.headers)