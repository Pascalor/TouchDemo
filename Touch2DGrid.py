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
    if difference <= 20:
        display = "white"
    if difference > 20 :
        display = "black"   
    grid.color(number = number, color = display)
    canvas.update()
        #sleep(1)


def main():
	#create the root 
    root = Tk()
    root.wm_title("Touch2D")

    #create the canvas 
    canvas_width = 500
    canvas_height = 600  

    #pixel number
    pixel_height = 6
    pixel_width = 5
    pixelnumber = pixel_width * pixel_height

    canvas = Canvas(root, width = canvas_width, height = canvas_height)

    #create the grid 

    
    grid = Touch2D(canvas,canvas_width,canvas_width, pixel_height, pixel_width)
    grid.draw()
    

    # thread = Thread(target = fill_pixel, args=(canvas , grid , 1)) 
    # thread.daemon = True
    # thread.start()
    

    # thread2 = Thread(target = fill_pixel, args=(canvas , grid , 5)) 
    # thread2.daemon = True
    # thread2.start()
    count = 0
    while True:
        #for drawings in range(pixelnumber):
        reading = Baseline(target = count, size = 1)
        reading.setbasevalue()
        for drawings in range(3):    
            difference = reading.value()
            print(difference)
            fill_pixel(canvas = canvas, grid = grid, difference = difference, number = count)
        

        count += 1
        if count > 29 :
            count = 0


    canvas.update()  


    	
    #start the loop
    root.mainloop()


if __name__ == '__main__':
	main()	