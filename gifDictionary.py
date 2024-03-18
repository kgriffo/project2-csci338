import requests

def main():
    result = requests.get("https://api.giphy.com/v1/gifs/trending?api_key=frUdMjsYJxj0gyHTP94XuDOnVodkPuY0&limit=25&offset=0&rating=g")
    gifs = result.json()

    print(gifs)

if __name__ == "__main__":
    main()