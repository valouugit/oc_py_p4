from datetime import datetime
from typing import List
from tinydb import TinyDB
import rich.prompt as Prompt

from model.player import Player
from model.gender import Gender


class PlayerMaker:
    def __init__(self) -> None:
        self.players = []

    def get_players(self) -> List[Player]:
        pass

    def add_player(self, save: bool = False) -> Player:
        genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}
        p_first_name = Prompt.Prompt.ask("Prénom du joueur")
        p_last_name = Prompt.Prompt.ask("Nom du joueur")
        p_birthday = Prompt.Prompt.ask("Date d'anniversaire (DD/MM/AAAA)")
        p_gender = Prompt.Prompt.ask(
            "Genre", choices=[genre_display[Gender.MAN], genre_display[Gender.WOMAN]]
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

        if save:
            self.players.append(player)

        return Player
