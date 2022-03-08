import time
from .dice import C_Die
from .player import C_AIPigPlayer
from .player import C_Player
class PigGame:
    def __init__(self):
        pass
    
    def  run(self):
        """ Init game """
        d = C_Die()
        r = None
        winFlag = False
        AIFlag = False


        """ get players """ 
        num_players = int(input('How Many Players? '))
        list_players = [None] * num_players
        if num_players == 1:
            AIFlag = True
      
        for p in list_players:
            i = list_players.index(p)
            p = input('Player {} name: '.format(i+1))
            list_players[i] = C_Player(p)
            
        if AIFlag == True:
            list_players.append(C_AIPigPlayer())
        
        """ the GaMe """
        while(winFlag == False):
            """ Welcome + rules """
            
            """ Game """
            for p in list_players:
                total = p.score
                print('It is {}\'s turn! Your current score is: {}'.format(p, p.score))
                while(True):
                    decision = p.does_roll() 
                    
                    if decision:
                        r = d.roll()
                        print('{} rolled a: {}'.format(p, r ))
                        p.score = r + p.score
                        print('current score is: {}'.format(p.score))
                    else:
                        print('{} is holding'.format(p))
                        break
                    if r == 1:
                        p.score = 0
                        print('{} rolled a 1! Score reset back to 0, next player\'s turn.'.format(p))
                        break
                    if p.score >= 30:
                        winFlag = True
                        break
                
                if winFlag == True:
                    print('{} won with {} points! GG'.format(p, p.score))
                    break
                