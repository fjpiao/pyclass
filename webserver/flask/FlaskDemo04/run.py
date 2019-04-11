from flask import Flask,request,render_template
import datetime
import os
app=Flask(__name__)

@app.route('/01-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        #1.获取前端传递过来的文件
        picture = request.files['picture']
        #2.得到文件名(获取扩展名)  ex:abc.jpg
        ext = picture.filename.split('.')[-1]
        #3.获取当前的时间:YYYYMMDDHHMMSSFFFFFF
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        #4.將时间和扩展名拼接到一起,组成新的文件名
        filename = ftime+'.'+ext
        #5.使用绝对路径将文件上传至　static/upload的目录下
        #/home/tarena/test/fjpiao/webfront/flask
        basedir = os.path.dirname(__file__)
        print('basedir:'+basedir)
        #拼完整的保存路径
        upload_path=os.path.join(basedir,'static/upload',filename)
        picture.save(upload_path)

        # #5.使用相对路径将文件上传至static/upload目录下
        # picture.save('static/upload'+filename)
        return '头像上传成功'
if __name__ == '__main__':
    app.run(debug=True)