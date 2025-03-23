import json

def save_flyers_to_json(all_flyers):
    """
    Saves a list of parsed flyers to a JSON file.

    This function takes a nested list of `Flyer` objects, extracts relevant attributes,
    and stores them in a structured JSON format in a file named `flyers.json`.

    Args:
        all_flyers (List[List[Flyer]]): A list of lists, where each inner list contains
                                        `Flyer` objects for a specific shop.

    Returns:
        None

    The output JSON file has the following structure:
    [
        {
            "title": "Prospekt",
            "thumbnail": "https://example.com/image.jpg",
            "shop_name": "Kaufland",
            "valid_from": "2025-03-22",
            "valid_to": "2025-03-29",
            "parsed_time": "2025-03-23 10:42:14"
        },
        ...
    ]
    """
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

    with open("assets/flyers.json", "w", encoding="utf-8") as json_file:
        json.dump(output_flyers, json_file, ensure_ascii=False, indent=4)
