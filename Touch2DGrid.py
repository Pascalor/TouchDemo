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

    color = ["#F5F5F5","#DCDCDC","#D3D3D3","#C0C0C0","#A9A9A9","#808080","#696969","#000000"]
       
    display = ""
    bound = 225
    if difference <= bound:
        display = color[0]
    if difference >= bound + 25 and difference <= bound + 50:
        display = color[2]
    if difference >= bound  :
        display = color[3]
    if difference >= bound + 50 and difference <= bound + 100:
        display = color[7]    
    

    grid.color(number = number, color = display)
    canvas.update()
        #sleep(1)

def grabdata(pixelnumber, canvas, grid):
    pixellist = []
    baselist = []
    for items in range(pixelnumber):
         pixellist.append(Baseline(target = items, size = 1))
         baselist.append(pixellist[items].setbasevalue())

    print("Baselist ", baselist) # the baseline values 
    while True:
        for count in range(pixelnumber):
            difference = pixellist[count].value()  - baselist[count]
            print(difference)
            fill_pixel(canvas = canvas, grid = grid, difference = difference, number = 1)
         


def createbaseline(pixelnumber):
    pixellist = []
    for items in range(pixelnumber):
         pixellist.append(Baseline(target = items, size = 1))
         pixellist[items].setbasevalue()
    return pixellist     

def main():
	#create the root 
    root = Tk()
    root.wm_title("Touch2D")

    #create the canvas 
    canvas_width =  500
    canvas_height = 600  

    #pixel number
    pixel_height = 6
    pixel_width =  5
    pixelnumber = pixel_width * pixel_height

    canvas = Canvas(root, width = canvas_width, height = canvas_height)

    #create the grid 

    
    grid = Touch2D(canvas,canvas_width,canvas_width, pixel_height, pixel_width)
    grid.draw()
    

    thread = Thread(target = grabdata, args=(pixelnumber,canvas,grid)) 
    thread.daemon = True
    thread.start()
    

    # canvas.update()  


    	
    #start the loop
    root.mainloop()


if __name__ == '__main__':
	main()	