#(1)匯入套件
from statistics import mode
from turtle import title
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(3)

#(2)匯入資料
from keras.datasets import mnist
(x_train_image,y_train_label),(x_test_image,y_test_label)=mnist.load_data()

#(3)convert 2-D 28x28 image to 4-D nx28x28x1 array
X_Train4D=x_train_image.reshape(x_train_image.shape[0],28,28,1).astype('float32')
x_Test4D=x_test_image.reshape(x_test_image.shape[0],28,28,1).astype('float32')

#normalize the image numbers to 0~1
X_Train4D_normalize=X_Train4D/255
x_Test4D_normalize=x_Test4D/255
print(X_Train4D_normalize.shape) #(60000, 28, 28, 1)
print(x_Test4D_normalize.shape)  #(10000, 28, 28, 1)

#(4)convert label numbers to one-hot encoding
y_TrainOneHot=np_utils.to_categorical(y_train_label)
y_TestOneHot=np_utils.to_categorical(y_test_label)
print(y_TrainOneHot.shape) #(60000, 10) 
print(y_TestOneHot.shape)  #(60000, 10) 

#(5)Use a Convolutional Neural Network
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D

model=Sequential()
model.add(Conv2D(filters=16,
                 kernel_size=(5,5),
                 padding='same',
                 input_shape=(28,28,1),
                 activation='relu'))
#以下43~49是額外增加的
model.add(MaxPooling2D(pool_size=(2,2))) #4個找最大值，有這個可以降維度1/4
model.add(Conv2D(filters=36,
                 kernel_size=(5,5),
                 padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2))) #4個找最大值，有這個可以降維度1/4，另外跟上面就是1/16<備註他是相乘的>
model.add(Dropout(0.25))
model.add(Flatten())
#以下52~53也是額外增加的
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))
print(model.summary())

#(6)Model training
#編譯，設定損失函數、優化器、指標
model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=['acc']) #注意metrics[]舊版是acc 新版是accuracy

train_history=model.fit(x=X_Train4D_normalize,
                        y=y_TrainOneHot,validation_split=0.2,
                        epochs=50,batch_size=300,verbose=2)

#(7)Training history
def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()

show_train_history(train_history,'acc','val_acc')
show_train_history(train_history,'loss','val_loss')

#(8)Accuracy
score=model.evaluate(x_Test4D_normalize,y_TestOneHot)
print('accuracy=',score[1])

#(9)Prediction
prediction=np.argmax(model.predict(x_Test4D_normalize),axis=1)

# prediction=model.predict(x_Test4D_normalize)
# prediction=np.round(prediction).astype(float) 另一種寫法跟73一起，label和數字還是擠成一團

# prediction=(model.predict(x_Test4D_normalize)>0.5).astype("int32") label和數字還是擠成一團

# prediction=model.predict_classes(x_Test4D_normalize) 2021被遺棄的寫法

def plot_images_labels_prediction(images,labels,prediction,idx,num=10):
    fig=plt.gcf()
    fig.set_size_inches(12,14)
    if num>25:num=25
    for i in range(0,num):
        ax=plt.subplot(5,5,1+i)
        ax.imshow(images[idx],cmap='binary')
        title="label="+str(labels[idx])
        if len(prediction)>0:
            title+=",predict="+str(prediction[idx])
        
        ax.set_title(title,fontsize=10)
        ax.set_xticks([]);ax.set_yticks([])
        idx+=1
    plt.show()

plot_images_labels_prediction(x_test_image,y_test_label,
                              prediction,idx=320)

#(10)Confusion matrix
df=pd.crosstab(y_test_label,prediction,
            rownames=['label'],colnames=['predict'])
print(df)