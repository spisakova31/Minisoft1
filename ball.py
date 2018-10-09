from math import sqrt

class Ball:
    def __init__(self, x, y, r, color='white'):
        self.x, self.y = x, y
        self.r = r
        self.color = color

    def clicked(self, click):
        distance = sqrt(((click.x - self.x) ** 2) + ((click.y - self.y) ** 2))
        return distance < self.r
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, outline = 'black', width = 1)


class BallIcon(Ball):
    def __init__(self, x, y, r, color='gray90'):
        super().__init__(x, y, r, color)


    def draw(self, canvas):
        super().draw(canvas)
        canvas.create_text(self.x, self.y, fill = 'gray30', text = '+', font = 'Times 50')
