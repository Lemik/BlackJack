import unittest
from models.card import Card
from models.player import Player, Dealer

class TestPlayerDealer(unittest.TestCase):
    def setUp(self):
        """Set up a player and a dealer for testing."""
        self.player = Player("Alice")
        self.dealer = Dealer()
    
    def test_player_decision(self):
        """Test the player's decision logic."""
        self.player.hand.add_card(Card("10", "♠"))
        self.player.hand.add_card(Card("6", "♥"))
        
        self.assertEqual(self.player.decision(), "hit")  # Player should hit on 16
        
        self.player.hand.add_card(Card("5", "♦"))  # Now total is 21
        
        self.assertEqual(self.player.decision(), "stand")  # Player should stand on 21
    
    def test_dealer_decision(self):
        """Test the dealer's decision logic."""
        self.dealer.hand.add_card(Card("10", "♠"))
        self.dealer.hand.add_card(Card("5", "♥"))
        
        self.assertEqual(self.dealer.decision(), "hit")  # Dealer should hit on 15
        
        self.dealer.hand.add_card(Card("3", "♦"))  # Now total is 18
        
        self.assertEqual(self.dealer.decision(), "stand")  # Dealer should stand on 18
    
    def test_dealer_hidden_card_display(self):
        """Test if dealer correctly hides the second card when printing."""
        self.dealer.hand.add_card(Card("10", "♠"))
        self.dealer.hand.add_card(Card("5", "♥"))
        
        expected_output = f"Dealer's Hand: {self.dealer.hand.hand[0]}, [Hidden Card]"
        self.assertEqual(str(self.dealer), expected_output)
    
if __name__ == "__main__":
    unittest.main()
