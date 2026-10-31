import requests
import sys
import json
import random
import statistics

collected = []


def main():
    print("""
=== Quote Analyzer ===

1. Get a random quote
2. Get multiple quotes
3. Analyze collected quotes
4. Save quotes
5. Load quotes
6. Exit
""")

    options()


def options():
    while True:
        option = input("Choose an option: ")

        if option == "1":
            random_quotes()
        elif option == "2":
            multiple_quotes()
        elif option == "3":
            analyze_quotes()
        elif option == "4":
            save_quotes()
        elif option == "5":
            load_quotes()
        elif option == "6":
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid option.")


def random_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()[0]

    clean_quote = {
        "quote": quote["q"],
        "author": quote["a"]
    }

    collected.append(clean_quote)

    print(f"'{clean_quote['quote']}'")
    print(f"-{clean_quote['author']}")


def multiple_quotes():
    try:
        count = int(input("How many quotes would you like to retrieve? "))
        if count <= 0:
            print("Please enter a number greater than 0.")
            return
        elif count > 50:
            print("You cannot request more than 50 quotes.")
            return
    except ValueError:
        print("Type in numbers!")
        return
    response = requests.get("https://zenquotes.io/api/quotes")
    quotes = random.sample(response.json(), count)

    for quote in quotes:
        clean_quote = {
            "quote": quote["q"],
            "author": quote["a"]
        }

        collected.append(clean_quote)

        print(f"'{clean_quote['quote']}'")
        print(f"-{clean_quote['author']}")


def analyze_quotes():
    lengths = [len(quote["quote"]) for quote in collected]

    total = len(collected)
    shortest = min(lengths) if lengths else 0
    longest = max(lengths) if lengths else 0
    avg = statistics.mean(lengths) if lengths else 0

    print(f"""
========= Analysis =========

Total quotes collected: {total}
Shortest quote: {shortest} characters
Longest quote: {longest} characters
Average quote length: {avg} characters
""")


def save_quotes():
    filename = input("Enter the save file name: ") + ".json"
    if len(filename) <= 10:
        print("Filename must be longer than 5 characters.")
        return
    elif len(filename) > 50:
        print("Please choose a shorter name")
        return

    with open(filename, "w") as file:
        json.dump(collected, file, indent=4, ensure_ascii=False)

    print(f"Quotes saved to {filename}.")


def load_quotes():
    filename = input("Enter the load file name: ") + ".json"
    try:
        with open(filename, "r") as file:
            loaded_quotes = json.load(file)
            collected.extend(loaded_quotes)
        print(f"Loaded {len(loaded_quotes)} quotes from {filename}.")
    except FileNotFoundError:
        print("File doesn't exist!")


main()