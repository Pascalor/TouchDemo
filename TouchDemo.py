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
breakpoint = 15
isPressed = True 
center = ((x + x1) / 2 , (y + y1) / 2)

count = 0 #This can be a list as well per pixle

default = 0.00 # this is the scale value 
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


    if invalue <= 1 and isPressed == False : 
        canvas.delete(id1)
        canvas.pack()
        canvas.update()
        id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
        scale = 0.00
        default = 0.00
        isActive = False 

    elif invalue > 1 and invalue < 2 : 
        scale = 0.1
        isActive = True  
         

    elif invalue >= 2 and invalue <= 25 :
        canvas.itemconfig(id1, fill = "red")
        isActive = False 
        isPressed = True
    
    elif invalue > 25 and invalue < 35 :
        scale = 0.1  
        isActive = True
        

    elif invalue > 35 and invalue < 200 :
        canvas.itemconfig(id1, fill = "red")   
        isActive = False 
        isPressed = True
    
   
    default += scale 
    scale = 0.00
    default /= 2
    default += 1


    print(invalue)
   
     
    if isActive :
        canvas.itemconfig(id1, fill = "red")
        canvas.scale("Circle", center[0] , center[1], default  , default )
        default = 0.00
        scale = 0.00

    canvas.after(delay)
    canvas.update()
    
    #if the count is a modulus of 5 clear circle 

    

    if invalue == 0 :
        count += 1 
        if count == breakpoint : 
            isPressed = False
            count = 0
    # if count % breakpoint == 0 :
         # canvas.delete(id1)
         # canvas.pack()
         # canvas.update()
         # id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
    #      canvas.after(delay)
    #      scale = 0.00
    #      default = 0.01




    

    




root.mainloop()