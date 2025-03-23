# Flyer Parser

## Popis
Flyer Parser je aplikácia na extrakciu informácií o letákoch z webovej stránky [prospektmaschine.de](https://www.prospektmaschine.de). Aplikácia načíta údaje o letákoch zo stránok hypermarketov a uloží ich do formátu JSON.

## Funkcionalita
- Parsovanie hypermarketov a ich letákov.
- Extrakcia relevantných informácií (názov, platnosť, thumbnail).
- Uloženie extrahovaných letákov do súboru vo formáte JSON.
- Logovanie udalostí a chýb do log súboru.

## Požiadavky
- Python 3.6 alebo vyšší
- Knižnice:
  - `requests`
  - `beautifulsoup4`

## Inštalácia
1. Klonuj tento repozitár:
   ```bash
   git clone https://github.com/MatusKuma/HyperiaZadanie.git

2. Prejdi do adresára projektu:
   ```bash
   cd ./HyperiaZadanie/

3. Nainštaluj požadované knižnice:
   ```bash
   pip install -r requirements.txt

4. Spusti script:
   ```bash
   python main.py