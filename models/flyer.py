from dataclasses import dataclass, field
import datetime

@dataclass
class Flyer:
    shop_name: str
    title: str = field(default="")
    thumbnail: str = field(default="")
    valid_from: str = field(default="")
    valid_to: str = field(default="")
    parsed_time: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __init__(self, shop_name: str):
        self.shop_name = shop_name
