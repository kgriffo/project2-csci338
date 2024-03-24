import os
import random

import click
import requests

# import giphyAPI
# import giphyCLI

API_KEY = os.environ["GIPHY_API_KEY"]


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
@click.option("--count", default=5, help="Number of gifs to print.")
@click.option(
    "--markdown",
    is_flag=True,
    show_default=True,
    default=False,
    help="Prints in markdown's image format",
)
@click.option(
    "--lucky",
    is_flag=True,
    show_default=True,
    default=False,
    help="Prints a random gif",
)
def trending(count, markdown, lucky):
    print("trending subcommand called!")
    result = requests.get(
        f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=25&offset=0&rating=g"
    )
    gifs = result.json()
    # I wasn't very familiar with dictionaries,
    # so ChatGPT and Python documentation helped me figure out how to access the gif urls
    if lucky:
        random_gif = random.choice(gifs["data"])
        url = random_gif["bitly_gif_url"]
        md_url = random_gif["images"]["preview_gif"]["url"]
        title = random_gif["title"]
        if markdown:
            print(f"![{title}]({md_url})")
        else:
            print(f"{title} ({url})")
    else:
        number = 1
        for gif_data in gifs["data"][:count]:
            url = gif_data["bitly_gif_url"]
            md_url = gif_data["images"]["preview_gif"]["url"]
            title = gif_data["title"]
            if markdown:
                print(f"![{title}]({md_url})")
            else:
                print(f"{number}) {title} ({url})")
            number += 1


@gif.command()
@click.option("--count", default=5, help="Number of gifs to print.")
@click.option(
    "--markdown",
    is_flag=True,
    show_default=True,
    default=False,
    help="Prints in markdown's image format",
)
@click.option(
    "--lucky",
    is_flag=True,
    show_default=True,
    default=False,
    help="Prints a random gif",
)
@click.argument("searchTerm")
def search(count, markdown, lucky, searchterm):
    print("search subcommand called!")
    result = requests.get(
        f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}"
        + f"&q={searchterm}&limit=25&offset=0&rating=g"
    )
    gifs = result.json()
    if lucky:
        random_gif = random.choice(gifs["data"])
        url = random_gif["bitly_gif_url"]
        md_url = random_gif["images"]["preview_gif"]["url"]
        title = random_gif["title"]
        if markdown:
            print(f"![{title}]({md_url})")
        else:
            print(f"{title} ({url})")
    else:
        number = 1
        for gif_data in gifs["data"][:count]:
            url = gif_data["bitly_gif_url"]
            md_url = gif_data["images"]["preview_gif"]["url"]
            title = gif_data["title"]
            if markdown:
                print(f"![{title}]({md_url})")
            else:
                print(f"{number}) {title} ({url})")
            number += 1


if __name__ == "__main__":
    gif()
