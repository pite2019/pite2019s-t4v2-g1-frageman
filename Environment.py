import random
import logging

class Environment:

    def __init__(self):
        pass

    def prepare_turb(self):
        for i in range(10000):
            yield random.gauss(0,15)

    