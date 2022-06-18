from datetime import datetime
from typing import List
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from model.gender import Gender
from model.player import Player

from model.tournament import Tournament


class TournamentView:
    def __init__(
        self,
        console: Console,
        tournament: Tournament = None
    ):
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
            Layout(name="commands"),
            Layout(name="players"),
            Layout(name="rounds")
        )
        layout["margin"].update(Text())
        layout["header"].update(self._get_header())
        layout["commands"].update(self._get_commands())
        layout["players"].update(self._get_players())
        layout["rounds"].update(self._get_rounds())

        self.console.print(layout)

    def show_players(self, players: List[Player]):
        layout = Layout()
        layout.split_column(
            Layout(name="margin", size=3),
            Layout(name="players"),
        )
        layout["margin"].update(Text())
        layout["players"].update(self._get_players_parents(players))
        self.console.print(layout)

    def _get_header(self) -> Table:
        table = Table(
            title=self.tournament.name,
            expand=True,
        )
        table.add_column("Description", justify="right", style="cyan")
        table.add_column("Lieu", justify="right", style="cyan")
        table.add_column("Date", justify="right", style="cyan")
        table.add_column("Type de timer", justify="right", style="cyan")
        table.add_column(
            "Nombre de rounds réalisés", justify="right", style="cyan"
        )
        table.add_column(
            "Nombre de rounds", justify="right", style="cyan"
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

    def _get_commands(self) -> Table:
        table = Table(
            title="Commande",
            expand=True,
        )
        table.add_column(
            "Commande", justify="right", style="cyan", ratio=1
        )
        table.add_column("Action", justify="right", style="cyan", ratio=5)

        table.add_row("0", "Retour")
        table.add_row("1", "Nouveau joueur")
        table.add_row("2", "Ajouter un joueur")
        table.add_row("3", "Ajouter un tour")
        table.add_row("4", "Voir un round")
        table.add_row("5", "Sauvegarder le tournois")
        table.add_row("6", "Changer les positions")
        table.add_row("7", "Voir les matchs")

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

        if len(self.tournament.players) == 0:
            table.add_row("Vide", "Vide", "Vide", "Vide")
            return table

        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}
        sorted_players = sorted(
            self.tournament.players,
            key=lambda p: p.position
        )
        index = 1
        for player in sorted_players:
            if type(player.birthday) is float:
                b = datetime.fromtimestamp(
                        player.birthday
                    ).strftime(
                        "%d/%m/%Y"
                    )
            else:
                b = player.birthday.strftime("%d/%m/%Y")
            table.add_row(
                "%s %s" % (player.last_name, player.first_name),
                b,
                genre_display[player.gender],
                str(player.position),
            )
            index += 1

        return table

    def _get_rounds(self) -> Table:
        table = Table(
            title="Tours",
            expand=True,
        )
        table.add_column("Numéro", justify="right", style="cyan", ratio=5)
        table.add_column("Nom", justify="right", style="cyan", ratio=5)
        table.add_column(
            "Date de début", justify="right", style="cyan", ratio=5
        )
        table.add_column(
            "Date de fin", justify="right", style="cyan", ratio=5
        )

        if len(self.tournament.rounds) == 0:
            table.add_row("Vide", "Vide", "Vide", "Vide")
            return table

        index = 1
        for round in self.tournament.rounds:
            table.add_row(
                str(index),
                round.name,
                round.date_start.strftime("%d/%m/%Y"),
                round.date_end.strftime("%d/%m/%Y"),
            )
            index += 1

        return table

    def _get_players_parents(self, players: List[Player]) -> Table:
        table = Table(
            title="Joueurs",
            expand=True,
        )
        table.add_column("Numéro", justify="right", style="cyan", ratio=5)
        table.add_column("Nom", justify="right", style="cyan", ratio=5)
        table.add_column(
            "Date d'anniversaire", justify="right", style="cyan", ratio=5
        )
        table.add_column("Genre", justify="right", style="cyan", ratio=5)
        table.add_column(
            "Position", justify="right", style="cyan", ratio=5
        )

        if len(players) == 0:
            table.add_row("Vide", "Vide", "Vide", "Vide")
            return table

        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}

        index = 1
        for player in players:
            if type(player.birthday) is float:
                b = datetime.fromtimestamp(
                        player.birthday
                    ).strftime(
                        "%d/%m/%Y"
                    )
            else:
                b = player.birthday.strftime("%d/%m/%Y")
            table.add_row(
                str(index),
                "%s %s" % (player.last_name, player.first_name),
                b,
                genre_display[player.gender],
                str(player.position),
            )
            index += 1

        return table
