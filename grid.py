from ball import Ball, BallIcon
from house import House, HouseIcon
from flag import Flag, FlagIcon

class Grid:
    def __init__(self, x, y, w, h, o_type, game):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.game = game #instancia game

        self.r = 2
        self.c = 4
        
        self.o_type = o_type
        self.o_w = self.w // self.c #vyska objektov
        self.o_h = self.h // self.r #sirka objektov


        self.objects = []

        if self.o_type == 'b':
            self.icon = BallIcon(self.x, self.y, self.o_w, self.o_h, 0, 0)
        if self.o_type == 'h':
            self.icon = HouseIcon(self.x, self.y, self.o_w, self.o_h, 0, 0)
        if self.o_type == 'f':
            self.icon = FlagIcon(self.x, self.y, self.o_w, self.o_h, 0, 0)

        self.addObject()
        
    def draw(self, canvas):
        for object_o in self.objects:
            object_o.draw(canvas)

        self.icon.draw(canvas)

    def addObject(self):
        r, c = self.icon.r, self.icon.c
        if self.o_type == 'b':
            self.objects.append(Ball(self.x, self.y, self.o_w, self.o_h, r, c))

        if self.o_type == 'h':
            self.objects.append(House(self.x, self.y, self.o_w, self.o_h, r, c))

        if self.o_type == 'f':
            self.objects.append(Flag(self.x, self.y, self.o_w, self.o_h, r, c))

        self.icon.increase_c()
        if (self.icon.c >= self.c):
            self.recalculate_after_add()
            self.set_new_positions()

    def set_new_positions(self):
        self.o_w = (self.w - self.icon.get_gap()*self.c) // self.c #vyska objektov
        self.o_h = self.h // self.r #sirka objektov

        pr, pc = 0, 0

        for obj in self.objects:
            obj.set_position(self.o_w, self.o_h, pr, pc)
            pc +=1
            if (pc == self.c):
                pc = 0
                pr += 1

        self.icon.set_position(self.o_w, self.o_h, pr, pc)
        
    def recalculate_after_add(self):
        if self.icon.r < self.r - 1 and self.icon.get_y_top_down_point() <= self.y + self.h:
            self.icon.increase_r()
        else:
            self.r += 1
            self.c += 1
            
            
    def recalculate_after_pop(self):
        if self.icon.c < 0:
            self.icon.r -= 1
            self.icon.c = self.c -1

        if (self.c - 1) * (self.r - 1) > len(self.objects):
            if self.c >= 5 and self.r > 2:
                self.c -= 1
                self.r -= 1

    def left_button_clicked(self, click):
        #ak bolo kliknute na ikonu
        if self.icon.is_clicked(click):
            self.addObject()
            return

        #ak bolo kliknute na niektory objekt
        for obj in self.objects:
            if obj.is_clicked(click):
                obj.clicked(click).set_color(self.game.get_coursor_color())

    def right_button_clicked(self, event):
        for i in range(0, len(self.objects)):
            if (self.objects[i].is_clicked(event)):
                self.objects.pop(i)
                self.icon.decrease_c()
                self.recalculate_after_pop()
                if len(self.objects) == 0:
                    self.addObject()
                    self.recalculate_after_add()
                self.set_new_positions()
                return
                    
