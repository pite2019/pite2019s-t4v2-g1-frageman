import random

class Plane:
    def __init__(self):
        self.max = 25.0
        self.angle = 0
	    
    def add_angle(self, ang):
        self.angle += ang
    
    def correction(self):
        correct_angle = abs(random.gauss(0,10))

        if self.angle > 0:
            self.angle -= correct_angle
        else:
            self.angle += correct_angle
