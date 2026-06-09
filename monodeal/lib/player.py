from lib.cards import Card, BankableCard, PropertyCard
from typing import List

class Player:
    _hand: List[Card]
    _properties: List[PropertyCard]
    _bank: List[BankableCard]
    def __init__(self):
        self._hand = []
        self._bank = []
        self._properties = []