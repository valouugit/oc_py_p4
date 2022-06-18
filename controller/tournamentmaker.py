from datetime import datetime
from typing import List
from rich.console import Console
import rich.prompt as Prompt
from controller.playermaker import PlayerMaker

from controller.roundmaker import RoundMaker
from controller.tournamentdb import TournamentDb
from model.command import Command
from model.player import Player
from model.round import Round
from model.tournament import Tournament
from view.matchview import MatchView
from view.roundview import RoundView
from view.tournamentview import TournamentView
from controller.playerpeers import PlayerPeers


class TournamentMaker:
    def __init__(
        self, console: Console, tournament: Tournament, players: List[Player]
    ) -> None:
        self.console = console
        self.tournament = tournament
        self.command = None
        self.player_peers = PlayerPeers(self.tournament)
        self.parent_players = players

    def show_tournament(self):
        sort_alpha = False
        while True:
            tournament_view = TournamentView(self.console, self.tournament)
            tournament_view.show(sort_alpha)
            while self._ask_command() == Command.NO_COMMAND:
                continue
            if self.command is Command.BACK:
                break
            elif self.command is Command.PLAYER_ADD:
                self._add_player()
            elif self.command is Command.PLAYER_IMPORT:
                tournament_view.show_players(self.parent_players)
                j_index = Prompt.IntPrompt.ask("Selectionnez un joueur")
                self.tournament.players.append(
                    self.parent_players[j_index - 1]
                )
            elif self.command is Command.ROUND_ADD:
                round = self._add_round()
                if type(round) is Round:
                    round_maker = RoundMaker(
                        self.console, self.tournament, round, self.player_peers
                    )
                    round_maker.make_round()
            elif self.command is Command.ROUND_VIEW:
                round_index = Prompt.IntPrompt.ask("Numéro du round")
                round_view = RoundView(
                    self.console,
                    self.tournament,
                    self.tournament.rounds[round_index - 1],
                )
                round_view.show()
                Prompt.Prompt.ask("Appuyer sur entrée pour continuer")
            elif self.command is Command.TOURNAMENT_SAVE:
                tournament_db = TournamentDb()
                tournament_db.save_tournament(self.tournament)
            elif self.command is Command.POSITION_CHANGE:
                for p in self.tournament.players:
                    position = Prompt.Prompt.ask(
                        "Quel est la position de %s? (%s)"
                        % (p.get_name(), p.position)
                    )
                    p.position = position
            elif self.command is Command.MATCH_VIEW:
                match_viewer = MatchView(
                    self.console,
                    self.tournament
                )
                match_viewer.show()
                Prompt.Prompt.ask("Appuyer sur entrée pour continuer")
            elif self.command is Command.CHANGE_SORT:
                sort_alpha = not sort_alpha

    def _add_player(self):
        player_maker = PlayerMaker()
        self.tournament.players.append(player_maker.add_player())

    def _add_round(self) -> Round | None:
        if len(self.tournament.rounds) >= self.tournament.rounds_number:
            self.console.print("Tous les tours ont déjà été réalisé !")
            Prompt.Prompt.ask("Appuyer sur 'entrée' pour continer")
            return
        r_name = Prompt.Prompt.ask(
            prompt="Nom du tour",
            default="Tour %s" % str(len(self.tournament.rounds) + 1),
        )
        r_start = Prompt.Prompt.ask("Date de début (DD/MM/AAAA)")
        r_stop = Prompt.Prompt.ask("Date de fin (DD/MM/AAAA)")

        round = Round(
            name=r_name,
            match=[],
            date_start=datetime.strptime(r_start, "%d/%m/%Y"),
            date_end=datetime.strptime(r_stop, "%d/%m/%Y"),
        )
        self.tournament.rounds.append(round)

        return round

    def _ask_command(self) -> Command:
        command = Prompt.IntPrompt.ask("Tapez une commande")
        if command == 0:
            self.command = Command.BACK
        elif command == 1:
            self.command = Command.PLAYER_ADD
        elif command == 2:
            self.command = Command.PLAYER_IMPORT
        elif command == 3:
            self.command = Command.ROUND_ADD
        elif command == 4:
            self.command = Command.ROUND_VIEW
        elif command == 5:
            self.command = Command.TOURNAMENT_SAVE
        elif command == 6:
            self.command = Command.POSITION_CHANGE
        elif command == 7:
            self.command = Command.MATCH_VIEW
        elif command == 8:
            self.command = Command.CHANGE_SORT
        else:
            return Command.NO_COMMAND
