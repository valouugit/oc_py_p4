from datetime import datetime
from rich.console import Console
from controller.tournamentmaker import TournamentMaker
from model.command import Command
import rich.prompt as Prompt

from model.timer import Timer
from model.tournament import Tournament
from view.dashboard import Dashboard


class TournamentManager:
    def __init__(self) -> None:
        self.console = Console()
        self.tournaments = []
        self.command = None

    def show_dashboard(self):
        while True:
            menu = Dashboard(self.console, self.tournaments)
            menu.show()
            while self._ask_command() == Command.NO_COMMAND:
                continue
            if self.command is Command.TOURNAMENT_ADD:
                self._add_tournament()
            elif self.command is Command.TOURNAMENT_VIEW:
                tournament_index = Prompt.IntPrompt.ask("Numéro du tournois")
                tournament_maker = TournamentMaker(
                    self.console, self.tournaments[tournament_index - 1]
                )
                tournament_maker.show_tournament()

    def _add_tournament(self):
        t_name = Prompt.Prompt.ask(prompt="Nom du tournois", default="Tournois")
        t_description = Prompt.Prompt.ask(prompt="Description du tournois")
        t_location = Prompt.Prompt.ask(prompt="Lieu du tournois")
        t_date = Prompt.Prompt.ask(
            prompt="Date du tournois (DD/MM/AAAA)",
            default=datetime.now().strftime("%d/%m/%Y"),
        )
        t_date = datetime.strptime(t_date, "%d/%m/%Y")
        t_timer = Prompt.Prompt.ask(
            prompt="Type de timer",
            choices=[Timer.BLITZ.name, Timer.BULLET.name, Timer.SPEED.name],
            default="BLITZ",
        )
        for i in Timer:
            if t_timer == i.name:
                t_timer = i
        t_round_number = Prompt.IntPrompt.ask("Nombre de tours", default=4)
        self.tournaments.append(
            Tournament(
                name=t_name,
                location=t_location,
                date=t_date,
                timer=t_timer,
                rounds=[],
                players=[],
                description=t_description,
                rounds_number=t_round_number,
            )
        )

    def _ask_command(self) -> Command:
        command = Prompt.IntPrompt.ask("Tapez une commande")
        if command == 1:
            self.command = Command.TOURNAMENT_ADD
        elif command == 2:
            self.command = Command.TOURNAMENT_VIEW
        else:
            return Command.NO_COMMAND
