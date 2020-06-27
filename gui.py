# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:43:26 2020

@author: zi chao
"""

import tkinter as tk
from tkinter import *
import PIL
import numpy as np
from keras.models import load_model

# loading saved model
model = load_model('./model')

# dictionary of all road sign class
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

# initializing GUI
root = Tk()
root.geometry(('800x600'))
root.title('Road Signs Classification')
root.configure(background='#CDCDCD')
label = Label(root, background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(root)

# classifying uploaded image to classes
def classify(file_path):
    image = PIL.Image.open(file_path)
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    prediction = model.predict_classes([image])[0]
    sign = classes[prediction+ 1]
    print(sign)
    label.configure(foreground='#011638', text=sign)

# creating classify button
def classifyButton(file_path):
    classify_button = Button(root, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_button.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_button.place(relx=0.79, rely=0.46)

# opening file explorer and uploading image to GUI
def uploadImage():
    try:
        file_path = tk.filedialog.askopenfilename()
        uploaded=PIL.Image.open(file_path)
        uploaded.thumbnail(((root.winfo_width()/2.25),(root.winfo_height()/2.25)))
        im=PIL.ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        classifyButton(file_path)
    except:
        pass

# creating upload button
upload = Button(root,text="Upload an image",command=uploadImage,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(root, text="Know Your Road Signs",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
root.mainloop()


    
    
