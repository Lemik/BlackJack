import random  
from typing import List
from models.card import Card

class Deck:
    def __init__(self) -> None:
        suits = ["♠"," ♥","♦","♣"]
        ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        self.deck = [Card(rank,suit) for suit in suits  for rank in ranks ]
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self) -> Card:
        if not self.deck:
            raise ValueError("No cards left in the deck!") 
        return self.deck.pop()