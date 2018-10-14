from game import Game
import tkinter
import random

class Palette:

    class Color:

        def __init__(self, x, y, r, color, canvas, w):
            self.x = x
            self.y = y
            self.r = r
            self.w = w
            self.color = color
            self.canvas = canvas
            self.outline = 'black'

        def draw(self):
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2,outline=self.outline)
            self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color,outline=self.color)

        def check(self):
            self.outline = 'green'
            self.draw()

        def unheck(self):
            self.outline = 'black'
            self.draw()            

        def click(self, x, y):
            ...
            

    class Eraser:
        def __init__(self, x, y, canvas, image, w):
            self.x = x
            self.y = y
            self.w = w
            self.canvas = canvas
            self.image = image

        def draw(self):
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2,outline='black')
            self.canvas.create_image(self.x,self.y,image=self.image)   

    def __init__(self, canvas, count_colors):
        self.colors_palette = ['black','gray','brown','red','salmon','orange',
                        'yellow','olive','lime','green','turquoise',
                        'aqua','blue','navy','hotpink', 'indigo', 'fuchsia']
        self.game = Game()
        self.count_colors = count_colors
        self.colors = random.sample(self.colors_palette, self.count_colors)
        self.eraser = None

    def draw(self, x, y):
        gap = 5 #medzera medzi gulickami
        paletteColor = 'grey70'
        r = 15 #velkost gulicky
        w = 40 #sirka palety
        h = (r * 2 * (self.count_colors + 4)) + (gap * 2 * (self.count_colors + 3)) + gap
        self.game.canvas.create_rectangle(x - w/2, y - w/2, x + w/2, y + h/2, fill=paletteColor)
        y += gap + r - w/2
        
        for color in self.colors:
            c = self.Color(x, y, r, color, self.game.canvas, w)
            c.draw()
            y += 2*r + 2*gap
        
        self.eraser = tkinter.PhotoImage(file='eraser.png')
        eraser = self.Eraser(x,y,self.game.canvas,self.eraser,w)
        eraser.draw()

    def change_coursor_colour(self, colour):
        ...
 
p = Palette('', 3)
p.draw(400,200)
