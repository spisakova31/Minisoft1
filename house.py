from math import tan, radians

class Roof:
    def __init__(self, x, y, w, h, color='white', border='black'):
        self.set_position(x, y, w, h)
        
        self.color = color
        self.border = border
        self.angle = 40

    def is_clicked(self, click):
        c_x = click.x
        if c_x > self.x + self.w/2:
            vzbodu = c_x - (self.x + self.w/2)
            c_x = self.x + self.w/2 - vzbodu
        side_w = c_x - (self.x)
        v = abs(tan(radians(self.angle))) * (side_w)
        return self.x < click.x and self.x + self.w > click.x and self.y - v < click.y and self.y > click.y

    def draw(self, canvas):
        v = abs(tan(radians(self.angle))) * (self.w/2)
        canvas.create_polygon(self.x, self.y, self.x + self.w/2, self.y - v, self.x + self.w, self.y, fill = self.color, outline = self.border)

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def is_colored(self):
        return self.color != 'white'

    def equals(self, other):
        return self.color == other.color
        
# ---------------------------------------------------------------------------------------------------------------

class Wall:
    def __init__(self, x, y, w, h, color='white', border='black'):
        self.angle = 40
        self.set_position(x, y, w, h)
        
        
        self.color = color
        self.border = border

    def is_clicked(self, click):
        return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.border)

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y, w, h):
        self.margin = w //6
        self.x = x + self.margin
        self.y = y 
        self.w = w - 2*self.margin
        self.h = h - abs(tan(radians(self.angle))) * (w/2)

    def is_colored(self):
        return self.color != 'white'

    def equals(self, other):
        return self.color == other.color

# -----------------------------------------------------------------------------------------------------------------------------        

class House:
    def __init__(self, grid_x, grid_y, w, h, r, c, wall_color='white', roof_color='white', border='black'):
        self.gap = 10
        self.grid_x, self.grid_y = grid_x, grid_y
        self.w, self.h = w, w
        
        self.r, self.c = r, c
        self.x, self.y = self.grid_x + self.c*self.w + self.c*self.gap, self.grid_y + self.r*self.h + self.r*self.gap

        self.wall = Wall(self.x, self.y, self.w, self.h, wall_color, border)
        self.roof = Roof(self.x, self.y, self.w, self.h, roof_color, border)

    def clicked(self, click):
        if self.wall.is_clicked(click):
            return self.wall
        if self.roof.is_clicked(click):
            return self.roof
        return None

    def is_clicked(self, click):
        return self.wall.is_clicked(click) or self.roof.is_clicked(click)

    def draw(self, canvas):
        self.wall.draw(canvas)
        self.roof.draw(canvas)

    def set_position(self, w, h, r, c):
        self.w, self.h = w, w
        
        self.r, self.c = r, c
        self.x, self.y = self.grid_x + self.c*self.w + self.c*self.gap, self.grid_y + self.r*self.h + self.r*self.gap
        
        self.wall.set_position(self.x, self.y, self.w, self.h)
        self.roof.set_position(self.x, self.y, self.w, self.h)

    def is_colored(self):
        return self.roof.is_colored() and self.wall.is_colored()

    def equals(self, other):
        return self.wall.equals(other.wall) and self.roof.equals(other.roof)

# -----------------------------------------------------------------------------------------        

class HouseIcon(House):
    def __init__(self, grid_x, grid_y, w, h, r, c, wall_color='gray90', roof_color='gray90', border='gray90'):
        super().__init__(grid_x, grid_y, w, h, r, c, wall_color, roof_color, border)

    def draw(self, canvas):
        super().draw(canvas)
        font_size = self.h // 2
        canvas.create_text(self.x + self.w//2, self.y + self.h//4, fill = 'gray30', text = '+', font = 'Times ' + (str)(font_size))

    def increase_c(self):
        super().set_position(self.w, self.h, self.r, self.c+1)

    def decrease_c(self):
        super().set_position(self.w, self.h, self.r, self.c-1)

    def increase_r(self):
        super().set_position(self.w, self.h, self.r+1, 0)

    def decrease_r(self, c):
        super().set_position(self.w, self.h, self.r-1, c)

    def get_y_top_down_point(self):
        return self.y + self.h

    def get_gap(self):
        return self.gap
