from models.parser import FlyerParser
from utils import save_flyers_to_json
import time

def main():
    print("Parsing started...")
    start_time = time.time()

    save_flyers_to_json()

    end_time = time.time()
    elapsed_time = end_time - start_time 
    print(f"Parsing completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()