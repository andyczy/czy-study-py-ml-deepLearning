#encoding:UTF-8
# chenzy python flask

# 导入 Flask 和 静态网页
from flask import Flask,render_template
app = Flask(__name__)
# 所有Flask程序都必须创建一个程序实例。
# Web服务器使用一种名为Web服务器网关接口（Web Server Gateway Interface，WSGI）的协议，
# 把接收自客户端的所有请求都转交给这个对象处理。



# 处理URL和函数之间关系的程序称为路由。
@app.route("/index",methods = ["GET"])
@app.route("/",methods = ["GET"])
# 像index()这样的函数称为视图函数（view function）。
def index():
    # Flask 提供的 render_template 函数把 Jinja2 模板引擎集成到了程序中。
    return render_template('index.html')

# 动态路由。
# Flask支持在路由中使用int、float和path类型。path类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# 启动程序
if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 8989,  
        debug = True 
    )