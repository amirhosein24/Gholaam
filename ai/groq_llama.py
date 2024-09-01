
from os import path, remove

from groq import Groq

import creds

client = Groq(api_key=creds.GroqApiToken)


def generate_text(client, prompt: str, system_prompt: str = "you are a helpfull assistant", model: str = "llama-3.1-70b-versatile") -> str:
    """
    use the groq api to generate text with prompt and system prompt
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content

    except Exception as error:
        print(error)
        return False


def transcribe(client, file_path: str) -> str:
    """
    gets a audio file of max 25 mg and transcirbe it and then delets the file
    """

    try:
        with open(file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
            )

            print(transcription.text)
            return transcription.text

    except Exception as error:
        print(error)
        return False

    finally:
        if path.isfile(file_path):
            print("file deleted")
            remove(file_path)
