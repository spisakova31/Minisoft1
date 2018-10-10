from math import sqrt

class Ball:
    def __init__(self, x, y, r, color='white', border='black'):
        self.x, self.y = x, y
        self.r = r
        self.color = color
        self.border = border

    def clicked(self, event):
        distance = sqrt(((event.x - self.x) ** 2) + ((event.y - self.y) ** 2))
        return distance < self.r
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, outline = self.border, width = 1)

    def set_color(self, color):
        self.color = color

class BallIcon(Ball):
    def __init__(self, x, y, r, color='gray90', border='gray90'):
        super().__init__(x, y, r, color, border)


    def draw(self, canvas):
        super().draw(canvas)
        canvas.create_text(self.x, self.y, fill = 'gray30', text = '+', font = 'Times 50')
