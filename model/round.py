from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Round:
    name: str
    match: List[tuple]
    date_start: datetime
    date_end: datetime
