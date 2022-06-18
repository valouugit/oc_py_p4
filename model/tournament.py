from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime

from typing import List
from .round import Round
from .player import Player
from .timer import Timer


@dataclass_json
@dataclass
class Tournament:
    name: str
    location: str
    date: datetime
    timer: Timer
    rounds: List[Round]
    players: List[Player]
    description: str | None = None
    rounds_number: int = 4
