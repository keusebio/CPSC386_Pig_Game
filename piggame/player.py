
class C_Player:
    def __init__(self,name):
        self._name = name
        self.score = 0
        
    def __str__(self):
        return self._name
    def __list__(self):
        return self._name   
        
class C_PigPlayer(C_Player):
    def __init__(self):
        self._name = name 
    
    def does_roll(self):
        resp = promt('Do you want to roll?')
        return resp == "yes"
        
class C_AIPigPlayer(C_PigPlayer):
    def __init__(self, name):
        self._name = "HAL"
        
    def does_roll(self):
        return True
        