from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/01-request')
def request_views():
    # print(dir(request))
    print('scheme:',request.scheme)
    print('method',request.method)
    print('args',request.args)
    print('form',request.form)
    print('cookies',request.cookies)
    print('files',request.files)
    print('path',request.path)
    print('full_path',request.full_path)
    print('url',request.url)
    print('header',request.headers)
    print('headers',request.headers['User-Agent'])
    #获取referer
    if 'Referer' in request.headers:
        print('请求源地址',request.headers['Referer'])
    return 'request'

@app.route('/test')
def test():
    return render_template('01-test.html')

@app.route('/get')
def get():
    return render_template('02-get.html')

@app.route('/02-server')
def server02():
    #通过request.args获取请求提交的数据
    #request.args[name]
    #request.args.get(name)
    #request.args.getlist(name)
    uname=request.args.get('uname')
    upwd=request.args['upwd']
    gender=request.args.get('gender')
    hobby=request.args.getlist('hobby')
    print('姓名:',uname)
    print('密码：',upwd)
    print('性别;',gender)
    print('爱好:',hobby)
    return '获取请求数据成功'

@app.route('/getexer')
def getexer():
    return render_template('03-getexer.html')

@app.route('/03-server')
def server03():
    title=request.args.get('title')
    classname=request.args.get('classname')
    text=request.args.get('text')
    print(title)
    print(classname)
    print(text)
    return '数据提交成功'

@app.route('/04-post')
def post_views():
    return render_template('04-post.html')

@app.route('/04-server',methods=['POST'])#post方法
def server04():
    uname=request.form.get('uname')
    upwd=request.form.get('upwd')
    return '接收post数据成功 姓名:%s 密码:%s'%(uname,upwd)

@app.route('/05-login',methods=['GET','POST'])
def login_views():
    #根据用户请求方式来决定到底要做什么
    if request.method == 'GET':
        #如果是get请求的话,则响应05-login.html模板
        return render_template('05-login.html')
    else:
        #如果是post请求的话,接收请求提交的数据做进一步处理
        uname=request.form.get('uname')
        upwd=request.form.get('upwd')
        return '姓名:%s,密码:%s'%(uname,upwd)

@app.route('/file',methods=['GET','POST'])
def file():
    if request.method == 'GET':
        return render_template('06-file.html')
    else:
        #1.从缓存区中得到上传的文件
        f=request.files['pic']
        #2.再将文件按照原始的名称保存进static目录中
        f.save('static/'+f.filename)
        return '文件上传成功'


if __name__ == "__main__":
    app.run(debug=True)