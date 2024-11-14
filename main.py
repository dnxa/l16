import requests
import json

cat_fact = requests.get("https://catfact.ninja/fact")

if cat_fact.status_code == 200:
    cat_fact_dict = json.loads(cat_fact.text)

    cat_fact_vowels = 0

    for i in cat_fact_dict.get("fact"):
        vowels = "aeiou"

        if i.lower() in vowels:
            cat_fact_vowels += 1


    print(f"there are {cat_fact_vowels} vowels in fact: {cat_fact_dict.get("fact")}")


dollars = input("Please enter dollars to convert: ")
bitcoin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if dollars.isdigit() and bitcoin_info.status_code == 200:
    bitcoin_info_dict = json.loads(bitcoin_info.text)

    exchange_rate = bitcoin_info_dict["bpi"]["USD"]["rate"]

    exchange_rate = exchange_rate.replace(",", "")

    bitcoin = float(dollars) / float(exchange_rate)

    print(f"You have {bitcoin} bitcoin")
