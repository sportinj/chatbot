
import os

from chatbot.clients.players import PlayerClient
from chatbot.clients.teams import TeamClient


class ApiClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.players = PlayerClient(url)
        self.teams = TeamClient(url)


client = ApiClient(os.environ['API_URL'])
