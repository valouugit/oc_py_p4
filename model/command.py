from enum import Enum, auto


class Command(Enum):
    NO_COMMAND = auto()
    BACK = auto()
    TOURNAMENT_ADD = auto()
    TOURNAMENT_VIEW = auto()
    TOURNAMENT_SAVE = auto()
    PLAYER_ADD = auto()
    PLAYER_IMPORT = auto()
    ROUND_ADD = auto()
    ROUND_VIEW = auto()
    POSITION_CHANGE = auto()
    MATCH_VIEW = auto()
    CHANGE_SORT = auto()
