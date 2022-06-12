from rich.console import Console
from rich.table import Table
from model.command import Command
import rich.prompt as Prompt

from model.round import Round
from model.tournament import Tournament
from view.roundview import RoundView
from controller.playerpeers import PlayerPeers


class RoundMaker:
    def __init__(
        self,
        console: Console,
        tournament: Tournament,
        round: Round,
        player_peers: PlayerPeers,
    ) -> None:
        self.console = console
        self.tournament = tournament
        self.round = round
        command = None
        self.player_peers = player_peers

    def show_round(self):
        while True:
            pass

    def make_round(self):
        peers = self.player_peers.getNextPeers()
        for peer in peers:
            self.round.match.append(([peer[0], 0], [peer[1], 0]))
        round_view = RoundView(self.console, self.tournament, self.round)
        round_view.show()
        index = 0
        for peer in peers:
            print(peer)
            winner = Prompt.IntPrompt.ask(
                "Qui de %s (1) ou %s (2) à gagné? (0 si nul)"
                % (peer[0].get_name(), peer[1].get_name()),
                choices=["0", "1", "2"],
            )
            if winner == 0:
                self.round.match[index] = ([peer[0], 0.5], [peer[1], 0.5])
            elif winner == 1:
                self.round.match[index] = ([peer[0], 1], [peer[1], 0])
            elif winner == 2:
                self.round.match[index] = ([peer[0], 0], [peer[1], 1])
            index += 1
