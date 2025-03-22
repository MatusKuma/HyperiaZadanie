from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Flyer:
    shop_name: str
    title: str = field(default="")
    thumbnail: str = field(default="")
    valid_from: str = field(default="")
    valid_to: str = field(default="")
    parsed_time: str = field(default="")

    def set_parsed_time(self):
        """ Nastaví čas, keď sa leták parsuje. """
        self.parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
