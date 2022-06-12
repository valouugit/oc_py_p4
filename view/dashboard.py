from typing import List
from rich.console import Console
from rich.table import Table
from rich import print
from rich.layout import Layout
from rich.text import Text

from model.tournament import Tournament


class Dashboard:
    def __init__(self, console: Console, tournaments: List[Tournament]) -> None:
        self.console = console
        self.tournaments = tournaments

    def show(self):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="tournaments", ratio=1),
        )
        layout["header"].update(Text())

        table = Table(
            title="Menu",
            expand=True,
            leading=10,
        )

        table.add_column(
            "Commande", justify="right", style="cyan", ratio=1, no_wrap=True
        )
        table.add_column("Action", justify="right", style="cyan", ratio=5, no_wrap=True)

        table.add_row("1", "Ajouter un tournois")
        table.add_row("2", "Voir un tournois")

        layout["main"].update(table)
        layout["tournaments"].update(self.showTournaments())

        self.console.print(layout)

    def showTournaments(self) -> Table:
        table = Table(
            title="Tournois",
            expand=True,
            leading=10,
        )
        table.add_column("Numéro", justify="right", style="cyan", no_wrap=True)
        table.add_column("Nom", justify="right", style="cyan", no_wrap=True)
        table.add_column("Lieu", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", justify="right", style="cyan", no_wrap=True)
        table.add_column(
            "Nombre de rounds", justify="right", style="cyan", no_wrap=True
        )
        table.add_column("Type de timer", justify="right", style="cyan", no_wrap=True)
        table.add_column("Description", justify="right", style="cyan", no_wrap=True)
        table.add_column("Nombre de round", justify="right", style="cyan", no_wrap=True)

        if not (self.tournaments):
            table.add_row(
                "Vide", "Vide", "Vide", "Vide", "Vide", "Vide", "Vide", "Vide"
            )
            return table

        index = 1
        for tournament in self.tournaments:
            table.add_row(
                str(index),
                tournament.name,
                tournament.location,
                tournament.date.strftime("%d/%m/%Y"),
                str(len(tournament.rounds)),
                tournament.timer.name,
                tournament.description,
                str(tournament.rounds_number),
            )
            index += 1

        return table
