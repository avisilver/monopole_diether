from monodeal.lib.cards import Card, NumberCard, BankableActionCard, NonBankableActionCard, BankableCard, PropertyCard

import unittest

class CardTests(unittest.TestCase):
    def test_card(self):
        c = Card()
        self.assertFalse(c.bankable())
        self.assertIsNone(c.value())
    
    def test_number_card(self):
        c = NumberCard(1)
        self.assertTrue(c.bankable())
        self.assertIsNotNone(c.value())
    
    def test_bankable_action_card(self):
        c = BankableActionCard(5)
        self.assertTrue(c.bankable())
        self.assertEqual(c.value(), 5)
    
    def test_non_bankable_action_card(self):
        c = NonBankableActionCard()
        self.assertFalse(c.bankable())
        self.assertIsNone(c.value())
    
    def test_property_card(self):
        c = PropertyCard()
        self.assertFalse(c.bankable())
        self.assertIsNone(c.value())
    
    def test_bankable_card(self):
        c = BankableCard(42)
        self.assertTrue(c.bankable())
        self.assertEqual(c.value(), 42)

    def test_sum_number_cards(self):
        val1, val2 = 1, 2
        c1 = NumberCard(val1)
        c2 = NumberCard(val2)
        self.assertEqual(c1 + c2, val1 + val2)