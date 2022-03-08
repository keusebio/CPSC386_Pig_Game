import time
from .dice import C_Die
from .player import C_Player
class PigGame:
    def __init__(self):
        pass
    
    def  run(self):
        """ Init game """
        d = C_Die()
        r = None
        num_players = int(input('How Many Players? '))
        list_players = [None] * num_players
        
        """ get player names """        
        for p in list_players:
            i = list_players.index(p)
            p = input('Player {} name: '.format(i+1))
            list_players[i] = C_Player(p)
            
        print(list_players)
        
        """ the GaMe """
        while(True):
            """ Game Start """
            for p in list_players:
                total = p.score
                print('It is {}\'s turn! Your current score is: {}'.format(p, p.score))
                while(True):
                    decision = input('{}, would you like to roll? (y/n) Current score: {} '.format(p, p.score))
                    if decision == 'y':
                        r = d.roll()
                        print('{} rolled a: {}'.format(p, r ))
                        p.score = r + p.score
                    else:
                        print('{} is holding'.format(p))
                        break
                    if r == 1:
                        p.score = 0
                        print('You rolled a {}! Score reset back to 0, next player\'s turn.')
                
                """
                print("I'm in a game!")
                rolled_number = d.roll()
                print('You rolled: {}'.format(rolled_number))
                time.sleep(2)
                """