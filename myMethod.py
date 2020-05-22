import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


def print_hello():
    print("hello")


def face_recognize(path1, path2):
    images = [cv2.imread(path1, cv2.IMREAD_GRAYSCALE)]
    labels = [1]
    recongnizer = cv2.face.LBPHFaceRecognizer_create()
    recongnizer.train(images, np.array(labels))
    predict_image = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
    label, confidence = recongnizer.predict(predict_image)
    print("label = ", label)
    print("confidence = ", confidence)
    return confidence


def face_recognizes():
    images=[]
    images.append(
        cv2.imread("D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041733.png", cv2.IMREAD_GRAYSCALE))
    images.append(
        cv2.imread("D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041734.png", cv2.IMREAD_GRAYSCALE))
    images.append(
        cv2.imread("D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041735.png", cv2.IMREAD_GRAYSCALE))
    # images.append(cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041734.png", cv2.IMREAD_GRAYSCALE))
    labels = [1, 2, 3]
    recongnizer = cv2.face.LBPHFaceRecognizer_create()
    recongnizer.train(images, np.array(labels))
    predict_image = cv2.imread("D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041732.png",
                               cv2.IMREAD_GRAYSCALE)
    label, confidence = recongnizer.predict(predict_image)
    print("label = ", label)
    print("confidence = ", confidence)


def subtract_time(sign_in_time, local_time):
    str1 = sign_in_time
    str2 = local_time
    arr = [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15]
    time1 = 0
    time2 = 0
    for i in arr:
        time1 = time1 * 10 + int(str1[i])
        time2 = time2 * 10 + int(str2[i])
    return time2 - time1


def send_mail(para_user, para_file_name):
    ret = True
    my_sender = '1909392064@qq.com'  # 发件人邮箱账号
    my_pass = 'this is my authorization code'
    with open('authorizationCode.txt') as file_obj:
        my_pass = file_obj.read()
    my_user = para_user  # 收件人邮箱账号，我这边发送给自己
    try:
        msg = MIMEMultipart()
        msg['From'] = formataddr(["attendance system", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "考勤系统"  # 邮件的主题，也可以说是标题

        msg.attach(MIMEText('附件中是学生考勤记录', 'plain', 'utf-8'))

        att = MIMEText(open(para_file_name, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/oct-stream'
        att["Content-Disposition"] = 'attachment; filename = "T040004.xlsx" '
        msg.attach(att)
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
