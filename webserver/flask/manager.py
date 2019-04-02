from flask import Flask

# 将当前的运行的主程序建成Flask应用，以便接收用户请求和相应
app = Flask(__name__)


# @app.route()是Flask中的路由定义,主要是为了匹配用户的访问路径
# '/'表示的是整个网站的根(域名或ip地址)，'index'表示的是此定义的访问路径(可以自由定义)
# index():表示匹配上路径之后的处理程序,视图处理函数(Views),视图处理函数中必须要有一个返回值,现在阶段必须返回一个字符串表示要响应的客户端浏览器的内容
@app.route('/index')  # 根相对路径　表示域名(ip)
def ind():
    return '<button clickon="">s</button>'


@app.route('/')
@app.route('/1')
def first():
    a = 2
    print(a)
    return '<h1>首页<h1>'


@app.route('/show/<name>/<path:gender>')
def show(name, gender):
    print('name的类型为:', type(name))
    print('gender的类型为:', type(gender))
    return name + gender


if __name__ == '__main__':
    # run():启动程序
    # debug=True,调试模式,真正部署运行时debug=False
    app.run(debug=True)
