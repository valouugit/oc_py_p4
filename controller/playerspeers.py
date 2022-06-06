from typing import List

from model.player import Player
from model.tournament import Tournament


class PlayerPeers:
    
    def __init__(self, tournament : Tournament) -> None:
        self.tournament = tournament
        self.offset = 0
    
    def _genPeersWithPosition(self):
        peers = []
        sorted_players = sorted(self.tournament.players, key=lambda p: p.position)
        for peer in range(0, int(len(sorted_players)/2)):
            peers.append(
                (
                    sorted_players[peer],
                    sorted_players[int(len(sorted_players)/2+peer)]
                )
            )
        return peers