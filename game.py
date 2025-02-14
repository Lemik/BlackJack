from models.card import Card
from models.deck import Deck
from models.hand import Hand
from models.player import Player, Dealer

import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class BlackjackGame:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('Jim')
        self.dealer = Dealer()
    
    def play_game(self) -> None:
        self.player.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())

        self.dealer.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())

        logging.info(f"\n{self.player.name}'s {self.player.hand}")
        logging.info(f"Dealer's {self.dealer}")  # One card hidden

        while self.player.decision() != "stand":
            self.player.hand.add_card(self.deck.deal())
        while self.dealer.decision() != "stand":
            self.dealer.hand.add_card(self.deck.deal())

        self.determine_winner()

    def determine_winner(self) -> None:
        """Determine the winner based on hand values."""
        logging.info("\nFinal Hands:")
        logging.info(f"{self.player.name}'s {self.player.hand}")
        logging.info(f"Dealer's {self.dealer.hand}")

        if self.player.decision() == "stand" and self.dealer.decision() == "stand":
            if(self.player.hand.value == 21):
                logging.info(f'Player {self.player.name} is a winner')

            elif(self.player.hand.value > 22):
                logging.info(f'Player {self.player.name} lost the game')

            elif(self.player.hand.value > self.dealer.hand.value):
                logging.info(f'Player {self.player.name} is a winner')

            elif(self.player.hand.value < self.dealer.hand.value):
                logging.info(f'Player {self.player.name} lost the game')
            else:
                logging.info("It's a tie!")