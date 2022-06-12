from enum import Enum, auto


class Command(Enum):
    NO_COMMAND = auto()
    BACK = auto()
    TOURNAMENT_ADD = auto()
    TOURNAMENT_VIEW = auto()
    PLAYER_ADD = auto()
