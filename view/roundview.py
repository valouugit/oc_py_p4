from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.table import Table

from model.round import Round
from model.tournament import Tournament


class RoundView:
    def __init__(self, console: Console, tournament: Tournament, round: Round) -> None:
        self.console = console
        self.tournament = tournament
        self.round = round

    def show(self):
        layout = Layout()
        layout.split_column(
            Layout(name="margin", size=3),
            Layout(name="header", ratio=1),
            Layout(name="match", ratio=6),
        )
        layout["margin"].update(Text())
        layout["header"].update(self._get_header())
        layout["match"].update(self._get_match())

        self.console.print(layout)

    def _get_header(self):
        table = Table(
            title=self.round.name,
            expand=True,
        )
        table.add_column("Date de départ", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date de fin", justify="right", style="cyan", no_wrap=True)

        table.add_row(
            self.round.date_start.strftime("%d/%m/%Y"),
            self.round.date_end.strftime("%d/%m/%Y"),
        )

        return table

    def _get_match(self):
        table = Table(
            title="Matchs",
            expand=True,
        )
        table.add_column("Joueur 1", justify="right", style="cyan", no_wrap=True)
        table.add_column("Joueur 2", justify="right", style="cyan", no_wrap=True)

        for match in self.round.match:
            table.add_row(match[0][0].get_name(), match[1][0].get_name())

        return table
