#encoding:UTF-8
# chenzy python flask

# 导入 Flask 和 静态网页
from flask import Flask,render_template
app = Flask(__name__)

# controller (习惯于Java mvc架构称呼)
@app.route("/index",methods = ["GET"])
@app.route("/",methods = ["GET"])
def index():
    return render_template('index.html')



# controller (习惯于Java mvc架构称呼)
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