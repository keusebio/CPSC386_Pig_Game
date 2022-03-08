import random

class C_Die:
    def __init__(self):
        pass
    
    def roll(self):
        return random.randrange(1,7)
        
        """
        return [random.randrange(1,7) for rolls in range(numrolls)]
        """