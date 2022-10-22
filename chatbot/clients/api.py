
import os
import httpx
from pydantic import BaseModel


class Team(BaseModel):
    uid: int
    name: str
    description: str


class PlayerClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/players'


class TeamClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/teams'

    def get_all(self) -> list[Team]:
        response = httpx.get(url=f'{self.url}/')
        response.raise_for_status()
        teams = response.json()
        return [Team(**team) for team in teams]


class ApiClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.players = PlayerClient(url)
        self.teams = TeamClient(url)


client = ApiClient(os.environ['API_URL'])
