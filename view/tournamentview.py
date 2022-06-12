from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.text import Text

from model.tournament import Tournament


class TournamentView:
    def __init__(self, console: Console, tournament: Tournament = None) -> None:
        self.tournament = tournament
        self.console = console

    def show(self):
        layout = Layout()
        layout.split_column(
            Layout(name="margin", size=3),
            Layout(name="header", ratio=1),
            Layout(name="tournaments", ratio=6),
        )
        layout["tournaments"].split_row(
            Layout(name="Commande"), Layout(name="players"), Layout(name="match")
        )
        layout["margin"].update(Text())
        layout["header"].update(self._getHeaderDetail())

        self.console.print(layout)

    def _get_header(self) -> Table:
        table = Table(
            title=self.tournament.name,
            expand=True,
        )
        table.add_column("Description", justify="right", style="cyan", no_wrap=True)
        table.add_column("Lieu", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", justify="right", style="cyan", no_wrap=True)
        table.add_column("Type de timer", justify="right", style="cyan", no_wrap=True)
        table.add_column(
            "Nombre de rounds réalisés", justify="right", style="cyan", no_wrap=True
        )
        table.add_column(
            "Nombre de rounds", justify="right", style="cyan", no_wrap=True
        )

        table.add_row(
            self.tournament.description,
            self.tournament.location,
            self.tournament.date.strftime("%d/%m/%Y"),
            self.tournament.timer.name,
            str(len(self.tournament.rounds)),
            str(self.tournament.rounds_number),
        )

        return table

    def _get_command(self) -> Table:
        pass
