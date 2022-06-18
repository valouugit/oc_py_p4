from datetime import datetime
from typing import List
from tinydb import TinyDB
import rich.prompt as Prompt

from model.player import Player
from model.gender import Gender


class PlayerMaker:
    def __init__(self) -> None:
        self.players = []
        self.db = TinyDB("data/players.json")
        self.genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}

    def add_player(self) -> Player:
        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}
        p_first_name = Prompt.Prompt.ask("Prénom du joueur")
        p_last_name = Prompt.Prompt.ask("Nom du joueur")
        p_birthday = Prompt.Prompt.ask("Date d'anniversaire (DD/MM/AAAA)")
        p_gender = Prompt.Prompt.ask(
            "Genre", choices=[
                genre_display[Gender.MAN],
                genre_display[Gender.WOMAN]
            ]
        )
        p_position = Prompt.IntPrompt.ask("Position")

        player = Player(
            first_name=p_first_name,
            last_name=p_last_name,
            birthday=datetime.strptime(p_birthday, "%d/%m/%Y"),
            gender=list(genre_display.keys())[
                list(genre_display.values()).index(p_gender)
            ],
            position=p_position,
        )

        return player

    def save_player(self, player: Player):
        self.db.insert(
            {
                "first_name": player.first_name,
                "last_name": player.last_name,
                "birthday": player.birthday.strftime("%d/%m/%Y"),
                "gender": self.genre_display[player.gender],
                "position": player.position,
            }
        )

    def load_user(self) -> List[Player]:
        players = []
        for player in self.db.all():
            players.append(
                Player(
                    first_name=player["first_name"],
                    last_name=player["last_name"],
                    birthday=datetime.strptime(
                        player["birthday"],
                        "%d/%m/%Y"
                    ),
                    gender=list(self.genre_display.keys())[
                        list(self.genre_display.values())
                        .index(player["gender"])
                    ],
                    position=player["position"],
                )
            )

        return players
