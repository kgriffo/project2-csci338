import random

import click

from giphyAPI import GiphyAPI


class GiphyCLI:

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
        help="Prints gifs in markdown format",
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
        giphy_api = GiphyAPI()
        gifs = giphy_api.getTrendingGifs()
        # I wasn't very familiar with dictionaries,
        # so ChatGPT and Python documentation helped me figure out how to access the gif urls
        if lucky:
            random_gif = random.choice(gifs["data"])
            url = random_gif["bitly_gif_url"]
            md_url = random_gif["images"]["original"]["url"]
            title = random_gif["title"]
            if markdown:
                print(f"![{title}]({md_url})")
            else:
                print(f"{title} ({url})")
        else:
            number = 1  # used to number printed gifs
            for gif_data in gifs["data"][:count]:
                url = gif_data["bitly_gif_url"]
                md_url = gif_data["images"]["original"]["url"]
                title = gif_data["title"]
                if markdown:
                    print(f"{number}) ![{title}]({md_url})")
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
        help="Prints gifs in markdown format",
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
        giphy_api = GiphyAPI()
        gifs = giphy_api.getSearchGifs(searchterm)
        if lucky:
            random_gif = random.choice(gifs["data"])
            url = random_gif["bitly_gif_url"]
            md_url = random_gif["images"]["original"]["url"]
            title = random_gif["title"]
            if markdown:
                print(f"![{title}]({md_url})")
            else:
                print(f"{title} ({url})")
        else:
            number = 1  # used to number printed gifs
            for gif_data in gifs["data"][:count]:
                url = gif_data["bitly_gif_url"]
                md_url = gif_data["images"]["original"]["url"]
                title = gif_data["title"]
                if markdown:
                    print(f"{number}) ![{title}]({md_url})")
                else:
                    print(f"{number}) {title} ({url})")
                number += 1
