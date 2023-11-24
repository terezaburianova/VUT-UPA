# Ukládání a příprava dat - Extrakce dat z webu
## Autoři:
Tým xharva03
* Tereza Burianová (xburia28)
* Mário Harvan (xharva03)

## E-shop:
Bike-Discount (https://www.bike-discount.de/en/)

## Obsah výstupu
* URL produktu
* Název produktu
* Cena produktu
* Materiál rámu
* Velikost kol
* Barva
* Hmotnost

## Spuštění skriptů:
* python3.10 get_urls.py - získá všechna URL ze 2 stran produktů
* python3.10 get_prods.py [soubor URL produktů] [počet zpracovaných produktů] - získá specifikaci produktů pro specifikovaný počet produktů ze specifikovaného souboru obsahujícího URL produktů (výchozí hodnoty: "urls.txt", všechna URL)
* build.sh - nainstaluje potřebné závislosti pomocí pip
* run.sh - spustí oba skripty se specifikací 10 produktů na výstupu
