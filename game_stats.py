class GameStats:
    '''track stats for alien invasion'''

    def __init__(self,ai_game):
        '''initialze stats'''
        self.settings = ai_game.settings
        self.reset_stats()

        #start alien invasion in active state
        self.game_active = True
        
    def reset_stats(self):
        '''initialize stats that can chang during game'''
        self.ships_left = self.settings.ship_limit

    