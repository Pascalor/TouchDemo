from Tkinter import * 
import sys
import math
from Touch2d import Touch2D
from threading import Thread
from time import sleep

#define a method that will create a thread for each pixel

def fill_pixel(canvas, grid, number):
    color = ["#F5F5F5","#DCDCDC","#D3D3D3","#C0C0C0","#A9A9A9","#808080","#696969","#000000"]
    difference = Baseline()
    grid.color(number = number, color = color[difference % len(color)])
    canvas.update()



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
    
    while True:

    	for pixels in range(pixelnumber):
            grid.color(number = pixels, color = "blue")
            canvas.update()
    #start the loop
    root.mainloop()


if __name__ == '__main__':
	main()	