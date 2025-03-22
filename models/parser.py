import requests
from models.flyer import Flyer
from typing import List, Dict, Optional
from bs4 import BeautifulSoup, Tag
from datetime import datetime
import re

class FlyerParser:
    BASE_URL = "https://www.prospektmaschine.de"

    def fetch_html(self, endpoint: str) -> Optional[str]:
        """ Fetches HTML content from a given endpoint. """
        try:
            response = requests.get(self.BASE_URL + endpoint, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {endpoint}: {e}")
            return None

    def parse_hypermarket_names(self) -> Dict[str, str]:
        """ Parses hypermarket names and their respective URLs. """
        html = self.fetch_html("/hypermarkte/")
        if not html:
            return {}

        soup = BeautifulSoup(html, "html.parser")
        hypermarket_info: Dict[str, str] = {}

        list_of_hypermarkets = soup.find("ul", id="left-category-shops")
        if list_of_hypermarkets:
            for li in list_of_hypermarkets.find_all("li"):
                a_tag = li.find("a")
                if a_tag and "href" in a_tag.attrs:
                    hypermarket_info[a_tag["href"]] = a_tag.text.strip()

        return hypermarket_info

    def parse_flyers_from_shop(self, endpoint: str, shop_name: str) -> List[Flyer]:
        """ Parses all flyers from a given shop and filters only valid ones. """
        html = self.fetch_html(endpoint)
        if not html:
            return []

        soup = BeautifulSoup(html, "html.parser")
        flyer_list: List[Flyer] = []
        flyers_div = soup.find("div", class_="page-body")
        for flyer_tag in flyers_div.find_all("div", class_="brochure-thumb"):
            flyer = Flyer(shop_name)
            flyer = self.fill_flyer_with_info(flyer_tag, flyer)

            if self.is_flyer_valid(flyer):
                flyer_list.append(flyer)

        return flyer_list

    def fill_flyer_with_info(self, html: Tag, flyer: Flyer) -> Flyer:
        """ Extracts and fills flyer information from HTML. """
        try:
            description = html.find("div", class_="letak-description")
            if not description:
                return flyer

            flyer.thumbnail = self.extract_thumbnail(html)

            title = description.find("strong")
            flyer.title = title.text.strip() if title else "Unknown"

            date_info = description.find("small")
            if date_info:
                dates = date_info.text.strip().split(" - ")
                flyer.valid_from = self.format_date(dates[0]) if len(dates) > 0 else "Unknown"
                flyer.valid_to = self.format_date(dates[1]) if len(dates) > 1 else "Unknown"
            else:
                flyer.valid_from = "Unknown"
                flyer.valid_to = "Unknown"

            flyer.set_parsed_time()
        except Exception as e:
            print(f"Error parsing flyer: {e}")

        return flyer

    def extract_thumbnail(self, html: Tag) -> str:
        """ Extracts a valid thumbnail URL from HTML. """
        thumbnail = html.find("img")
        if thumbnail:
            img_url = thumbnail.get("data-src", thumbnail.get("src", ""))
            match = re.search(r"(https?://.*?\.jpg)", img_url)
            return match.group(1) if match else img_url
        return ""

    def format_date(self, date_str: str) -> str:
        """ Converts date from 'DD. MM. YYYY' format to 'YYYY-MM-DD'. """
        match = re.search(r"(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})", date_str)
        return f"{match.group(3)}-{int(match.group(2)):02d}-{int(match.group(1)):02d}" if match else "Unknown"

    def is_flyer_valid(self, flyer: Flyer) -> bool:
        """ Checks if the flyer is valid based on date range. """
        now = datetime.now().date()

        try:
            valid_from = datetime.strptime(flyer.valid_from, "%Y-%m-%d").date()
            valid_to = datetime.strptime(flyer.valid_to, "%Y-%m-%d").date()
            return valid_from <= now <= valid_to
        except ValueError:
            return False

    def parse_all_flyers(self) -> List[List[Flyer]]:
        """ Parses all flyers from all hypermarkets and filters valid ones. """
        list_of_flyers: List[List[Flyer]] = []
        hypermarkets = self.parse_hypermarket_names()

        for endpoint, shop_name in hypermarkets.items():
            flyers = self.parse_flyers_from_shop(endpoint, shop_name)
            if flyers:
                list_of_flyers.append(flyers)

        return list_of_flyers
