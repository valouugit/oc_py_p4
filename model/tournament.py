from dataclasses import dataclass
from typing import List, Optional
from .round import Round
from .player import Player
from .timer import Timer

@dataclass
class Tournament:
    name : str
    location : str
    date : str
    rounds : List[Round]
    players : List[Player]
    timer : Timer
    description : Optional[str] = None
    rounds_number : int = 4