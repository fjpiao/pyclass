from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func

# 导入pymysql,并且将其伪装成MySQLdb 可以在配置数据库加入'+pymysql'来代替
# import pymysql
# pymysql.install_as_MySQLdb()


app = Flask(__name__)
# 通过app配置数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
# 关闭追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 指定启动模式为调试模式
app.config['DEBUG'] = True
# 配置数据库操作的自动提交 卸载视图函数的时候
# 每次再执行完视图处理函数时将自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建SQLAlchemy的实例
db = SQLAlchemy(app)

# 将app交给Manager进行管理,以后由Manager来启动程序
manager = Manager(app)

# 创建Migrate对象,指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加子命令,增加做数据库迁移的子命令
# 为manager增加一个叫做db的子命令,该命令的具体执行操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


# 创建一个实体类－Users,映射到数据库中users表
# id 主键　自增
# username,长度为80的字符串,不允许为空,唯一,加索引
# age,整数,允许为空
# email,长度为120的字符串,必须唯一
class Users(db.Model):
    __tablename__ = 'users'  # 如果表名为users的话,则可以省略
    id = db.Column(db.Integer, primary_key=True)  # 主键默认自增
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean, default=True)

    # 重写__repr__函数
    def __repr__(self):
        return '<Users:%r>' % self.username


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个外键列,要引用自course表的主键id
    cid = db.Column(
        db.INTEGER,
        db.ForeignKey('course.id')
    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), unique=True, index=True)
    # 增加关联属性和反向引用关系属性
    teachers = db.relationship(  # course.teachers
        'Teacher',  # 对应类名
        backref='course',  # teacher.course
        lazy='dynamic'
    )


# 更新字段时需要先通过db.dropa_all() 先删除所有的表结构
# db.drop_all()
# 再通过db.create_all()将Users类映射到数据库上
# db.create_all()
# 但使用以上方法增加字段会删除数据　不实用
# 使用manager来避免此问题

@app.route('/')
def index():
    return '这是我的Flask程序中的主页'


@app.route('/01-add')
def add_views():
    # 1.创建Users的对象
    user = Users()
    # 2.对象属性赋值　插入数据
    user.username = 'xiaoze'
    user.age = 30
    user.email = 'maria@163.com'

    user.username = 'daze'
    user.age = 40
    user.email = 'aria@163.com'

    user.username = 'zhongze'
    user.age = 42
    user.email = 'bbria@163.com'

    user.username = 'buze'
    user.age = 45
    user.email = 'hshria@163.com'

    # 3.将Users的对象保存回数据库并提交
    db.session.add(user)
    # 4.提交　否则回滚
    db.session.commit()

    return '增加数据成功'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        # 创建Users对象
        user = Users()
        # 接收前端传递过来的数据
        user.username = request.form['username']
        user.email = request.form['email']
        user.age = request.form['age']
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        # 将数据构建成Users的对象
        db.session.add(user)
        # 将对象保存回数据库
        db.session.commit()

        return redirect('/03-queryall')


@app.route('/03-query')
def query_views():
    # #查询Users类(users表)中所有的数据
    # query=db.session.query(Users)
    # print(query)#输出为SQL查询语句
    # print('类型为:',type(query))

    # 查询Users类(users表)中所有的数据
    users = db.session.query(Users).all()
    print(users)
    for user in users:
        # users表示的就是users列表中的每一条数据(Users对象)
        print('姓名:%s,邮箱:%s' % (user.username, user.email))
    return '查询数据成功'


@app.route('/03-queryall')
def queryall_views():
    # 接收前端传递过来的kw参数,如果没有则为''
    word = request.args.get('word')
    if not word:
        users = db.session.query(Users).all()
    else:
        users = db.session.query(Users).filter(
            or_(
                Users.email.like('%' + word + '%'),
                Users.username.like('%' + word + '%')
            )
        ).all()
    return render_template('03-queryall.html', users=users, word=word)


@app.route('/04query')
def query04_views():
    # 1.查询age>40并且isActive为True的Users的信息
    # users = db.session.query(Users).filter(Users.age > 40, Users.isActive == True).all()

    # 2.查询age>40或者isActive为True
    # users = db.session.query(Users).filter(or_(Users.age > 40, Users.isActive == True)).all()
    # print(users)
    # 3.查询年龄是30或35的users的信息　使用in＿()
    # users= db.session.query(Users).filter(Users.age.in_([30,35])).all()
    # users=db.session.query(Users).filter(Users.age.between(30,40)).all()
    # 4.查询id=1的users的信息
    # users=db.session.query(Users).filter_by(id=1).first()
    # 5.年龄降序
    users = db.session.query(Users).order_by('age desc').all()
    print(users)
    return '查询成功'


@app.route('/aggregate')
def aggregate_views():
    # 1.查询Users实体中所有人的年龄的总和
    # result=db.session.query(func.sum(Users.age)).all()
    # print('所有人年龄和为%d'%result[0])
    # 2.查询Users实体中所有人的平均年龄,年龄总和,最大年龄和最小年龄分别是多少
    # result=db.session.query(
    #     func.avg(Users.age),
    #     func.sum(Users.age),
    #     func.max(Users.age),
    #     func.min(Users.age)
    # ).all()
    # print('平均年龄：%.2f,总年龄：%d,max:%d,min:%d'%(result[0][0],result[0][1],result[0][2],result[0][3]))
    # 3.查询Users实体中,按isActive分组后每组的人数
    # result=db.session.query(Users.isActive,func.count('*')).group_by('isActive').all()
    # print(result)
    # 4.查询Users实体中,按isActive分组后每组的平均年龄,并且将平均年龄大于18岁的组的信息查询出来
    result = db.session.query(
        Users.isActive,
        func.avg(Users.age),
    ).group_by(
        'isActive'
    ).having(
        func.avg(Users.age) >= 18
    ).all()
    print(result)
    return '聚合查询成功'


