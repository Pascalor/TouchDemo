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
delay = 25
breakpoint = 25
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
    
    ser = serial.Serial("/dev/tty.usbmodem0E20E711", 9600)
    value = ser.readline()
    #id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
    
    #check for non integer character and ignore it 
    
    #ignore non string chars 

    value = value.split()
    try:   
        invalue = int(value[0])
    except IndexError:
        continue    
    
    print(invalue)

    #set some boundaries
    isActive = False
     

    touchbound = 30 #this will be the touch boundary 



    if invalue <= touchbound and isPressed == False : 
        canvas.delete(id1)
        canvas.pack()
        canvas.update()
        id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
        scale = 0.00
        default = 0.00
        isActive = False 

    elif invalue > touchbound  and invalue < touchbound + 5 : 
        scale = 0.1
        isActive = True  
   
    elif invalue >= touchbound + 5 and invalue <= touchbound + 10 :
        canvas.itemconfig(id1, fill = "red")
        isActive = True 
        isPressed = True
        #needs to switch invalue in here 
        
    elif invalue > touchbound + 10 and invalue < touchbound + 20 :
        scale = 0.1
        isActive = True

    elif invalue > touchbound + 20 and invalue < 100 :
        canvas.itemconfig(id1, fill = "red")   
        isActive = True 
        isPressed = True
    
   
    
   
    default += scale 
    scale = 0.00
    default /= 2
    default += 1


   
   
     
    if isActive :
        canvas.itemconfig(id1, fill = "red")
        canvas.scale("Circle", center[0] , center[1], default  , default )
        default = 0.00
        scale = 0.00

    canvas.after(delay)
    canvas.update()

    

    if invalue < 10 :
        count += 1 
        if count == breakpoint : 
            isPressed = False
            count = 0


root.mainloop()



def scale_set(invalue, newscale) :
    isActive = False
    isPassed = False # flag for being passed 


    if invalue <= 1 and isPressed == False : 
        canvas.delete(id1)
        canvas.pack()
        canvas.update()
        id1 = canvas.create_oval(x, y, x1, y1, tag = "Circle" , fill = "white", outline = "white")
        scale = 0.00
        default = 0.00
        isActive = False 

    elif invalue > 1 and invalue < 2 : 
        scale = newscale
        isActive = True  
   
    elif invalue >= 2 and invalue <= 25 :
        canvas.itemconfig(id1, fill = "red")
        isActive = False 
        isPressed = True
        
    elif invalue > 25 and invalue < 35 :
        scale = newscale
        isActive = True

    elif invalue > 35 and invalue < 200 :
        canvas.itemconfig(id1, fill = "red")   
        isActive = False 
        isPressed = True
         
    
   
    default += scale 
    scale = 0.00
    default /= 2
    default += 1


    # print(invalue)
   
     
    if isActive :
        canvas.itemconfig(id1, fill = "red")
        canvas.scale("Circle", center[0] , center[1], default  , default )
        default = 0.00
        scale = 0.00

    canvas.after(delay)
    canvas.update()

    if invalue == 0 or invalue == 1 :
        count += 1 
        if count == breakpoint : 
            isPressed = False
            count = 0
    return
