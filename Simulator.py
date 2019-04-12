import random
import sys
import os
import time

class Plane:

    def __init__(self):
       self.angle = 0
    
    def simulation(self):
        self.angle+= random.randint(0,3)
        
    def correction(self):
        self.angle -= random.randint(0,3)
        
plane = Plane()
while True:
    plane.simulation()
    plane.correction()
    print(plane.angle)
    time.sleep(0.2)




    
  
