import requests

key = "frUdMjsYJxj0gyHTP94XuDOnVodkPuY0"


def main():
    result = requests.get(
        f"https://api.giphy.com/v1/gifs/trending?api_key={key}&limit=25&offset=0&rating=g"
    )
    gifs = result.json()

    print(gifs)


if __name__ == "__main__":
    main()
