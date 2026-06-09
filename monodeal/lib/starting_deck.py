from typing import List, Type

from lib.cards import Card
from lib.action_cards import BirthdayCard, DoubleRentCard, JustSayNoCard, PassGoCard, RentCard
from lib.number_cards import OneCard, TwoCard, ThreeCard, FourCard, FiveCard, TenCard

class DeckCardTypeSpec:
    def __init__(self, card_class: Type[Card], count: int) -> None:
        self.card_class: Type[Card] = card_class
        self.count: int = count

# const, don't mutate
starting_deck: List[DeckCardTypeSpec] = [
    DeckCardTypeSpec(BirthdayCard, 2),
    DeckCardTypeSpec(DoubleRentCard, 2),
    DeckCardTypeSpec(JustSayNoCard, 2),
    DeckCardTypeSpec(PassGoCard, 2),
    DeckCardTypeSpec(RentCard, 2),
    DeckCardTypeSpec(OneCard, 10),
    DeckCardTypeSpec(TwoCard, 7),
    DeckCardTypeSpec(ThreeCard, 6),
    DeckCardTypeSpec(FourCard, 5),
    DeckCardTypeSpec(FiveCard, 4),
    DeckCardTypeSpec(TenCard, 2),
]

def get_starting_deck() -> List[Card]:
    """Return a new list of new cards as specified in starting_deck"""
    deck: List[Card] = []
    for card_spec in starting_deck:
        deck += [card_spec.card_class()] * card_spec.count
    return deck
    