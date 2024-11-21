class Player:

    players = 0

    def __init__(self, id, money=1000, makkara=[]):
        self.id = id
        self.money = money
        self.makkara = makkara
        Player.players += 1

class Game(Player):
    def __init__(self, id, money=1000, makkara=[]):
        super().__init__(id, money)

class Situation(Player):

    def buymakkara(self):
        pass