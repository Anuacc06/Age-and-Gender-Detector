import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import cv2
from keras.models import load_model # type: ignore
model=load_model('Age_Sex_Detection.keras')
model
top=tk.Tk()
top.geometry('800x600')
top.title('Age and Gender Detection')
top.configure(background="#CDCDCD")
label1=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
label2=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
sign_image=Label(top)


def Detect(file_path):
    global Label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=np.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=["Male","Female"]
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print("Predicted Age is"+str(age))
    print("Predicted Gender is"+sex_f[sex])
    label1.configure(foreground="#011638",text=age)
    label2.configure(foreground="#011638",text=sex_f[sex])

def Show_Detect_Button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground="white",font=("arial",10,"bold"))
    Detect_b.place(relx=0.79,rely=0.46)
    return Detect_b

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        Show_Detect_Button(file_path)
    except:
        pass
        
upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#364156",foreground="white",font=("arial",20,"bold"))
upload.pack(side="bottom",pady=50)
sign_image.pack(side="bottom",expand=True)
label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
heading=Label(top,text="Age and Gender Detector",pady=20,font=("arial",20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()