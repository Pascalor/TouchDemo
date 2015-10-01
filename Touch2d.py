from Tkinter import * 
import sys
import math

class Touch2D:
    #constructor
    def __init__(self, canvas, canvas_width, canvas_height, rowmax, columnmax):

        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.pixel_count = int(rowmax) * int(columnmax)
        self.rowmax = int(rowmax)
        self.columnmax = int(columnmax)
        self.pixels = []

    def draw(self):
        #this method creates the rectangles 
        side = math.sqrt((self.canvas_width * self.canvas_height)/self.pixel_count) #the side length of each pixel

        xbound = side * self.columnmax
        ybound = side * self.rowmax
        origin = 0
        x = origin
        y = origin
        x2 = side 
        y2 = side 


        for element in range(self.pixel_count):

            #check to see for row boundary 

            if y == ybound:
                y = origin
                y2 = side #restart the row
                x += side 
                x2 += side
                #column += side #next column

            id1 = self.canvas.create_rectangle(x, y, x2, y2, fill = "white", outline = "black") #create the pixel
            canvas.update()
            canvas.grid()
            self.pixels.append(id1) #add to the pixel list 
            y2 += side
            y += side #move to the next row
            
            

if __name__ == '__main__':
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

    
    #start the loop
    root.mainloop()

