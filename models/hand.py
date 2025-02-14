from models.card import Card

class Hand:
    def __init__(self) -> None:
        """Initialize an empty hand with a total value of 0."""
        self.hand = []  # Stores Card objects
        self.value = 0  # Total value of the hand
        self.aces = 0  # Track number of Aces

    def add_card(self, card: Card) -> None:
        """Add a card to the hand and update the total value."""
        self.hand.append(card)
        self.value += card.get_value()  # Add card value
        
        # Track Aces separately
        if card.rank == "A":
            self.aces += 1  # Count the Ace

        # If value exceeds 21 and there's an Ace, reduce Ace value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10  # Convert an Ace from 11 to 1
            self.aces -= 1  # Reduce the Ace count

    def __str__(self) -> str:
        """Return a string representation of the hand."""
        return f"Hand: {', '.join(str(card) for card in self.hand)} | Value: {self.value}"