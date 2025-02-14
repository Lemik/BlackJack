import unittest
from models.deck import Deck
from models.card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        """Set up a shuffled deck before each test."""
        self.deck = Deck()
        self.deck.shuffle()
    
    def test_deck_deal(self):
        """Test that dealing reduces the deck size."""
        initial_size = len(self.deck.deck)
        dealt_cards = [self.deck.deal() for _ in range(5)]
        
        self.assertEqual(len(self.deck.deck), initial_size - 5)
        self.assertTrue(all(isinstance(card, Card) for card in dealt_cards))
    
    def test_deck_size(self):
        """Test that the deck starts with 52 cards."""
        self.assertEqual(len(self.deck.deck), 52)
    
if __name__ == "__main__":
    unittest.main()
