import os
import requests
import logging

from utils import bytes_to_dict
from igdb.wrapper import IGDBWrapper

IGDB_CLIENT_ID = os.getenv("IGDB_CLIENT_ID")
IGDB_CLIENT_SECRET = os.getenv("IGDB_CLIENT_SECRET")


class IGDBService:
    def __init__(self) -> None:
        self.authorize()
        self.client = IGDBWrapper(IGDB_CLIENT_ID, self.access_token)

    def authorize(self):
        response = requests.post(
            f"https://id.twitch.tv/oauth2/token?client_id={IGDB_CLIENT_ID}&client_secret={IGDB_CLIENT_SECRET}&grant_type=client_credentials"
        )
        response.raise_for_status()
        jsonResponse = response.json()
        logging.info("Authorized IGDB successfully")
        self.access_token = jsonResponse["access_token"]

    def search(self, query: str):
        byte_array = self.client.api_request(
            "search", f'search "{query}"; fields game; limit 5;'
        )
        return bytes_to_dict(byte_array)

    def games(self, ids):
        game_ids = ",".join(map(str, ids))
        byte_array = self.client.api_request(
            "games", f"where id=({game_ids}); fields id, cover, name ;"
        )
        return bytes_to_dict(byte_array)
