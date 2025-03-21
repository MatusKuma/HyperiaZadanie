import requests
from models.flyer import Flyer
from typing import List
from bs4 import BeautifulSoup

class FlyerParser:
    BASE_URL = "https://www.prospektmaschine.de/hypermarkte/"

    def fetch_html(self) -> str:
        response = requests.get(self.BASE_URL)
        response.raise_for_status()
        return response.text

    def parse_flyers(self, html: str) -> List[Flyer]:
        soup = BeautifulSoup(html, "html.parser")
        flyers = []

        # TODO: parsing logic

        return flyers