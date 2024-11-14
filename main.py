import requests
import json

cat_fact = requests.get("https://catfact.ninja/fact")

# 200 response code means success.
if cat_fact.status_code == 200:
    cat_fact_dict = json.loads(cat_fact.text)

    # this will be the number of vowels after the loop.
    cat_fact_vowels = 0

    for i in cat_fact_dict.get("fact"):
        # All the vowels.
        vowels = "aeiou"

        # We convert it to lower case cause vowels are lower case also.
        if i.lower() in vowels:
            cat_fact_vowels += 1

    print(f"there are {cat_fact_vowels} vowels in fact: {cat_fact_dict.get("fact")}")
else:
    print(f"ERROR: Could not search for cat facts please try again later.")


dollars = input("Please enter dollars to convert: ")
bitcoin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Make sure you give us a number in dollars input.
if dollars.isdigit() and bitcoin_info.status_code == 200:
    bitcoin_info_dict = json.loads(bitcoin_info.text)

    # Get the exchange rate that is nested in the json.
    exchange_rate = bitcoin_info_dict["bpi"]["USD"]["rate"]

    # We replace commas because we don't want to denote thousands for float conversion.
    exchange_rate = exchange_rate.replace(",", "")

    # Divide money by exchange rate to get the bitcoin count.
    bitcoin = float(dollars) / float(exchange_rate)

    print(f"You have {bitcoin} bitcoin")
else:
    print(f"ERROR: Could not convert {dollars} to bitcoin please try again.")


name = input("Please enter your name: ")
name_age_info = requests.get(f"https://api.agify.io/?name={name}")

if name_age_info.status_code == 200:
    name_age_info_dict = json.loads(name_age_info.text)

    age = name_age_info_dict.get("age")

    # It will return None if our name does not exist.
    if age is None:
        print(f"No name {name} in database")
    else:
        print(f"name {name} is {age} years old")
else:
    print(f"ERROR: Could not search for your name in the database please try again later.")