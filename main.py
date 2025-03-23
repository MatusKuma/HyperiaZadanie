from models.parser import FlyerParser
from utils.utils import save_flyers_to_json
import time
import logging
import log_config

def main():
    log_config.setup_logging()
    logging.info("Starting the application...") 
    logging.info("Parsing started...")
    
    start_time = time.time()
    
    parser = FlyerParser()
    all_flyers = parser.parse_all_flyers()
    save_flyers_to_json(all_flyers)

    end_time = time.time()
    elapsed_time = end_time - start_time 
    logging.info(f"Parsing completed in {elapsed_time:.2f} seconds.")

    for shop_flyers in all_flyers:
        shop_name = shop_flyers[0].shop_name if shop_flyers else "Unknown"
        flyer_count = len(shop_flyers)
        logging.info(f"{shop_name} : {flyer_count}")

if __name__ == "__main__":
    main()
