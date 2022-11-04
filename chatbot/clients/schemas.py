from enum import Enum

from pydantic import BaseModel
from datetime import datetime

class PlayerStatus(Enum):
    HEALTHY = 'healthy'
    INJURY = 'injury'


class Team(BaseModel):
    uid: int
    name: str
    description: str


class Player(BaseModel):
    name: str
    description: str
    uid: int
    team_id: int
    status: PlayerStatus


class Injury(BaseModel):
    uid: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime | None

    def display(self) -> str:
        dates = f'{self.start_date}-{self.end_date}' if self.end_date else self.start_date
        return f'{dates} {self.name}\n{self.description}'
