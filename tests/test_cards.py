from lib.cards import Card, NumberCard, ActionCard, BankableCard, PropertyCard

import unittest

class CardTests(unittest.TestCase):
    def test_card(self):
        c = Card()
        self.assertFalse(c.bankable())
        self.assertIsNone(c.value())
    
    def test_number_card(self):
        c = NumberCard()
        self.assertTrue(c.bankable())
        self.assertIsNotNone(c.value())
    
    def test_action_card(self):
        c = ActionCard()
        self.assertTrue(c.bankable())
        self.assertIsNone(c.value())
    
    def test_property_card(self):
        c = PropertyCard()
        self.assertFalse(c.bankable())
        self.assertIsNone(c.value())
    
    def test_bankable_card(self):
        c = BankableCard()
        self.assertTrue(c.bankable())
        self.assertIsNone(c.value())

    def test_sum_number_cards(self):
        val1, val2 = 1, 2
        c1 = NumberCard(val1)
        c2 = NumberCard(val2)
        self.assertEqual(c1 + c2, val1 + val2)