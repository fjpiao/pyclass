from flask import Flask, render_template

app = Flask(__name__)


@app.route('/calc/<num1>/<int:num2>')
def calc(num1, num2):
    # 将num1和num2转换成数字
    num1 = int(num1)

    # 拼接响应输出的字符串
    s = '<h1>%d+%d=%d</h1>' % (num1, num2, num1 + num2)
    s += '<h1>%d-%d=%d</h1>' % (num1, num2, num1 - num2)
    return s


@app.route('/')
@app.route('/index')
@app.route('/<int:num>')
@app.route('/index/<int:num>')
def pa(num=1):
    return '%d' % (num)


@app.route('/mytemp')
def mytemp():
    str = render_template('index.html',name1='lalala',name2='hahaha')
    print(str)
    return str


if __name__ == '__main__':
    app.run(debug=True)
