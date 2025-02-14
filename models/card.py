from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    
    def get_value(self) -> int :
        """Return the card value for Blackjack."""
        if (self.rank in ["K","Q","J"]):
            return 10
        elif(self.rank == "A"):
            return 11
        else:
            return int(self.rank)

    def __str__(self) -> str:
        """Return a string representation of the card."""
        return f"{self.rank}{self.suit}"