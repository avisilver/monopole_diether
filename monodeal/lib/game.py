# from lib.action_cards import ActionCard
# from lib.cards import Card
from lib.game_area import GameArea
from lib.player import Player

from typing import List
class Game:
    """
    Represent the full state of a game including the Game area and all the players
    """
    def __init__(self, num_players: int):
        assert num_players >= 2, "It takes two to tango"
        self.game_area = GameArea()
        self.players: List[Player] = [] 
        for _p in range(num_players):
            self.players.append(Player())