@app.route('/aggregateexer')
def aggregate_exer():
    # 1.查询Users中所有人的总年龄
    result = db.session.query(
        func.sum(Users.age)
    ).all()
    print(result)
    # 2.总人数
    result = db.session.query(
        func.count(Users.id)
    ).all()
    print(result)
    # 3.年龄大于18岁的人的平均年龄
    result = db.session.query(
        func.avg(Users.age)
    ).filter(
        Users.age >= 18
    ).all()
    print(result)
    # 4.查询Users实体中按isActive分组后,组内人数大于2人的组的信息(组,人数)
    result = db.session.query(
        Users.isActive,
        func.count('*')
    ).group_by(
        'isActive'
    ).having(
        func.count('*') > 2
    ).all()
    print(result)
    # 5.年龄大于18岁按isActive分组后，组内大于２人的信息(组，人数)
    result = db.session.query(
        Users.isActive,
        func.count('*')
    ).filter(
        Users.age >= 18
    ).group_by(
        'isActive'
    ).having(
        func.count('*') > 2
    ).all()
    print(result)
    return '成功'


@app.route("/delete")
def delete():
    id = request.args['id']
    users = Users.query.filter_by(id=id).first()
    db.session.delete(users)
    return redirect('/03-queryall')


@app.route('/update', methods=['GET', 'POST'])
def updateee():
    # get请求的话,则接收传递过来的id,并查询数据显示在09-update.html上
    if request.method == 'GET':
        id = request.args['id']
        user = Users.query.filter_by(id=id).first()
        return render_template('update.html', user=user)
    # post请求的话,则接收要修改的所有的数据并更新回数据库
    # 接收前端传递过来的id,username,age,email,isActive的值
    else:
        id = request.form['id']
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        isActive = False
        if 'isActive' in request.form:
            isActive = True
        user = Users.query.filter_by(id=id).first()
        user.username = username
        user.age = age
        user.email = email
        user.isActive = isActive
        db.session.add(user)
        return redirect('/03-queryall')


@app.route('/regtea')
def regtea_views():
    # 方案一:声明一个Teacher对象,通过外键属性来关联对应的course的id值
    # tea=Teacher()
    # tea.tname='率则Maria'
    # tea.tage=28
    # tea.cid=1#通过cid属性为teacher的外键赋值
    # db.session.add(tea)

    # 方案二:声明一个Teacher对象,通过course属性来关联对应的course值
    tea = Teacher()
    tea.tname = 'laowei'
    tea.tage = 47
    # 获取id为1的课程的信息
    course = Course.query.filter_by(id=1).first()
    # 将上面course对象与tea中Course()创建给Teacher()的course对象关联
    tea.course = course
    db.session.add(tea)

    return '注册teacher成功'


@app.route('/keyquery')
def keyquery():
    # 1.查询xiaoming的个人信息以及所教授的课程
    tea = Teacher.query.filter_by(tname='xiaoming').first()
    print('姓名:%s,年龄:%d' % (tea.tname, tea.tage))
    # 通过tea对象的course属性获取对应的课程对象
    print('所教课程:%s' % tea.course.cname)
    # 2.查询Python基础课程所对应的所有的老师的信息
    course = Course.query.filter_by(cname='P基础').first()
    print('课程名称:%s' % course.cname)
    # 通过course中的关联属性teachers来获取对应的所有的老师的信息
    # course.teachers表示的是course所对应的teachers的一个查询对象
    # (AppenderBaseQuery类型,属于BaseQuery的子类)
    print(course.teachers)
    print(type(course.teachers))
    teachers = course.teachers.all()
    print(teachers)
    for tea in teachers:
        print('老师姓名:%s' % tea.tname)
    return '查询成功'


@app.route('/teacherreg', methods=['GET', 'POST'])
def teacherreg():
    if request.method == 'GET':
        # 查询Course实体类中所有的数据
        courses = Course.query.all()
        return render_template('/teacherreg.html', courses=courses)
    else:
        teacher = Teacher()
        teacher.tname = request.form['tname']
        teacher.tage = request.form['tage']
        teacher.course = Course.query.filter_by(id=request.form['cid']).first()
        db.session.add(teacher)
        return redirect('/teacherreg')


@app.route('/teacherquery')
def teacherquery():
    courses = Course.query.all()
    cid = request.args.get('cid', '0')  # 0为默认值

    if cid == '0':
        teachers = Teacher.query.all()
    else:
        selected_course = Course.query.filter_by(id=cid).first()
        teachers = selected_course.teachers.all()
    return render_template('/teacherquery.html', courses=courses, teachers=teachers, cid=int(cid))


if __name__ == '__main__':
    # 没有manger时的方法
    # app.run(debug=True)
    # 使用manager启动 避免是哦要嗯
    manager.run()
    # 问题１:指定调试模式(debug=True)
    # 解决方案:app.config['DEBUG']=True

    # 问题2:指定启动的端口(port=xxxx)
    # 解决方案:python3 run01.py runserver --port xxxx

    # 问题3:指定启动的IP地址(host=0.0.0.0)
    # 解决方案:python3 run01.py runserver --host 0.0.0.0

    # 问题2,3:综合解决方案
    # 解决方案:python3 run01.py runserver --host 0.0.0.0 --port 5555

    # python3 run01.py runserver 要写子命令
