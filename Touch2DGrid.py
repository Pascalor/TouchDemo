from Tkinter import * 
import sys
import math
from Touch2d import Touch2D


def main():
	#create the root 
    root = Tk()
    root.wm_title("Touch2D")

    #create the canvas 
    canvas_width = 500
    canvas_height = 600  


    canvas = Canvas(root, width = canvas_width, height = canvas_height)

    #create the grid 

    
    grid = Touch2D(canvas,canvas_width,canvas_width, 6, 5)
    grid.draw()
    grid.color(number = 0, color = "red")

    #start the loop
    root.mainloop()


if __name__ == '__main__':
	main()	