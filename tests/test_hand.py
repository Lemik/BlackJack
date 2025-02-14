import unittest 
from models.hand import Hand
from models.card import Card

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_add_A_cards(self):
        self.hand.add_card(Card("A", "♠"))
        
        self.assertEqual(self.hand.value, 11)
        self.assertEqual(self.hand.aces, 1)

    def test_add_8_cards(self):
        self.hand.add_card(Card("8", "♠"))
        
        self.assertEqual(self.hand.value, 8)
        self.assertEqual(self.hand.aces, 0)

    def test_value_cards(self):
        self.hand.add_card(Card("A", "♠"))
        self.hand.add_card(Card("8", "♠"))
        self.hand.add_card(Card("2", "♠"))
        
        self.assertEqual(self.hand.value, 21)
        self.assertEqual(self.hand.aces, 1)   


if __name__ == "__main__":
    unittest.main()