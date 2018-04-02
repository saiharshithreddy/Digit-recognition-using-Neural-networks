
from __future__ import division, print_function, absolute_import

import scipy
import numpy as np
import cv2
from keras.models import model_from_json
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import PIL.ImageOps 

####################################### BROWSE ###########################################
root = Tk() #interface
def  browsefunc():
	global filename 
	ftypes = [('Image file', '.jpg'), ('PNG file', '.png'), ('All files', '*')]
        
	filename = filedialog.askopenfilename(filetypes=ftypes, defaultextension='.jpg')	# stores the path of the file
	global img
	img = cv2.imread(filename,0)
	
	 

 #image is taken as input
f = Frame(root, height=200, width=400, background="white") # a frame is created for GUI
f.pack() # pack is used to display on the screen

browsebutton = Button(f, text="Browse", background="white",fg="black", command=browsefunc) 

browsebutton.pack(side=LEFT) #position of the button

label = Label(root)
label.pack()



##################################### Draw the image #######################################
class ImageGenerator:
    
    def __init__(self,parent,posx,posy,*kwargs):
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 155
        self.sizey = 275
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.drawing_area=Canvas(self.parent,width=self.sizex,height=self.sizey)
        self.drawing_area.place(x=self.posx,y=self.posy)
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
        self.button=Button(self.parent,text="Save",bg='white',command=self.save)
        self.button.pack(side=LEFT)
        self.button1=Button(self.parent,text="Clear",bg='white',command=self.clear)
        self.button1.pack(side=LEFT)
	

        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
###################################################### saving the image ###############################
    def save(self):
      filename2 = filedialog.asksaveasfile()
      self.image.save(filename2)
      ftypes = [('Image file', '.jpg'), ('All files', '*')]
        
      picture = filedialog.askopenfilename(filetypes=ftypes, defaultextension='.jpg')
      col = Image.open(picture)
      col.save("temp.jpg")
      image = Image.open('temp.jpg')

      inverted_image = PIL.ImageOps.invert(image)

      inverted_image.save('result.jpg')
##################################################### clear the paintbox ###############################	    
    def clear(self):
        self.drawing_area.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true',width=7,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,0,0),width=7)

        self.xold = event.x
        self.yold = event.y

if __name__ == "__main__":
   
    root.wm_geometry("%dx%d+%d+%d" % (400, 400, 10, 10))
    root.config(bg='white')
    ImageGenerator(root,1,1)

    
################################## loading model ############################################
def prediction():
	json_file = open('/home/harshith/Desktop/new/lenet_model1.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()

########################## loading weights ###################################################
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("/home/harshith/Desktop/new/lenet_weights1.h5")
	print("Loaded model from disk")
	
########################## loading the image file ############################################

	global img
	img = cv2.resize(img,(28, 28)).astype(np.float32)
	img = np.expand_dims(img, axis=0)
	img = np.expand_dims(img, axis=3)

############################## Prediction ####################################################
	prediction = loaded_model.predict([img])


###################################### printing output #######################################
	global num
	num = np.argmax(prediction)
	print("The predicted number is :")
	print(num)
	
	w = Message(root, background="white", text=num)
	w.pack(side=BOTTOM)
	
	m = Message(root, background="white",text="The predicted number is:")
	m.pack(side=BOTTOM)
	

    	
button = Button(f, text="Prediciton", background= "white", command=prediction)
button.pack(side=LEFT)
quitButton = Button(f, text="Quit", background= "white",fg="red", command=f.quit)
quitButton.pack(side=LEFT)
root.geometry("550x550")
root.mainloop()

