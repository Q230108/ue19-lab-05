import requests


def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"  # URL de l'API de blagues
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "single":
            print(joke["joke"])
        else:
            print(joke["setup"])
            print(joke["delivery"])
    else:
        print("Erreur lors de la récupération de la blague.")


if __name__ == "__main__":
    get_joke()
