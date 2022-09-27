import random

class Insect:
    def __init__(self,l,w):
        self.wings = w
        self.legs = l
        self.flight = 0


    def calc_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight