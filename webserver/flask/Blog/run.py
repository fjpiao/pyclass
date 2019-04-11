from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import os
app = Flask(__name__)
#数据库连接配置
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost/blog'
#指定启动模式为调试模式
app.config['DEBUG']=True
#取消信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#创建数据库实例
db=SQLAlchemy(app)
#创建Manager对象用于管理app
manager = Manager(app)

#实现数据迁移指令
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

#创建实体类
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(120),nullable=False,unique=True)
    url=db.Column(db.String(120),nullable=True)
    email=db.Column(db.String(120),nullable=False,unique=True)
    password=db.Column(db.String(100),nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        #1.接收前端传递过来的username和password
        username = request.form.get('username')
        password = request.form.get('password')
        #2.判断username和password在数据库中是否存在
        user=db.session.query(User).filter_by(username=username,password=password).first()
        if user:
            return "<script>alert('登录成功');</script>"
        else:
            return '<script>alert("登录失败");location.href="/login";</script>'





@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        user = User()
        user.username=request.form.get('username')
        user.password=request.form.get('password')
        user.email = request.form.get('email')
        user.url = request.form.get('url')
        db.session.add(user)
        db.session.commit()

        return "注册成功"

@app.route('/release',methods=['GET','POST'])
def release():
    if request.method=='GET':
        return render_template('')
    else:
        #获取数据
        author = request.form['author']
        list = request.form['list']
        print('标题:%s'%author)
        print('类型:%s'%list)
        #判断是否有文件上传
        if request.files:
            #有文件上传
            picture=request.files['picture']
            ext = picture.filename.split['.'][-1]
            ftime=datetime.datetime.now().strftime('%Y%m%d%h%M%S%F')
            filename = ftime + '.' +ext
            basedir=os.path.dirname(__file__)
            upload_path=os.path.join(basedir,'static/upload',filename)
            picture.save(upload_path)
            print('上传路径:%s'%upload_path)
            content= request.form['content']
            print('内容:%s'%content)
            return '发布博客成功'
if __name__ == '__main__':
    manager.run()


