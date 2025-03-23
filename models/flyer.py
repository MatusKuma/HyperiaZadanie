from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Flyer:
    """
    Represents a flyer with relevant information.

    Attributes:
        shop_name (str): The name of the shop where the flyer is from.
        title (str): The title of the flyer.
        thumbnail (str): The URL of the thumbnail image for the flyer.
        valid_from (str): The start date of validity for the flyer.
        valid_to (str): The end date of validity for the flyer.
        parsed_time (str): The time when the flyer was parsed.
    """
    
    shop_name: str
    title: str = field(default="")
    thumbnail: str = field(default="")
    valid_from: str = field(default="")
    valid_to: str = field(default="")
    parsed_time: str = field(default="")

    def set_parsed_time(self):
        """
        Sets the parsed_time attribute to the current date and time.

        This method formats the current date and time as a string
        in the format 'YYYY-MM-DD HH:MM:SS' and assigns it to the
        parsed_time attribute of the Flyer instance.

        Returns:
            None
        """
        self.parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
