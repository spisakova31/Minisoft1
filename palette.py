import tkinter
import random
import math


class Palette:
    class Color:
        def __init__(self, x, y, r, color, canvas, w):
            self.x = x
            self.y = y
            self.r = r
            self.w = w
            self.color = color
            self.canvas = canvas
            self.width = 1

        def draw(self):
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2, outline='black', fill='white', width=self.width)
            self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color, outline=self.color)

        def check(self):
            self.width = 4
            self.draw()

        def uncheck(self):
            self.width = 1
            self.draw()

        def is_clicked(self, click):
            return math.sqrt(((click.x - self.x) ** 2) + ((click.y - self.y) ** 2)) < self.r


    class Eraser:
        def __init__(self, x, y, canvas, image, w):
            self.x = x
            self.y = y
            self.w = w
            self.canvas = canvas
            self.image = image
            self.width = 1

        def draw(self):
            self.canvas.create_rectangle(self.x-self.w/2, self.y-self.w/2, self.x+self.w/2, self.y+self.w/2, outline='black', fill='white', width=self.width)
            self.canvas.create_image(self.x, self.y, image=self.image)

        def is_clicked(self, click):
            return self.x - self.w/2 < click.x and self.x + self.w/2 > click.x and self.y - self.w/2 < click.y and self.y + self.w/2 > click.y

        def check(self):
            self.width = 4
            self.draw()

        def uncheck(self):
            self.width = 1
            self.draw()


    def __init__(self, canvas, count_colors, game, x, y):
        self.colors_palette = ['dimgray', 'brown', 'red', 'salmon', 'orange', 'yellow', 'olive', 'lime', 'green',
                               'turquoise', 'aqua', 'blue', 'navy', 'hotpink', 'indigo', 'fuchsia']
        self.count_colors = count_colors
        self.game = game
        self.canvas = canvas
        self.color = 'white'
        self.colors = random.sample(self.colors_palette, self.count_colors)
        self.colors_objects = []
        self.x = x
        self.y = y
        self.w = 40
        self.h = (self.count_colors + 1) * self.w
        self.gap = 5
        self.color_r = (self.w - 2 * self.gap) / 2
        self.eraserImg = tkinter.PhotoImage(file='eraser.png')
        self.eraser = None
        self.draw_init()

    def draw_init(self):
        x, y = self.x, self.y
        self.colors_objects.clear()
        first = True
        for color in self.colors:
            c = self.Color(x, y, self.color_r, color, self.canvas, self.w)
            if first:
                c.width = 4
                first = False
            self.colors_objects.append(c)
            c.draw()
            y += 2 * self.color_r + 2 * self.gap
        self.eraser = self.Eraser(x, y, self.canvas, self.eraserImg, self.w)
        self.eraser.draw()

    def draw(self):
        for color in self.colors_objects:
            color.draw()
        self.eraser.draw()

    # paleta ma stred na najvrchnejsej farbe v strede...blbost ja viem ale ked som to zistila uz bolo vsetko hotove
    def is_clicked(self, click):
        return self.x - self.w / 2 < click.x and self.x + self.w / 2 > click.x and self.y - (self.color_r + self.gap) < click.y and self.y + self.h - (self.color_r + self.gap) > click.y

    def left_button_clicked(self, click):
        if self.is_clicked(click):
            if self.eraser.is_clicked(click):
                self.game.cursor_color = 'white'
                self.eraser.check()
                for color in self.colors_objects:
                    color.uncheck()
            else:
                for color in self.colors_objects:
                    if color.is_clicked(click):
                        self.game.set_cursor_color(color.color)
                        color.check()
                    else:
                        color.uncheck()
                self.eraser.uncheck()


