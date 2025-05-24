import requests
import urllib3

urllib3.disable_warnings()

url = 'https://weihei.jieyutest.com:11000/system-service/system/user/list'

headers = {
    'authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEyMzg4Mys3ZDg3ZDdkMjFhZjA0OTk1OTgyYTgwZTk3YTM1ZDE1MCJ9.lvdyRTrJfSbGqRIhQLKFZf17Yww7ZpM-F8hx1gwqeqMTEWqwPALYt1kO5jN4utwxLqhUfLOwbtSl3JgM4sQEDA'
}
#构建cookies字典


#创建get参数字典
data = {
    'pageNum':'1',
    'pageSize':'10',
    'page':"1"
}

response = requests.get(url, headers=headers, params=data, verify=False)
# response = requests.get(url, cookies=cookies, params=data, verify=False)
print(response.text)
print(response.headers)

# cookies_list = response.cookies
# print(cookies_list)
# cookies = {cookies_list.split('=')[0]: cookies_list.split('=')[-1] for cookie in cookies_list}
# print(cookies)


