from dataclasses import dataclass
import datetime
@dataclass
class Flyer:
    
    def __init__(self, title, shop_name, thumbnail, valid_from, valid_to):
        self.title = title
        self.thumbnail = thumbnail
        self.shop_name = shop_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.parsed_time = datetime.datetime.now()

    

    title: str
    thumbnail: str
    shop_name: str
    valid_from: datetime
    valid_to: datetime
    parsed_time: datetime
