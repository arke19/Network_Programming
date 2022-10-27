import random
from enum import Enum

class Value(Enum):
    Ace = 1
    Deuce = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class Suit(Enum):
    Clubs = 1
    Hearts = 2
    Diamonds = 3
    Spades = 4


class Card:

    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
       return self._value
       
    def getSuit(self):
       return self._suit

    def __str__(self):
       return "{} of {}".format(Value(self.getValue()).name, Suit(self.getSuit()).name)
    
class CardDeck:
   def __init__(self):
      self.cards = []
      self.reset()

   def shuffle(self):
       random.shuffle(self.cards)

   def getCard(self):
       return self.cards.pop()

   def size(self):
       return len(self.cards)
       
   def reset(self):
      for values in range(1,14):
         for suits in range(1,5):
            self.cards.append(Card(suits, values))



deck = CardDeck()
deck.shuffle()
while deck.size()>0:
   card = deck.getCard()
   print("Card {} has value {}".format(card, card.getValue()))
