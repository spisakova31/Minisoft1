from ball import Ball
from house import House
from flag import Flag

class Task:

    def __init__(self, number, obj, num_colours):
        self.number = number
        self.obj = obj
        self.num_colours = num_colours

    def get_text(self):
        words = {'Ball': ('lôpt', 'jedna nebola vyfarbená'), 'House': ('domčekov', 'jeden nebol vyfarbený'), 'Flag': ('vlajok', 'jedna nebola vyfarbená')}
        return ('Koľko najviac rôznych ' + words[self.obj][0] + ' vieš vytvoriť tak, aby ani ' + words[self.obj][1] +
                ' rovnako ako ostatné? \nPouži všetky farby na palete vpravo.')

