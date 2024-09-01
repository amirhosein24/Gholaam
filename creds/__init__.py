
def load_json():

    from os import path
    home_path = path.dirname(path.dirname(__file__)) + "/"

    from json import load
    with open(home_path + "creds/creds.json", encoding='utf-8') as file:
        config = load(file)
        groq_api = config["groq_apikey"]

    return groq_api, home_path


GroqApiToken, HomePath = load_json()
del load_json
