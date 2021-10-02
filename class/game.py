#https://ncase.me/trust/

from collections import Counter

class   Player:
    def __init__(self,name="noname"):
        self.name = name
        self.dec_f = False
    def dec(self):
        self.dec_f = True

class   Cheater(Player):
    def __init__(self):
        super().__init__("cheater")
    def play(self,match=0):
        return False

class   Cooperative(Player):
    def __init__(self):
        super().__init__("cooperative")
    def play(self,match=0):
        return True

class   Copycat(Player):
    def __init__(self):
        super().__init__("copycat")
    def play(self,match):
        if match == 0:
            self.dec_f = False
            return True
        if self.dec_f == True:
            self.dec_f = False
            return False
        return True

class   Grudger(Player):
    def __init__(self):
        super().__init__("grudger")
    def play(self,match):
        if match == 0:
            self.dec_f = False
            return True
        if self.dec_f == True:
            return False
        return True

class   Detective(Player):
    def __init__(self):
        super().__init__("detective")
        self.cheat = 0
    def check_ch(self):
        if self.dec_f == True:
            self.cheat = 1
        self.dec_f = False
    def play(self,match):
        if match == 0:
            self.dec_f = False
            self.cheat = 0
            return True
        if match == 1:
            self.check_ch()
            return False
        if match == 2 or match == 3:
            self.check_ch()
            return True
        if self.cheat == 0:
            return False
        if self.dec_f == True:
            self.dec_f = False
            return False
        return True

class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
    def play(self, player1, player2):
        self.registry.update( {player1.name: 0} )
        self.registry.update( {player2.name: 0} )
        for i in range(self.matches):
            pl1 = player1.play(i)
            pl2 = player2.play(i)
            #print(i, pl1, pl2)
            if pl1 and pl2:
                self.registry.update( {player1.name: 2} )
                self.registry.update( {player2.name: 2} )
            elif pl2:
                player2.dec()
                self.registry.update( {player1.name: 3} )
                self.registry.subtract( {player2.name: 1} )
            elif pl1:
                player1.dec()
                self.registry.update( {player2.name: 3} )
                self.registry.subtract( {player1.name: 1} )
            else:
                player1.dec()
                player2.dec()
    def top3(self):
        for k,v in dict(self.registry.most_common(3)).items():
            print(k,": ", v, sep='')

if __name__ == "__main__":
    print("\033[38;5;154mmain_test\033[0m")

    game = Game()
    ch = Cheater()
    cp = Cooperative()
    cc = Copycat()
    g = Grudger()
    d = Detective()

    cout = 0
    players = [ch, cp, cc, g, d]

    for player1 in players:
        for player2 in players:
            if player1.name != player2.name and players.index(player1) > players.index(player2):
                game.play(player1, player2)
                cout+=1

    print(cout)
    game.top3()
