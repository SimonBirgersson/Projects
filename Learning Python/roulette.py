#%% this is a roulette simulation for fun
Class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1:37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets)-1
    def spin(self):
        self.ball = random.choice(self.pockets)
    def betPocket(self,pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return - amt
    def _str_(self):
    return 'Fair Roulette'n
#%%
def playRoulette(game,numSpins, pocket, bet):
    totPocket = 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)
    if toPrint:
        print(numSpins,' spins of ',game)
        print('Expected return betting', pocket, '=', str(100*totPocket/numSpins) + '%\n')
    return (totPocket/numSpins)

random.seed(0)
game =FairRoulette()
for numSpins in (100,1000000):
    for i range(3):
        playRoulette(game,numSpins,2,1,True)