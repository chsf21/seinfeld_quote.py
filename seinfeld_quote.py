# Grabs a random Seinfeld quote from seinfeldism.com
import random
import requests
from bs4 import BeautifulSoup

# Keeps a list of seen quotes to prevent repitition. If all quotes have been seen, the set is cleared.
seen_quotes = set()

# Generate a random number to be used in the seinfeldism.com URL as the quote id
def gen_x():
    global x
    x = random.randrange(1, 2371)
    if x in seen_quotes:
        gen_x()
    else:
        seen_quotes.add(x)

def get_quote():
    global seen_quotes
    if len(seen_quotes) == 2371:
        seen_quotes.clear()
    gen_x()

    global url
    url = f"https://seinfeldism.com/seinfeld-quote.php?id={x}"
    page = requests.get(url)
    global page_text
    page_text = page.text

    parsed = BeautifulSoup(page_text, 'html.parser')
    body = parsed.find("p", class_="largequote")

    # Printing quote
    print()
    for child in body.children:
        if child.name == "br":
            print()
        elif child.name == "p":
            print()
            print()
            print(child.get_text(separator=" ", strip="True"))
        else:
            print(child.string, end=" ")
    print()

# Display the first quote
get_quote()

# Enter user input cycle
while True:
    response = input("Another? [Y/N] [L for link]: ")
    response_lower = response.lower()
    if response_lower == "y":
        get_quote()
    elif response_lower == "l":
        print(url)
    elif response_lower == "n":
        break
    else:
        print("Please enter a valid response.")
