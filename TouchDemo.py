from Tkinter import * 
from random import randint
import time
import serial 


root = Tk()
root.wm_title("TouchDemo")
#The code for the rest of the gui will go here 

canvas_height = 500 #canvas height and width 
canvas_width = 500


#create a list for the number of pixles 

isActive = False

x = 100
y = 140
x1 = 50
y1 = 90
delay = 50
breakpoint = 25

center = ((x + x1) / 2 , (y + y1) / 2)

count = 0 #This can be a list as well per pixle

default = 0.05 # this is the scale value 
scale = int()
canvas = Canvas(root, height = canvas_height, width = canvas_width) #create the canvas 
id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
canvas.pack()

while True : 
    #create a circle everyloop then make it grow 
    
    ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
    trash = ser.readline()
    value = ser.readline()
    #id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
    
    #check for non integer character and ignore it 
    
    #ignore non string chars 

    if '_______\r\n' in value :
        value = value.replace('_______\r\n', '0')



    if 'A\r\n' in value :
        value = value.replace('A\r\n', '0')

   
    invalue = int(value.strip(''))
    

    #set some boundaries
    isActive = False


    if invalue <= 1 : 
        #canvas.itemconfig(id1, fill = "white") 
        scale = 0.00
        default = 0.00
        isActive = False 

   # elif invalue     

    elif invalue > 5 : 
        scale = 0.01
        isActive = True
    elif invalue > 25 :
        scale = 0.025  
        isActive = True
    elif invalue > 125 :
        scale = .05     
        isActive = True 

    
   
    default += scale 
    
    default /= 2

    default += 1


    print(invalue)
   
     
    if isActive :
        canvas.scale("Circle", center[0] , center[1], default  , default )
        canvas.itemconfig(id1, fill = "red")

    canvas.after(delay)
    canvas.update()
    
    #if the count is a modulus of 5 clear circle 

    

    count += 1 

    if count % breakpoint == 0 :
         canvas.delete(id1)
         canvas.pack()
         canvas.update()
         id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
         canvas.after(delay)
         scale = 0.00
         default = 0.01




    

    




root.mainloop()