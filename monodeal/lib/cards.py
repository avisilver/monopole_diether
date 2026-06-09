"""Card classes"""

# from collections import abc
from typing import Optional

class Card(object):
    """Abstract base class for all cards"""

    _value: Optional[int] = None
    _bankable: bool = False

    def __init__(self, value: Optional[int]=None, bankable: bool=False):
        self._value = value
        self._bankable = bankable

    def bankable(self):
        """Return whether the card can be played in the bank"""
        return self._bankable

    def value(self):
        """Return the card's value which is used to pay debts"""
        return self._value

    def __str__(self):
        return """{}, bankable={}, value={}""".format(
            repr(self), self.bankable(), self.value()
        )

    # def __repr__(self):
    #     return f"Card({self.value()})"
    
    
class BankableCard(object):
    """
    Mixin class that indicates that a card can be played in the bank
    Inherit from this first before Card, to override the default value for BANKABLE
    """
    _bankable: bool = True
    _value: int = 0
    def __add__(self, other_bankablecard: "BankableCard") -> int:
        if not isinstance(other_bankablecard, BankableCard):
            raise TypeError(f"Cannot add {type(self)} and {type(other_bankablecard)}")
        return self.value() + other_bankablecard.value()

class NumberCard(BankableCard, Card):
    """Type class for number cards"""
    def __str__(self):
        # return super().__str__()
        return f"NumberCard({self._value})"
    def __repr__(self):
        # return super().__str__()
        return f"NumberCard({self._value})"

class ActionCard(BankableCard, Card):
    """Abstract base class for action cards"""


class PropertyCard(Card):
    """Abstract base class for property cards"""


# def make_number_card(name, value):
#     """Create an instance of a NumberCard with the given name and value"""
#     newclass = type(
#         name,
#         (NumberCard,),
#         {},
#         )
#     # This also worked if you wanted to return the class : newclass.VALUE = value
#     return newclass(value)
# Three = make_number_card("Three", value=3)


# from enum import Enum
# from collections import namedtuple

# CardClass = Enum(
#     "CardClass", (
#         'NUMBER',
#         'ACTION',
#         'PROPERTY',
#         )
#     )

# CardType = Enum(
#     "CardType", (
#         'ONE',
#         'TWO',
#         'FIVE',
#         'THREE',
#         'TEN',
#         )
#     )

# CardData = namedtuple("CardData", ("card_type", "card_class", "value"))

# card_data = {
#     CardType.ONE: CardData(CardType.ONE, CardClass.NUMBER, 1)
# }
