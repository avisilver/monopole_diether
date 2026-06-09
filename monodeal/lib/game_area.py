from typing import List
from lib.cards import Card
from lib.starting_deck import get_starting_deck
# from lib.action_cards import ActionCard, BirthdayCard, DoubleRentCard, JustSayNoCard, PassGoCard, RentCard

class GameArea:
    """
    Represent the central game area consisting of the main deck and play pile
    """
    def __init__(self):
        self.main_deck: List[Card] = get_starting_deck()
        self.play_pile: List[Card] = []
    
    def deal_two_cards(self) -> List[Card]:
        """
        Cards are always dealt two at a time from the main deck
        Remove at most two cards from the main deck and return them as a list so they can be given to a player
        When the return list is empty, the main deck is empty!
        """
        ret_cards: List[Card] = []
        count = 2
        while len(self.main_deck) > 0 and count > 0:
            ret_cards.append(self.main_deck.pop())
            count -= 1
        return ret_cards
    
    def play_card(self, card: Card):
        self.play_pile.append(card)



