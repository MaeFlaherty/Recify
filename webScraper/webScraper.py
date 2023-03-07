from bs4 import BeautifulSoup
import json
from urllib.request import urlopen, Request
import sys
#import web

ok = False
#Creates a fake browser visit to avoid 403 forbidden errors
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"}

# 
def get_ld_json(url: str) -> dict:
    parser = "html.parser"
    req = Request(url, headers = headers)
    html = urlopen(req)
    soup = BeautifulSoup(html, parser)
    return json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))




if __name__ == "__main__":
    url = input("enter site URL: ")

    data = get_ld_json(url)

    ingredients = data["recipeIngredient"]

    instructions = data["recipeInstructions"]

    print("\n" + data["name"] + "\n")

    print ("<h2>*****INGREDIENTS*****<h2>")
    for count, ing in enumerate(ingredients):
        print(ing + "\n")

    print ("<h2>*****INSTRUCTIONS*****<h2>")
    for count, inst in enumerate(instructions):
        print(f"{count}. \n" + instructions[count]["text"] + "\n")



