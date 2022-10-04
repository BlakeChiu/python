# from nis import cat
from base64 import encode
from tkinter import font
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose
from keras.models import Model
from keras.preprocessing import image

cat_train_path="./input/cat-and-dog/training_set/cats/"
cat_test_path="./input/cat-and-dog/test_set/cats/"

cat_train=[]
for filename in os.listdir(cat_train_path):
    if filename.endswith(".jpg"):
        img=image.load_img(cat_train_path+filename,target_size=(128,128))
        cat_train.append(image.img_to_array(img))
cat_train=np.array(cat_train)

cat_test=[]
for filename in os.listdir(cat_test_path):
    if filename.endswith(".jpg"):
        img=image.load_img(cat_test_path+filename,target_size=(128,128))
        cat_test.append(image.img_to_array(img))
cat_test=np.array(cat_test)

print("cat_train",cat_train.shape)
print("cat_test",cat_test.shape)

#Visualize the cats
def show_cat_data(X,n=10,title=""):
    plt.figure(figsize=(15,5))
    for i in range(n):
        ax=plt.subplot(2,n,i+1)
        plt.imshow(image.array_to_img(X[i]))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.suptitle(title,fontsize=20)

show_cat_data(cat_train,title="train cats")
show_cat_data(cat_test,title="test cats")

#Build the cat Autoencoder
input_layer = Input(shape=(128, 128, 3), name="INPUT")
x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_layer)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)

code_layer = MaxPooling2D((2, 2), name="CODE")(x)

x = Conv2DTranspose(8, (3, 3), activation='relu', padding='same')(code_layer)
x = UpSampling2D((2, 2))(x)
x = Conv2DTranspose(8, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2DTranspose(16, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2,2))(x)
output_layer = Conv2D(3, (3, 3), padding='same', name="OUTPUT")(x)

cat_AE = Model(input_layer, output_layer)
cat_AE.compile(optimizer='adam', loss='mse')
cat_AE.summary()

# Train the cat Autoencoder
cat_AE.fit(cat_train, cat_train,
                epochs=30,
                batch_size=32,
                shuffle=True,
                validation_data=(cat_test, cat_test))

#Save model
cat_AE.save("cat_AE.h5")

#Make a model to get the encoded representation (i.e. intermediate layer output) for a given cat image.
get_encoded_cat = Model(inputs=cat_AE.input, outputs=cat_AE.get_layer("CODE").output)

#Get the encoded cats
encoded_cat=get_encoded_cat.predict(cat_test)
encoded_cat = encoded_cat.reshape((len(cat_test), 16*16*8))
encoded_cat.shape

#Get the reconstructed cats
reconstructed_cats = cat_AE.predict(cat_test)

#Visualize the results on test set
def show_data(X, n=10, height=28, width=28, title=""):
    plt.figure(figsize=(10, 3))
    for i in range(n):
        ax = plt.subplot(2,n,i+1)
        plt.imshow(X[i].reshape((height,width)))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.suptitle(title, fontsize = 20)
    
show_cat_data(cat_test, title="original cats")
show_data(encoded_cat, height=32, width=64, title="encoded cats")
show_cat_data(reconstructed_cats, title="reconstructed cats")