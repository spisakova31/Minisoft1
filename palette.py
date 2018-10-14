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
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2, outline=self.outline, fill='white')
            self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color, outline=self.color)

        def check(self):
            self.outline = 'green'
            self.draw()

        def uncheck(self):
            self.outline = 'black'
            self.draw()            

        def is_clicked(self, click):
            return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

        def clicked(self, click):
            if self.is_clicked(click):
                return self
            return None

    class Eraser:
        def __init__(self, x, y, canvas, image, w):
            self.x = x
            self.y = y
            self.w = w
            self.canvas = canvas
            self.image = image

        def draw(self):
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2, outline='black', fill='white')
            self.canvas.create_image(self.x, self.y, image=self.image)

        def is_clicked(self, click):
            return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

        def clicked(self, click):
            if self.is_clicked(click):
                return self
            return None

    def __init__(self, canvas, count_colors):
        self.colors_palette = ['black', 'gray', 'brown', 'red', 'salmon', 'orange', 'yellow', 'olive', 'lime', 'green',
                               'turquoise', 'aqua', 'blue', 'navy', 'hotpink', 'indigo', 'fuchsia']
        self.count_colors = count_colors
        self.canvas = canvas
        self.color = 'white'
        self.colors = random.sample(self.colors_palette, self.count_colors)
        self.eraser = None
        self.w = 40
        self.h = (self.count_colors + 1) * self.w
        self.gap = 5
        self.color_r = (self.w - 2 * self.gap) / 2

    def draw(self, x, y):
        for color in self.colors:
            c = self.Color(x, y, self.color_r, color, self.canvas, self.w)
            c.draw()
            y += 2 * self.color_r + 2 * self.gap

        self.eraser = tkinter.PhotoImage(file='eraser.png')
        eraser = self.Eraser(x, y, self.canvas, self.eraser, self.w)
        eraser.draw()

