from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-var')
def var01():
    str = render_template('01-var.html', name1='gaga', name2='lalal')
    print(str)
    return str


# 演示允许传递到模板中做变量的类型
@app.route('/02-var')
def var02():
    # 字符串
    name = 'meng'
    # 数字
    age = 20
    # 列表,元组,字典
    list = ['a', 'b', 'v']
    tup = ('1', '2', '5')
    dic = {
        'n1': '10',
        'n2': '11',
        'n3': '12'
    }
    # 对象
    person = Person()
    person.name = 'weisss'
    # params={
    #     'name':name,
    #     'age':age,
    #     'list':list,
    #     'tup':tup,
    #     'dic':dic,
    #     'person':person
    # }
    params = locals()
    print(params)
    return render_template('02-var.html', params=params)


class Person(object):
    name = 'wei'

    def a1(self):
        return self.name


@app.route('/')
def macro():
    list = [1, 2, 3]
    return render_template('03-macro.html', list=list)

@app.route('/04-static')
def static_views():
    return render_template('04-static.html')

@app.route('/05-parent')
def parent():
    return render_template('05-parent.html')

@app.route('/06-child')
def child():
    return render_template('06-child.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
