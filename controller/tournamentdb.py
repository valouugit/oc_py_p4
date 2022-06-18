import json
from typing import List
from tinydb import TinyDB, Query

from model.gender import Gender
from model.tournament import Tournament


class TournamentDb:
    def __init__(self) -> None:
        self.players = []
        self.db = TinyDB("data/tournaments.json")
        self.genre_display = {Gender.MAN: "Homme", Gender.WOMAN: "Femme"}

    def save_tournament(self, tournament: Tournament):
        tournament_query = Query()
        if len(self.db.search(tournament_query.name == tournament.name)) == 0:
            self.db.insert(json.loads(tournament.to_json()))
        else:
            self.db.update(
                json.loads(tournament.to_json()),
                tournament_query.name == tournament.name,
            )

    def load_tournament(self) -> List[Tournament]:
        tournaments_db = self.db.all()
        tournaments = []
        for tournament in tournaments_db:
            tournaments.append(Tournament.from_dict(tournament))
        return tournaments
