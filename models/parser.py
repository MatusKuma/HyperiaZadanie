import requests
from models.flyer import Flyer
from typing import List, Dict
from bs4 import BeautifulSoup, Tag
from datetime import datetime
import re

class FlyerParser:
    BASE_URL = "https://www.prospektmaschine.de"

    def fetch_html(self, endpoint: str) -> str:
        response = requests.get(self.BASE_URL + endpoint)
        response.raise_for_status()
        return response.text

    def parse_hypermarket_names(self) -> Dict[str, str]:
        html = self.fetch_html("/hypermarkte/")
        soup = BeautifulSoup(html, "html.parser")
        hypermarket_info: Dict[str, str] = {}

        list_of_hypermarkets = soup.find("ul", id="left-category-shops")

        if list_of_hypermarkets:
            for li in list_of_hypermarkets.find_all("li"):
                a_tag = li.find("a")
                if a_tag and "href" in a_tag.attrs:
                    endpoint = a_tag["href"]
                    text = a_tag.text.strip()
                    hypermarket_info[endpoint] = text  

        return hypermarket_info

    def parse_flyers_from_shop(self, endpoint: str, shop_name: str) -> List[Flyer]:
        flyer_list: List[Flyer] = []
        html = self.fetch_html(endpoint)
        soup = BeautifulSoup(html, "html.parser")

        now = datetime.now().date()  

        for flyer_tag in soup.findAll("div", class_="brochure-thumb"):
            flyer = Flyer(shop_name)
            flyer = self.fill_flyer_with_info(flyer_tag, flyer)

            
            try:
                valid_from = datetime.strptime(flyer.valid_from, "%Y-%m-%d").date()
                valid_to = datetime.strptime(flyer.valid_to, "%Y-%m-%d").date()
            except ValueError:
                continue  

            
            if valid_from <= now <= valid_to:
                flyer_list.append(flyer)

        return flyer_list



    def fill_flyer_with_info(self, html: Tag, flyer: Flyer) -> Flyer:
        description = html.find("div", class_="letak-description")
        thumbnail = html.find("img")

        if thumbnail:
            flyer.thumbnail = thumbnail.get("data-src", thumbnail.get("src", ""))

        if flyer.thumbnail:
            match = re.search(r"(https?://.*?\.jpg)", flyer.thumbnail)
            if match:
                flyer.thumbnail = match.group(1)

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

        flyer.parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return flyer

    def format_date(self, date_str: str) -> str:
        match = re.search(r"(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})", date_str)
        if match:
            day, month, year = match.groups()
            return f"{year}-{int(month):02d}-{int(day):02d}"
        return "Unknown"
    
    def parse_all_flyers(self) -> List[List[Flyer]]:
        list_of_flyers: List[List[Flyer]] = []
        dict_of_shops = self.parse_hypermarket_names()

        for endpoint, shop_name in dict_of_shops.items():
            flyers = self.parse_flyers_from_shop(endpoint, shop_name)
            list_of_flyers.append(flyers)

        return list_of_flyers