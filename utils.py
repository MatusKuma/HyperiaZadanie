import json
from models.parser import FlyerParser

def save_flyers_to_json():
    parser = FlyerParser()
    all_flyers = parser.parse_all_flyers()

    output_flyers = []

    for shop_flyers in all_flyers:
        for flyer in shop_flyers:
            output_flyers.append({
                "title": flyer.title,
                "thumbnail": flyer.thumbnail,
                "shop_name": flyer.shop_name,  
                "valid_from": flyer.valid_from,
                "valid_to": flyer.valid_to,
                "parsed_time": flyer.parsed_time
            })

    with open("flyers.json", "w", encoding="utf-8") as json_file:
        json.dump(output_flyers, json_file, ensure_ascii=False, indent=4)