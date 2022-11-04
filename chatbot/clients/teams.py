import httpx

from chatbot.clients.schemas import Team


class TeamClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/teams'

    def get_all(self) -> list[Team]:
        response = httpx.get(url=f'{self.url}/')
        response.raise_for_status()
        teams = response.json()
        return [Team(**team) for team in teams]
