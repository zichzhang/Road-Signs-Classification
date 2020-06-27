# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:48:11 2020

@author: zi chao
"""

import numpy as np
import pandas as pd 
import tensorflow as tf
#import cv2
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout


data = []
labels = []
classes = 43

# retrieving images and labels
for i in range(classes):
    print('loading class ' + str(i+1) + '...')
    current_path = os.getcwd()
    path = os.path.join(current_path,'Train',str(i))
    images = os.listdir(path)

    for im in images:
        try:
            image = Image.open(path + '/' + im)
            image = image.resize((30,30))
            image = np.array(image)
            data.append(image)
            labels.append(i)
        except: 
            print('Error: image cannot load')

# storing all image data and labels into arrays
data = np.array(data)
labels = np.array(labels)

print(data.shape, labels.shape)
# splitting train and test data
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=21)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# converting labels to one-hot encoding
y_train = to_categorical(y_train, 43)
y_test = to_categorical(y_test, 43)

# building convolutional neural network
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=(30,30,3)))
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(rate=0.25))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(43, activation='softmax')) #output

# creating the loss function
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# fitting the model
model.fit(X_train, y_train, batch_size=32, epochs=15, validation_data=(X_test, y_test))

# save the model
model.save('./model')




    
    

  