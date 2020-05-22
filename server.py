#-*-coding:utf-8-*-
from flask import Flask
from flask import request
import cv2
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def test():
    return '服务器正常运行'

#此方法接收图片
@app.route('/upload',methods=['POST'])
def upload():
    f = request.files['file']
    print('连接成功')
   # 当前文件所在路径
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join(basepath, "C:\\Users\\19093\\Desktop\\", secure_filename(f.filename))
    # 保存文件
    f.save(upload_path)
    return '保存成功'

if __name__ == '__main__':
    app.run(host='0.0.0.0')