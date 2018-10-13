from tkinter import *
import random

class Palette:

    class Color:

        def __init__(self, x, y, r, color, canvas):
            self.x = x
            self.y = y
            self.r = r
            self.color = color
            self.canvas = canvas

        def draw(self):
            self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)

        def make_bigger(self):
            self.r += 2

        def make_smaller(self):
            self.r -= 2
            

    def __init__(self, canvas, count_colors):
        self.colors_palette = ['black','gray','brown','red','salmon','orange',
                        'yellow','olive','lime','green','turquoise',
                        'aqua','blue','navy','hotpink', 'indigo', 'fuchsia'] 
        self.canvas = canvas
        self.count_colors = count_colors
        self.master = Tk()
        self.master.configure(cursor='dot red')
        self.colors = random.sample(self.colors_palette, self.count_colors)

    def draw(self, x, y):
        canvas = Canvas(self.master, width=250, height=350)
        canvas.pack()
        gap = 5 #medzera medzi gulickami
        paletteColor = 'grey70'
        r = 15 #velkost gulicky
        w = 40 #sirka palety
        h = (r * 2 * (self.count_colors + 3)) + (gap * 2 * (self.count_colors + 3)) + gap
        canvas.create_rectangle(x - w/2, y - w/2, x + w/2, y + h/2, fill=paletteColor)
        y += gap + r - w/2
        
        for color in self.colors:
            c = self.Color(x, y, r, color, canvas)
            c.draw()
            y += 2*r + 2*gap

        eraser = PhotoImage(file='eraser.png')
        label = Label(image=eraser)
        label.place(10,10)
        label.image = eraser # keep a reference!
        label.pack()

    def change_coursor_colour(self, colour):
        ...
 
            


p = Palette('', 3)
p.draw(100,50)
