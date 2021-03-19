import random
class Player:
    def __init__(self, name ) -> None:
        self.name = name
        self.hand = []

    def showPlayer(self):
        print("Players name : {} \n Players cards are {}".format(self.name,self.showHand))

    def showHand(self):
        for card in self.hand:
            card.printCard()

    def addCard(self,card):
        self.hand.append(card)

class Card: 
    def __init__(self, suit, val) -> None:
        suits = ['♢','♡','♣','♠']
        if (suit in suits and val in range(1,14)):
            self.suit = suit
            self.val = val
    
    def printCard(self):
        if self.val >= 10:
            print("------------")
            print("| {}       |".format(self.val))
            print("|          |")
            print("|    {}     |".format(self.suit))
            print("|          |")
            print("|       {} |".format(self.val))
            print("------------")
        else:
            print("------------")
            print("| {}        |".format(self.val))
            print("|          |")
            print("|    {}     |".format(self.suit))
            print("|          |")
            print("|       {}  |".format(self.val))
            print("------------")

    def show(self):
        print("{} of {}".format(self.val,self.suit ))

class Deck: 
    def __init__(self) -> None:
        self.deck = []
        for suit in ['♢','♡','♣','♠']:
            for val in range(1,14):
                card = Card(suit,val)
                self.deck.append(card)
    
    def showDeck(self):
        for card in self.deck:
            card.printCard()
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def dealCard(self, Player):
        Player.addCard(self.deck.pop(0))
        

class Blackjack:
    def __init__(self, playerCount) -> None:
        self.theDeck = Deck()
        self.theDeck.shuffle()
        self.Players = []
        self.Dealer = Player("Dealer")
        for i in range(int(playerCount)):
            self.Players.append(Player('Player{}'.format(i+1)))

    def cardTotal(self, Player) -> int:
        cardCount = 0
        for card in Player.hand:
            if card.val == 1:
               cardCount += 11 
            elif card.val in [10,11,12,13]:
                cardCount += 10
            else:
                cardCount += card.val
        return cardCount

    def dealCard(self,Player):
        self.theDeck.dealCard(Player)

    def showPlayers(self):
        for Player in self.Players:
            Player.showPlayer()


# def play():
#     print("\t        Lets Play Some Blackjack !!!")
#     print("________________________________________________________________")
#     playerCount = input("How many people will be playing? : ")
#     Game = Blackjack(playerCount)
#     for player in Game.Players:
#         Game.dealCard(player)
#     Game.dealCard(Game.Dealer)
#     for player in Game.Players:
#         Game.dealCard(player)
    
#     for player in Game.Players:
#         print(player.name)
#         player.showHand()
