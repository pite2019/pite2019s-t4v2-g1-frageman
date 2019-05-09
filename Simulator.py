
import random
import sys
import os
import time
import logging
from Plane import Plane
from Environment import Environment

if __name__ == "__main__":

    plane = Plane()
    env = Environment()
    gen = env.prepare_turb()

    while True:
        if abs(plane.angle) < abs(plane.max):
            print(plane.angle)
        plane.add_angle(next(gen))
        if abs(plane.angle) > abs(plane.max):
            logging.warning("TURUBALTION FASTEN YOUR SEAT BELTS")
        if abs(plane.angle) > 70.0:
            logging.error("CRASH")
            exit(1)
        plane.correction()
        time.sleep(0.2)
