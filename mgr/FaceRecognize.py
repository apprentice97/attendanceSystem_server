import cv2
import numpy as np

images=[]
images.append(cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041733.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041734.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041735.png", cv2.IMREAD_GRAYSCALE))
#images.append(cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041734.png", cv2.IMREAD_GRAYSCALE))
labels = [1, 2, 3]
recongnizer = cv2.face.LBPHFaceRecognizer_create()
recongnizer.train(images, np.array(labels))
predict_image = cv2.imread("D:\\zuoye\\python\\attendanceSystem\\picture\\received\\B16041732.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recongnizer.predict(predict_image)
print("label = ", label)
print("confidence = ", confidence)