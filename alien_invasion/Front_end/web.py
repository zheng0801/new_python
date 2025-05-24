from flask import Flask, render_template

#实例化Flask类
#实例化中加上一个template_folder = 'XXX'，可以修改存放html文件的位置为XXX
app = Flask(__name__)

#创建网址/show/info和index()函数的对应关系
#访问/show/info时执行index()
@app.route('/')
def index():
    #Flask内部会自动打开index.html这个文件，并读取内容，将内容返回给用户
    #默认去当前项目的templates目录找文件
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/user/list')
def user_list():
    return render_template('user_list.html')

# @app.route('/show/info')
# def two_index():
#     #返回福建联通
#     return '福建联通'

if __name__ == '__main__':
    #可以定义端口和hosts，run(host = '', port = '')
    app.run()
