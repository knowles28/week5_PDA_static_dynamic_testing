import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Heart", 1)
        self.card2 = Card("Spade", 2)
        self.card3 = Card("Diamond", 3)
        
        self.game = CardGame()
        
    
    def test_check_for_ace_true(self):
        game = self.game.check_for_ace(self.card1)
        self.assertEqual(True, game)
        
    
    def test_check_for_ace_false(self):
        game = self.game.check_for_ace(self.card2)
        self.assertEqual(False, game)
        
    
    def test_highest_card_first(self):
        game = self.game.highest_card(self.card2, self.card1)
        self.assertEqual(self.card2, game)
        
        
    def test_highest_card_second(self):
        game = self.game.highest_card(self.card2, self.card3)
        self.assertEqual(self.card3, game)
        
        
    def test_card_total_1(self):
        cards = [self.card1, self.card2, self.card3]
        game = self.game.cards_total(cards)
        self.assertEqual("You have a total of 6", game)
     
        
    def test_card_total_2(self):
        cards = [self.card3, self.card2]
        game = self.game.cards_total(cards)
        self.assertEqual("You have a total of 5", game)

