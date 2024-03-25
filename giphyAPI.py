import os

import requests


class GiphyAPI:

    API_KEY = os.environ["GIPHY_API_KEY"]

    # constructs and returns a dictionary of trending gifs
    def getTrendingGifs(self):
        result = requests.get(
            "https://api.giphy.com/v1/gifs/trending?api_key="
            + f"{self.API_KEY}&limit=25&offset=0&rating=g"
        )
        gifs = result.json()
        return gifs

    # constructs and returns a dictionary of gifs based on the search term
    def getSearchGifs(self, searchterm):
        result = requests.get(
            "https://api.giphy.com/v1/gifs/search?api_key="
            + f"{self.API_KEY}&q={searchterm}&limit=25&offset=0&rating=g"
        )
        gifs = result.json()
        return gifs
