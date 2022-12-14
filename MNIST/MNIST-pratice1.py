import numpy as np 
import pandas as pd 
from keras.utils import np_utils
np.random.seed(10)

# 匯入資料
from keras.datasets import mnist
(x_train_image,y_train_label),(x_test_image,y_test_label)=mnist.load_data()
print('train data= ',len(x_train_image))
print('test data=', len(x_test_image))

#======================================================
#把影像畫出來
import matplotlib.pyplot as plt 
# 建立函數要來畫多圖的
def plot_images_labels_prediction(images,labels,prediction,idx,num=10): 

    # 設定顯示圖形的大小
    fig= plt.gcf()
    fig.set_size_inches(12,14)

    # 最多25張
    if num>25:num=25

    # 一張一張畫
    for i in range(0,num):
        ax=plt.subplot(5,5,i+1) # 建立子圖形5*5(五行五列)

        # 畫出子圖形
        ax.imshow(images[idx],cmap='binary')

        # 標題和label
        title="label=" +str(labels[idx])

        # 如果有傳入預測結果也顯示
        if len(prediction)>0:
            title+=",predict="+str(prediction[idx])

        # 設定子圖形的標題大小
        ax.set_title(title,fontsize=10)

        # 設定不顯示刻度
        ax.set_xticks([]);ax.set_yticks([])  
        idx+=1
    plt.show()  

plot_images_labels_prediction(x_train_image,y_train_label,[],0,10)