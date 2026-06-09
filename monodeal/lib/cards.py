"""Card classes"""

# from collections import abc
from typing import Optional

class Card(object):
    """Abstract base class for all cards"""

    _value: Optional[int] = None
    _bankable: bool = False

    # def __init__(self, value: Optional[int]=None, bankable: bool=False):
    #     self._value = value
    #     self._bankable = bankable

    def bankable(self):
        """
        Return whether the card can be played in the bank
        All cards with value apart from property cards and a small number of action cards are bankable
        """
        return self._bankable

    def value(self):
        """
        Return the card's value which is used to pay debts
        Almost all cards, including property cards, have value
        self._value is None for cards that don't have a value
        """
        return self._value

    def __str__(self):
        return """{}, bankable={}, value={}""".format(
            repr(self), self.bankable(), self.value()
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value()}, bankable={self.bankable()})"
    
    
class BankableCard(Card):
    """
    A card can be played in the bank and has a value, but is not necessarily a number card (e.g. action cards)
    """
    _bankable: bool = True
    _value: int = 0
    def __init__(self, value: Optional[int]=None):
        # A class that defines a value but doesn't set it in the constructor can set it here by passing it in as an argument,
        # but if it does set it in the constructor then that value will be used instead
        if value is not None:
            self._value = value

    def __add__(self, other_bankablecard: "BankableCard") -> int:
        if not isinstance(other_bankablecard, BankableCard):
            raise TypeError(f"Cannot add {type(self)} and {type(other_bankablecard)}")
        return self.value() + other_bankablecard.value()

class NumberCard(BankableCard):
    """Type class for number cards"""
    # def __str__(self):
    #     # return super().__str__()
    #     return f"NumberCard({self._value})"
    
    def __repr__(self):
        # return super().__str__()
        return f"NumberCard({self._value})"

class NonBankableActionCard(Card):
    """
    Base class for action cards that do not have a value and cannot be played in the bank
    A very few do not
    """
    def __init__(self, value: Optional[int]=None, bankable: bool=False):
        self._value = value
        self._bankable = bankable


class BankableActionCard(BankableCard):
    """
    Base class for action cards
    Most action cards are bankable and have a value.
    """


class PropertyCard(Card):
    """
    Base class for property cards
    Property cards are not bankable but have a value which is used when using them to pay rent and other debts,
    which happens when the player doesn't have enough money in the bank
    """

