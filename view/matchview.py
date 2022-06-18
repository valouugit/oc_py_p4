from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.table import Table

from model.tournament import Tournament


class MatchView:
    def __init__(
            self,
            console: Console,
            tournament: Tournament,
        ):
        self.console = console
        self.tournament = tournament

    def show(self, view: bool = False):
        layout = Layout()
        layout.split_column(
            Layout(name="margin", size=3),
            Layout(name="match"),
        )
        layout["margin"].update(Text())
        layout["match"].update(self._get_matchs())

        self.console.print(layout)

    def _get_matchs(self):
        table = Table(
            title="Tout les matchs",
            expand=True,
        )
        table.add_column("Tours", justify="right", style="white")
        table.add_column("Gagnant", justify="right", style="green")
        table.add_column("Perdant", justify="right", style="red")

        for round in self.tournament.rounds:
            for match in round.match:
                if match[0][1] == 1:
                    winner = match[0][0].get_name()
                    loser = match[1][0].get_name()
                elif match[1][1] == 1:
                    winner = match[1][0].get_name()
                    loser = match[0][0].get_name()
                else:
                    winner = "%s %s" % (
                        match[0][0].get_name(),
                        match[1][0].get_name()
                    )
                    loser = ""

                table.add_row(
                    round.name,
                    winner,
                    loser
                )

        return table