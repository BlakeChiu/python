from pyexpat import model
from turtle import width
import matplotlib.pyplot as plt
import matplotlib.image as  mpimg
import numpy as np
import cv2
import time

from keras.models import load_model
model=load_model('my_model.h5')
model.load_weights('my_model_weights.hdf5')

cap=cv2.VideoCapture(0)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d " %(width,height))

while(True):
 tStart = time.time() #計時開始
 ret, img_1 = cap.read() #讀一張照片
 img_2 = img_1[0:480,80:560] #把他變成480x480
 cv2.imshow('Camera',img_2) #放在最左邊的影像
 
 #25~35把正方形的彩色影像變成灰階影像，然後把背景變成黑色，字變成白色，最後變成28x28的影像放在input影像
 img_2_gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
 img_3 = 255 - img_2_gray
 img_3 = img_3.astype('float32')
 img_3_min = np.amin(img_3)
 img_4 = img_3 - np.amin(img_3)
 img_5 = 255 * img_4 / (np.amax(img_4))
 kernel = np.ones((5,5),np.uint8)
 img_6 = cv2.dilate(img_5,kernel,iterations = 3)
 img_7 = cv2.resize(img_6,(28,28),1)
 img_8 = img_6.astype('uint8')
 cv2.imshow('input',img_8) 
 
 x_test_image = np.reshape(img_7, (1,28,28))
 
 # convert 2-D 28x28 image to 4-D nx28x28x1 array
 x_Test4D=x_test_image.reshape(x_test_image.shape[0],28,28,1).astype('float32')
 # normalize the image numbers to 0~1
 x_Test4D_normalize = (x_Test4D / np.amax(x_test_image))
 prediction=np.argmax(model.predict(x_Test4D_normalize),axis=1)

 filename = '%s%d%s' % ('./numbers/number_', prediction, '.jpg')
 img_9 = cv2.imread(filename)
 img_10 = cv2.resize(img_9,(480,480),1)
 cv2.imshow('inference',img_10)
 tEnd = time.time() #計時結束
 
 if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.imwrite('output.jpg', img_2)
    break
cap.release()
cv2.destroyAllWindows()
print('It takes %f sec for each frame' % (tEnd - tStart))