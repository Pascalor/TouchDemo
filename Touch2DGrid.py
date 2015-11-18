from Tkinter import * 
import sys
import math
from Touch2d import Touch2D
from threading import Thread
from time import sleep
from thread import start_new_thread
from Baseline import Baseline
#define a method that will create a thread for each pixel





def fill_pixel(canvas, grid, difference, number):

    #the list of colors that can be filled in
    color = ["#F5F5F5","#DCDCDC","#D3D3D3","#C0C0C0","#A9A9A9","#808080","#696969","#000000"]
       
    display = ""
    #try and dynammically change the bound


    #change this bound value to match wanted sensitivity 
    bound = 75

    print(difference)
    if difference <= bound:
        display = color[0]
    if difference >= bound and difference <= bound + 10:
        display = color[3]
        print("Color 3")
    if difference >= bound + 10 :
        display = color[4]
        print("color 4")
    if difference >= bound+ 125 and difference <= bound + 225:
        display = color[6]    
    if difference >= bound + 225:
        display = color[7]    
    

    grid.color(number = number, color = display)
    canvas.update()
        #sleep(1)



#this method gets the data from the serial port         

def grabdata(pixelnumber, canvas, grid):
    pixellist = []
    baselist = []
    for items in range(pixelnumber):
         pixellist.append(Baseline(target = items, size = 1))   #add it to the size of the pixel list 
         baselist.append(pixellist[items].setbasevalue())   #set the basevalue for each pixel

    print("Baselist ", baselist) # the baseline values 
    while True:
        for count in range(pixelnumber):
            difference = pixellist[count].value()  - baselist[count] #next real value
            #print(difference)
            fill_pixel(canvas = canvas, grid = grid, difference = difference, number = count) #pass to this function to fill 
         


    

def main():
	#create the root 
    root = Tk()
    root.wm_title("PressureDemo")

    #create the canvas 
    canvas_width =  500
    canvas_height = 600  

    #pixel number
    pixel_width =  5
    pixel_height = 6
    

    pixelnumber = pixel_width * pixel_height

    canvas = Canvas(root, width = canvas_width, height = canvas_height)

    #create the grid 


    
    grid = Touch2D(canvas,canvas_width,canvas_width, pixel_height, pixel_width)
    grid.draw()

    


    
    #launch thread for continuously grabbing the data 

    thread = Thread(target = grabdata, args=(pixelnumber,canvas,grid)) 
    thread.daemon = True
    thread.start()


    



    	
    #start the loop
    root.mainloop()


if __name__ == '__main__':
	main()	