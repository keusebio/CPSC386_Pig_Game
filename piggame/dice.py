import random

class Die:
    def __init__(self):
        pass
    
    def roll(self, numrolls):
        return [random.randrange(1,7) for rolls in range(numrolls)]