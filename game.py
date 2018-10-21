import tkinter
import random
import time
from ball import Ball, BallIcon
from house import House, HouseIcon
from flag import Flag, FlagIcon
from grid import Grid
from palette import Palette
from task import Task

class Game:
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.level = 1
        self.score = 0
        self.trial = 0
        self.margin_left = 50
        self.user_input = 0
        self.grid = None
        self.edit_num = 0

        self.canvas = tkinter.Canvas(width=self.width, height=self.height, bg='white')
        self.tasks = self.create_tasks()
        self.palette = None
        self.cursor_color = None
        self.load_level()

        self.ok_button = tkinter.Button(text='OK?', command=self.check, bg='springgreen')
        self.entry = tkinter.Entry(textvariable=self.user_input)
        self.entry.pack()
        self.ok_button.pack()

        self.canvas.bind('<Button-1>',self.left_button_clicked) # Button-1 – lave tlačidlo
        self.canvas.bind('<Button-3>',self.right_button_clicked) # Button-3 – pravé tlačidlo

        self.draw_playground()
        self.canvas.pack()
        tkinter.mainloop()

    def draw_footer(self):
        self.canvas.create_rectangle(0, self.height, self.width, self.height-30, fill='grey50', outline='grey50', )
        self.canvas.create_text(self.margin_left, self.height, font="Times 18", text='Level: ' + str(self.level), anchor="sw")
        self.canvas.create_text(self.width - 150, self.height, font='Times 18', text='Score: ' + str(self.score), anchor="sw")
    
    def draw_playground(self):
        self.draw_footer()
        self.canvas.create_rectangle(0, 0, self.width, 135, fill='peachpuff', outline='salmon')
        self.canvas.create_text(self.margin_left, 70, font="Times 16", text=self.tasks[self.level-1].get_text(), anchor="sw")
        self.entry.place(x=self.margin_left, y=100, height=30, width = 100)
        self.ok_button.place(x=self.margin_left + 105, y=100, height=30)
        self.canvas.create_rectangle(0, 135, self.width, self.height - 30, fill='grey97', outline='grey97')
        self.grid.draw(self.canvas)
        self.palette.draw()

    def check(self):
        self.trial += 1
        print(str(self.entry.get()) + ' = ' + str(self.tasks[self.level-1].get_result()))
        result = self.tasks[self.level-1].get_result()
        if self.entry.get() == str(result):
            self.level += 1
            if self.trial == 1:
                self.score += 1
            if self.level > 8:
                self.game_done()
            else:
                self.canvas.create_text(self.margin_left + 105 + 50, 130, font="Times 18",
                                        text='SUPER', anchor="sw", fill='green')
                self.canvas.after(1000)
                # time.sleep(1000)
                self.trial = 0
                self.load_level()
                self.entry.delete(0, 'end')
                self.reload()

        else:
            self.trial += 1
            self.canvas.create_text(self.margin_left + 105 + 50, 130, font="Times 18", text='NESPRÁVNE :( SKÚS TO EŠTE RAZ', anchor="sw", fill='red')

    def reload(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='white')
        self.draw_playground()
        self.canvas.pack()
        self.entry.delete(0, 'end')
        self.entry.insert(0, self.grid.get_number_of_colored())

    def left_button_clicked(self, event):
        self.grid.left_button_clicked(event)
        self.palette.left_button_clicked(event)
        self.reload()

    def right_button_clicked(self, event):
        self.grid.right_button_clicked(event)
        self.reload()
        
    def get_canvas(self):
        return self.canvas

    def get_coursor_color(self):
        return self.cursor_color

    def set_cursor_color(self, color):
        self.cursor_color = color

    def create_tasks(self):
        tasks = list()
        tasks.append(Task(1, 'Ball', random.randint(1, 4)))
        tasks.append(Task(2, 'Ball', random.randint(4, 6)))
        tasks.append(Task(3, 'House', 2))
        tasks.append(Task(4, 'House', 3))
        tasks.append(Task(5, 'Flag', 2))
        tasks.append(Task(6, 'Flag', 3))
        tasks.append(Task(7, 'House', random.randint(4, 5)))
        tasks.append(Task(8, 'Flag', random.randint(4, 5)))
        return tasks

    def load_level(self):
        self.grid = Grid(50, 220, 800, 280, self.tasks[self.level - 1].get_obj(), self)
        self.palette = self.palette = Palette(self.canvas, self.tasks[self.level-1].get_count_colors(), self, self.width - 80, self.height / 2 - 40)
        self.cursor_color = self.cursor_color = self.palette.colors[0]

    def game_done(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='palegreen')
        self.entry.destroy()
        self.ok_button.destroy()
        self.canvas.create_text(self.width / 2, self.height / 2, font="Times 25",
                                text='Podarilo sa ti úspešne prejsť všetky levely :)\n Na prvý pokus sa ti podarilo splniť ' + str(
                                    self.score) + ' levelov.')

    def increase_edit(self):
        print('som tu. edit = ' + str(self.edit_num))
        print('pretyp: ' + str(int(self.edit_num)))
        self.edit_num = int(self.edit_num) + 1
        print('po pripocitani 1: ' + str(self.edit_num))
        self.entry.delete(0, 'end')
        self.entry.insert(0, self.edit_num)

    def decrease_edit(self):
        self.edit_num = int(self.edit_num) - 1
        self.entry.delete(0, 'end')
        self.entry.insert(0, self.edit_num)

g = Game()
a = input()
