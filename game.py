import tkinter
from ball import Ball, BallIcon
from house import House, HouseIcon
from flag import Flag, FlagIcon
from grid import Grid

class Game:
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.level = 1
        self.score = 0


        self.margin_left = 50
        self.canvas = tkinter.Canvas(width = self.width, height = self.height, bg='white')

        self.grid = Grid(50, 220, 800, 280, 'b', self)
        self.user_input = 0
        

        self.draw_playground(None)
        self.canvas.pack()

        self.canvas.bind('<Button-1>',self.left_button_clicked) # Button-1 – lave tlačidlo
        self.canvas.bind('<Button-3>',self.right_button_clicked) # Button-3 – pravé tlačidlo

        tkinter.mainloop()

    def draw_footer(self):
        self.canvas.create_rectangle(0, self.height, self.width, self.height-30, fill='red')
        self.canvas.create_text(self.margin_left, self.height - 10, font="Times 18", text=self.level)
    
    def draw_playground(self, task):
        self.draw_footer()
        self.canvas.create_text(self.width//2, 50, font="Times 18", text='ahoj ja som zadanie')
        
         #toto bude asi treba pretypovat na cislo potom
        entry1 = tkinter.Entry(textvariable = self.user_input)
        entry1.place(x=self.margin_left, y=100, height=30, width = 100)

        self.ok_button = tkinter.Button(text = 'OK?', command = self.check)
        self.ok_button.place(x=self.margin_left + 105, y=100, height=30)

        self.grid.draw(self.canvas)

    def check(self):
        self.level += 1
        self.reload()
        
    def reload(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='white')
        self.draw_playground(None)
        self.canvas.pack()

    def left_button_clicked(self, event):
        self.grid.left_button_clicked(event)
        #tu este bude volanie pre kliknutie do palety farieb
        self.reload()

    def right_button_clicked(self, event):
        self.grid.right_button_clicked(event)
        self.reload()
        
    def get_canvas(self):
        return self.canvas

    def get_coursor_color(self):
        #tento return bude vracat aktualne zvolenu farbu kurzora
        return 'red'

g = Game()
