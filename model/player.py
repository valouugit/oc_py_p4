from dataclasses import dataclass

from model.gender import Gender


@dataclass
class Player:
    first_name: str
    last_name: str
    birthday: str
    gender: Gender
    position: int

    def get_name(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)
