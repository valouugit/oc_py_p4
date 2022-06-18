from typing import List
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from model.gender import Gender
from model.player import Player

from model.tournament import Tournament


class Dashboard:
    def __init__(
        self,
        console: Console,
        tournaments: List[Tournament],
        players: List[Player]
    ):
        self.console = console
        self.tournaments = tournaments
        self.players = players

    def show(self):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main", ratio=2),
            Layout(name="body", ratio=6),
        )
        layout["header"].update(Text())
        layout["body"].split_row(
            Layout(name="tournaments"),
            Layout(name="players")
        )

        table = Table(
            title="Menu",
            expand=True,
            leading=10,
        )

        table.add_column(
            "Commande", justify="right", style="cyan", ratio=1
        )
        table.add_column(
            "Action",
            justify="right",
            style="cyan",
            ratio=5,
            no_wrap=True
        )

        table.add_row("1", "Ajouter un tournois")
        table.add_row("2", "Voir un tournois")
        table.add_row("3", "Ajouter un joueur")

        layout["main"].update(table)
        layout["tournaments"].update(self.showTournaments())
        layout["players"].update(self._get_players())

        self.console.print(layout)

    def showTournaments(self) -> Table:
        table = Table(
            title="Tournois",
            expand=True,
            leading=10,
        )
        table.add_column("Numéro", justify="right", style="cyan")
        table.add_column("Nom", justify="right", style="cyan")
        table.add_column("Lieu", justify="right", style="cyan")
        table.add_column("Date", justify="right", style="cyan")
        table.add_column(
            "Nombre de rounds", justify="right", style="cyan"
        )
        table.add_column("Type de timer", justify="right", style="cyan")
        table.add_column("Description", justify="right", style="cyan")
        table.add_column("Nombre de round", justify="right", style="cyan")

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

    def _get_players(self) -> Table:
        table = Table(
            title="Joueurs",
            expand=True,
        )
        table.add_column("Nom", justify="right", style="cyan", ratio=5)
        table.add_column(
            "Date d'anniversaire", justify="right", style="cyan", ratio=5
        )
        table.add_column("Genre", justify="right", style="cyan", ratio=5)
        table.add_column(
            "Position", justify="right", style="cyan", ratio=5
        )

        if self.players is None:
            table.add_row("Vide", "Vide", "Vide", "Vide")
            return table

        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}
        sorted_players = sorted(
            self.players,
            key=lambda p: p.position
        )
        index = 1
        for player in sorted_players:
            table.add_row(
                "%s %s" % (player.last_name, player.first_name),
                player.birthday.strftime("%d/%m/%Y"),
                genre_display[player.gender],
                str(player.position),
            )
            index += 1

        return table
