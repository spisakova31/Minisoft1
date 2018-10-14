class Stripe:
    def __init__(self, x, y, w, h, color='white', border='black'):
        self.set_position(x, y, w, h)
        self.color = color
        self.border = border

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.border)

    def is_clicked(self, click):
        return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def is_colored(self):
        return self.color != 'white'

    def equals(self, other):
        return self.color == other.color     

# -------------------------------------------------------------------------------------------------------------------------        

class Flag:
    def __init__(self, grid_x, grid_y, w, h, r, c, color1='white', color2='white', color3='white', border='black'): 
        self.gap = 10
        self.grid_x, self.grid_y = grid_x, grid_y
        
        ph = w//4
        self.r, self.c = r, c
        self.w, self.h = w, w - 2*ph
        self.x, self.y = self.grid_x + self.c*self.w + self.c*self.gap, self.grid_y + self.r*self.h + self.r*ph
        self.stripe_height = self.h/3
        
        self.stripes = [Stripe(self.x, self.y, self.w, self.stripe_height, color1, border),
                        Stripe(self.x, self.y + self.stripe_height, self.w, self.stripe_height, color2, border),
                        Stripe(self.x, self.y + 2*self.stripe_height, self.w, self.stripe_height, color3, border)]

    def clicked(self, click):
        for stripe in self.stripes:
            if stripe.is_clicked(click):
                return stripe
        return None

    def is_clicked(self, click):
        return self.clicked(click) != None

    def draw(self, canvas):
        for stripe in self.stripes:
            stripe.draw(canvas)

    def set_position(self, w, h, r, c):
        ph = w//4
        self.r, self.c = r, c
        self.w, self.h = w, w - 2*ph
        self.x, self.y = self.grid_x + self.c*self.w + self.c*self.gap, self.grid_y + self.r*self.h + self.r*ph
        self.stripe_height = self.h/3

        for i in range(len(self.stripes)):
            stripe = self.stripes[i]
            stripe.set_position(self.x, self.y + i*self.stripe_height, self.w, self.stripe_height)

    def is_colored(self):
        return self.stripes[0].is_colored() and self.stripes[1].is_colored() and self.stripes[2].is_colored()

    def equals(self, other):
        return self.stripes[0].equals(other.stripes[0]) and self.stripes[1].equals(other.stripes[1]) and self.stripes[2].equals(other.stripes[2])

# --------------------------------------------------------------------------------------------------------------------------
            
class FlagIcon(Flag):
    def __init__(self, grid_x, grid_y, w, h, r, c, color1='gray90', color2='gray90', color3='gray90', border='gray90'):
        super().__init__(grid_x, grid_y, w, h, r, c, color1, color2, color3, border)

    def draw(self, canvas):
        super().draw(canvas)
        font_size = self.h // 2
        canvas.create_text(self.x + self.w//2, self.y + self.h//2, fill = 'gray30', text = '+', font = 'Times ' + (str)(font_size))
        
    def is_clicked(self, click):
        return self.x < click.x and self.x + self.w > click.x and self.y < click.y and self.y + self.h > click.y

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
            
