import os

import click
import requests

import giphyAPI
import giphyCLI


@click.group()
def gif():
    print("hello from giphy cli!")
    API_KEY = os.environ["GIPHY_API_KEY"]
    result = requests.get(
        f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=25&offset=0&rating=g"
    )
    gifs = result.json()
    print(gifs)


@gif.command()
def trending():
    print("trending subcommand called!")


@gif.command()
def search():
    print("search subcommand called!")


if __name__ == "__main__":
    gif()
