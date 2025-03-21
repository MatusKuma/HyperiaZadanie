from models.parser import FlyerParser

def main():
    print("Parsing started...")
    parser = FlyerParser()
    html_text = parser.fetch_html()

    hypermarket_names = parser.parse_hypermarket_names(html_text)
    i=1
    for hypermarket in hypermarket_names:
        print(i, ".- ", hypermarket)
        i+=1

if __name__ == "__main__":
    main()