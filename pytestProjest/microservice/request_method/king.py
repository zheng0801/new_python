import requests
import json
import urllib3

#禁用不安全提示警告
urllib3.disable_warnings()

class King():

    def __init__(self):
        #定义请求的url
        self.url = 'https://weihei.jieyutest.com:11000/system-service/system/role'
        #定义请求头，包括内容类型和授权信息
        self.headers = {
            "content-type" : "application/json",
            "authorization" : "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEyMzg4MytkN2Q1NGQ2ZmYxNWI0ZWNmOTI3M2YzOGUyYzA4MjI1YiJ9.V7L_INhkPPV1pqEAuYoIJeygxEN_VEmQNH_20X82K6ievORPrDa7UUONW9fERTzJRFfMsS5j_6bca3OrabgHAg"
        }
        #定义请求的json数据
        self.json_data = {
            "roleName": "11",
            "roleKey": "11",
            "roleSort": 1,
            "status": "0",
            "menuIds": []
        }

    # def add_json_data(self, json_key, json_value):
    #
    #     new_json_data = self.json_data
    #     #将json格式数据转换成字典
    #     dict_data = json.loads(new_json_data)
    #     #向字典中添加数据
    #     dict_data[json_key] = json_value
    #     #将字典转换成json格式
    #     json_data = json.dumps(dict_data)


    def post_data(self):
        #发送post请求
        response = requests.post(self.url, headers=self.headers, json=self.json_data, verify=False)
        return response.text

    def parse_data(self,data):
        #使用loads方法将json格式转换成python字典
        dict_data = json.loads(data)
        print(dict_data['message'])

    def run(self):
        response = self.post_data()
        print(response)
        self.parse_data(response)

if __name__ == '__main__':
    king = King()
    king.run()
