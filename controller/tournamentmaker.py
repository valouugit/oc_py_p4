from rich.console import Console
import rich.prompt as Prompt
from model.command import Command

from model.tournament import Tournament
from view.tournamentview import TournamentView


class TournamentMaker:
    def __init__(self, console: Console, tournament: Tournament) -> None:
        self.console = console
        self.tournament = tournament
        self.command = None

    def show_tournament(self):
        while True:
            tournament_view = TournamentView(self.console, self.tournament)
            tournament_view.show()
            while self._ask_command() == Command.NO_COMMAND:
                continue
            if self.command is Command.BACK:
                break
            elif self.command is Command.PLAYER_ADD:
                pass

    def _ask_command(self) -> Command:
        command = Prompt.IntPrompt.ask("Tapez une commande")
        if command == 0:
            self.command = Command.BACK
        elif command == 1:
            self.command = Command.PLAYER_ADD
        else:
            return Command.NO_COMMAND
