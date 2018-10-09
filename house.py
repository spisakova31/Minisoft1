from math import tan, radians

class House:
    def __init__(self, x, y, w, h, wall_color='white', roof_color='white'):
        self.angle = 50
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.margin = self.w // 5
        self.wall_color = wall_color
        self.roof_color = roof_color

    def clicked(self, click):
        return self.clicked_wall(click) or self.clicked_roof(click)

    def clicked_wall(self, click):
        return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

    def clicked_roof(self, click):
        c_x = click.x
        if c_x > self.x + self.w/2:
            vzbodu = c_x - (self.x + self.w/2)
            c_x = self.x + self.w/2 - vzbodu
        side_w = c_x - (self.x - self.margin)
        v = abs(tan(radians(self.angle))) * (side_w)
        return self.x - self.margin < click.x and self.x + self.w + self.margin  > click.x and self.y - v < click.y and self.y > click.y

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.wall_color, outline = 'black')
        v = abs(tan(radians(self.angle))) * (self.w/2  + self.margin)
        canvas.create_polygon(self.x - self.margin, self.y, self.x + self.w/2, self.y - v, self.x + self.w + self.margin, self.y, fill = self.roof_color, outline = 'black')
