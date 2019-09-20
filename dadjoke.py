import requests
from pyfiglet import figlet_format as figform
from termcolor import colored as col
from random import randint

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
url = "https://icanhazdadjoke.com/search"

print(" ")
header = "Dad Joke (De)-Generator"
shade = valid_colors[randint(0, 6)]
text = col(figform(header), color=shade)
print(text)

fromUser = input("Ready for a dad joke? What topic would you want? ")

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": fromUser, "limit": 1}
)

data = response.json()

if data["total_jokes"] > 1:
    print("I've got " + str(data["total_jokes"]) + " jokes about " + fromUser + ". Here's one: ")
    print(data["results"][0]["joke"])
    print(" ")
    print(" ")
elif data["total_jokes"] > 0:
    print("I've got one joke about " + fromUser + ". Here it is: ")
    print(data["results"][0]["joke"])
    print(" ")
    print(" ")
else:
    print("Sorry, I don't have any jokes about " + fromUser + "! Please try again.")
    print(" ")
    print(" ")