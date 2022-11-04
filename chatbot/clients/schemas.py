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
