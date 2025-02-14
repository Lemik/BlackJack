from models.card import Card
from models.hand import Hand

class Player:
    def __init__(self, name) -> None:
        """Initialize a player with a name and an empty hand."""
        self.name = name 
        self.hand = Hand()

    def decision(self) -> str:
        """Decide whether to hit or stand based on hand value."""
        if self.hand.value >= 17:
            return "stand"
        else:
            return "hit"

    def __str__(self) -> str:
        """Return a formatted string for the player's status."""
        return f"{self.name}'s {self.hand}"

class Dealer:
    def __init__(self) -> None:
        """Initialize the dealer with an empty hand."""
        self.hand = Hand()

    def decision(self) -> str:
        """Dealer stands on 17 or higher, otherwise hits."""
        return "stand" if self.hand.value >= 17 else "hit"

    def __str__(self) -> str:
        """Show only one card if the hand has at least one card."""
        if not self.hand.hand:
            return "Dealer has no cards."
        return f"Dealer's Hand: {self.hand.hand[0]}, [Hidden Card]" if len(self.hand.hand) > 1 else f"Dealer's Hand: {self.hand.hand[0]}"
