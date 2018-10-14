from ball import Ball
from house import House
from flag import Flag

class Task:

    def __init__(self, number, obj, num_colours):
        self.number = number
        self.obj = obj
        self.num_colours = num_colours

    def create_text(self):
        words = {Ball: ('lôpt', 'jedna nebola vyfarbená'), House: ('domčekov', 'jeden nebol vyfarbený'), Flag: ('vlajok', 'jedna nebola vyfarbená')}
        return ('Koľko najviac rôznych ' + words[type(self.obj)][0] + ' vieš vytvoriť tak, aby ani ' + words[type(self.obj)][1] +
                ' rovnako ako ostatné? Použi všetky farby na palete vpravo.')

ball = Ball(10,10,10)
task = Task(1, ball, 4)  
print(task.create_text())
