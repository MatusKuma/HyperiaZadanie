import requests
from models.flyer import Flyer
from typing import List
from bs4 import BeautifulSoup

class FlyerParser:
    BASE_URL = "https://www.prospektmaschine.de/"

    def fetch_html(self) -> str:
        response = requests.get(self.BASE_URL+"hypermarkte/")
        response.raise_for_status()
        return response.text

    def parse_hypermarket_names(self, html: str) -> List[Flyer]:
        soup = BeautifulSoup(html, "html.parser")
        hypermarket_names = []

        list_of_hypermarkets = soup.find("ul", id="left-category-shops")
              
        for li in list_of_hypermarkets.find_all("li"):
            a_tag = li.find("a")
            if a_tag and a_tag.text:
                hypermarket_names.append(a_tag.text.strip())

        return hypermarket_names