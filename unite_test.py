import os
import myMethod

def run():
    print("hello\nworld")


if __name__ == '__main__':
    path1 = "D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041732.png"
    path2 = "D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041734.png"
    myMethod.face_recognize(path1, path2)
