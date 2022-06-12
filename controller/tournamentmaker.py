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
                self._add_player()

    def _add_player(self):
        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}
        p_first_name = Prompt.Prompt.ask("Prénom du joueur")
        p_last_name = Prompt.Prompt.ask("Nom du joueur")
        p_birthday = Prompt.Prompt.ask("Date d'anniversaire (DD/MM/AAAA)")
        p_gender = Prompt.Prompt.ask(
            "Genre", choices=[genre_display[Gender.MAN], genre_display[Gender.WOMAN]]
        )
        p_position = Prompt.IntPrompt.ask("Position")

        self.tournament.players.append(
            Player(
                first_name=p_first_name,
                last_name=p_last_name,
                birthday=datetime.strptime(p_birthday, "%d/%m/%Y"),
                gender=list(genre_display.keys())[
                    list(genre_display.values()).index(p_gender)
                ],
                position=p_position,
            )
        )

    def _ask_command(self) -> Command:
        command = Prompt.IntPrompt.ask("Tapez une commande")
        if command == 0:
            self.command = Command.BACK
        elif command == 1:
            self.command = Command.PLAYER_ADD
        else:
            return Command.NO_COMMAND
