#este by sa to malo rozbit na objekty STRIPE - mali by vysku, suradnice, farbu a vlastne metody

class Flag:
    def __init__(self, x, y, w, h, color1='white', color2='white', color3='white', border='black'): 
        self.x, self.y = x, y #top left
        self.w, self.h = w, h
        self.stripe_height = self.h/3
        self.color1 = color1 #top stripe
        self.color2 = color2
        self.color3 = color3
        self.border = border

    def clicked(self, click):  #potrebujeme tu asi vracat nie True/False, ale ten objekt co bol kliknuty!!!!
        return self.clicked_stripe(click, 1) or self.clicked_stripe(click, 2) or self.clicked_stripe(click, 3)

    def clicked_stripe(self, click, stripe):
        return self.x < click.x and self.x + self.w > click.x and self.h < click.y and self.h + stripe*self.stripe_height > click.y

    def draw(self, canvas):
        colors = [self.color1, self.color2, self.color3]
        for i in range(3):
            canvas.create_rectangle(self.x, self.y + (self.stripe_height * i), self.x + self.w, self.y + (self.stripe_height * (i + 1)), fill = colors[i], outline = self.border)

    def set_color1(self, color):
        self.color1 = color

    def set_color2(self, color):
        self.color2 = color

    def set_color3(self, color):
        self.color3 = color

class FlagIcon(Flag):
    def __init__(self, x, y, w, h, color1='gray90', color2='gray90', color3='gray90', border='gray90'):
        super().__init__(x, y, w, h, color1, color2, color3, border)

    def draw(self, canvas):
        super().draw(canvas)
        canvas.create_text(self.x + self.w//2, self.y + self.h//2, fill = 'gray30', text = '+', font = 'Times 50')
        
        
        
            
