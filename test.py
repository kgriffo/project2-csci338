import os
import unittest

from giphyAPI import GiphyAPI
from giphyCLI import GiphyCLI

API_KEY = os.environ["GIPHY_API_KEY"]

api = GiphyAPI()
cli = GiphyCLI()


# API tests
class TestAPI(unittest.TestCase):
    # tests to ensure the API is returning the gif info in dictionary format
    def test_get_trending_gifs(self):
        # ChatGPT told me about the isinstance method
        self.assertTrue(
            isinstance(api.getTrendingGifs(), dict),
            "getTrendingGifs did not return a dictionary",
        )

    def test_get_search_gifs(self):
        searchterm = "cats"
        self.assertTrue(
            isinstance(api.getSearchGifs(searchterm), dict),
            "getSearchGifs did not return a dictionary",
        )

    # test to ensure the API is grabbing the right amount of gifs
    def test_dict_lens(self):
        searchterm = "cats"
        trendingGifs = api.getTrendingGifs()
        searchGifs = api.getSearchGifs(searchterm)
        # get the number of gifs
        numTrendingGifs = len(trendingGifs["data"])
        numSearchGifs = len(searchGifs["data"])
        self.assertTrue(numTrendingGifs == 25, f"gif dict is {numTrendingGifs} long")
        self.assertTrue(numSearchGifs == 25, f"gif dict is {numSearchGifs} long")


# CLI tests
class TestCLI(unittest.TestCase):
    pass

  
if __name__ == "__main__":
    unittest.main()
