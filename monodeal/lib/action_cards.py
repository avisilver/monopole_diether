from lib.cards import BankableActionCard, NonBankableActionCard

class PassGoCard(BankableActionCard):
    """
    Collect two cards from the deck
    """
    _value: int = 2

class RentCard(BankableActionCard):
    """Charge rent"""
    _value: int = 2


class DoubleRentCard(NonBankableActionCard):
    """
    Play with RentCard
    Double the rent amount
    """

class JustSayNoCard(NonBankableActionCard):
    """
    Prevent an opponent's action against you
    """


class BirthdayCard(BankableActionCard):
    """
    Receive a birthday card. And money. You get money
    """
    _value: int = 2


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """


# class Card(ActionCard):
#     """
    
#     """

