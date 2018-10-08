import tkinter

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.level = 1
        self.score = 0
        self.canvas = tkinter.Canvas(width = self.width, height = self.height)
        self.drawPlayground(None)
        self.canvas.pack()

    def drawPlayground(self, task):
        vstup = 'tu pisem' #pozriet syntax pre input
        entry1 = tkinter.Entry(textvariable = vstup)
        entry1.pack()

        self.ok_button = tkinter.Button(text = 'OK?',
                           command = self.check)
        self.ok_button.pack()

    def check(self):
        ...



g = Game()
