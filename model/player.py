from dataclasses import dataclass

from model.gender import Gender


@dataclass
class Player:
    first_name: str
    last_name: str
    birthday: str
    gender: Gender
    position: int
