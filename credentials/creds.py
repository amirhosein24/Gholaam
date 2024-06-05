
def load_json():

    from os import path
    home = path.dirname(path.dirname(__file__)) + "/"

    from json import load
    with open(home + "credentials/creds.json", encoding='utf-8') as file:
        config = load(file)

    groq_api = config["groq_apikey"]

    return groq_api


GroqApiToken = load_json()
