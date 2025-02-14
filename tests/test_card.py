import unittest
from models.card import Card

class TestCard(unittest.TestCase):
    def test_card_value(self):
        self.assertEqual(Card("A", "♠").get_value(), 11)
        self.assertEqual(Card("K", "♠").get_value(), 10)
        self.assertEqual(Card("5", "♠").get_value(), 5)

if __name__ == "__main__":
    unittest.main()