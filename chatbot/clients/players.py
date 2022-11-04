import httpx

from chatbot.clients.schemas import Injury, Player


class PlayerClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/players'

    def find_by_name(self, name: str) -> list[Player]:
        response = httpx.get(
            url=f'{self.url}/',
            params={'name': name},
        )
        response.raise_for_status()
        players = response.json()
        return [Player(**player) for player in players]

    def get_injuries(self, player_id: int) -> list[Injury]:
        response = httpx.get(url=f'{self.url}/{player_id}/injuries/')
        response.raise_for_status()
        injuries = response.json()
        return [Injury(**injury) for injury in injuries]
