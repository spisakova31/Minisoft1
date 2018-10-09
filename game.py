import tkinter
from ball import Ball, BallIcon
from house import House

class Game:
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.level = 1
        self.score = 0
        self.canvas = tkinter.Canvas(width = self.width, height = self.height, bg='white')
        self.drawPlayground(None)
        self.canvas.pack()

        self.canvas.bind('<Button-1>',self.clicked) # Button-3 – pravé tlačidlo
        tkinter.mainloop()
        
    def drawPlayground(self, task):
        margin_left = 50
##        margin_top = 100

        self.canvas.create_text(self.width//2, 50, font="Times 18", text='ahoj ja som zadanie')
        
        self.user_input = 0 #toto bude asi treba pretypovat na cislo potom
        entry1 = tkinter.Entry(textvariable = self.user_input)
        entry1.place(x=margin_left, y=100, height=30, width = 100)

        self.ok_button = tkinter.Button(text = 'OK?', command = self.check)
        self.ok_button.place(x=margin_left + 105, y=100, height=30)

        self.canvas.create_rectangle(0, self.height, self.width, self.height-30, fill='red')
        self.canvas.create_text(margin_left, self.height - 10, font="Times 18", text=self.level)

    def check(self):
        self.level += 1
        self.reload()
        
    def reload(self):
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='white')
        self.drawPlayground(None)
        self.canvas.pack()

    def clicked(self, event):
        print('klikol ', event)

g = Game()
