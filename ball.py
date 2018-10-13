from math import sqrt

class Ball:
    def __init__(self, grid_x, grid_y, w, h, r, c, color='white', border='black'):
        self.gap = 5
        
        self.grid_x, self.grid_y = grid_x, grid_y
        self.set_position(w, h, r, c)
        
        self.color = color
        self.border = border

    def is_clicked(self, click):
        distance = sqrt(((click.x - self.x) ** 2) + ((click.y - self.y) ** 2))
        return distance < self.rad

    def clicked(self, click):
        if self.is_clicked(click):
            return self
        return None
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.rad, self.y - self.rad, self.x + self.rad, self.y + self.rad, fill = self.color, outline = self.border, width = 1)

    def set_color(self, color):
        self.color = color

    def set_position(self, w, h, r, c):
        if w < h:
            self.w, self.h = w
            self.rad = w // 2
        else:
            
            self.w, self.h = h, h
            self.rad = h // 2
       
        self.r, self.c = r, c
        self.x, self.y = self.grid_x + self.c*self.w + self.c*self.gap + self.rad, self.grid_y + self.r*self.h + self.r*self.gap + self.rad
        

# --------------------------------------------------------------------------

class BallIcon(Ball):
    def __init__(self, grid_x, grid_y, w, h, r, c, color='gray90', border='gray90'):
        super().__init__(grid_x, grid_y, w, h, r, c, color, border)

    def draw(self, canvas):
        super().draw(canvas)
        font_size = self.rad
        canvas.create_text(self.x, self.y, fill = 'gray30', text = '+', font = 'Times ' + (str)(font_size))

    def increase_c(self):
        super().set_position(self.w, self.w, self.r, self.c+1)

    def decrease_c(self):
        super().set_position(self.w, self.w, self.r, self.c-1)

    def increase_r(self):
        super().set_position(self.w, self.w, self.r+1, 0)

    def decrease_r(self, c):
        super().set_position(self.w, self.w, self.r-1, c)

    def get_y_top_down_point(self):
        return self.y + self.rad

    def get_gap(self):
        return self.gap
