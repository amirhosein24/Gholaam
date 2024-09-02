
from os import path, remove

from groq import Groq

import creds

groq_client = Groq(api_key=creds.GroqApiToken)


def generate_text(prompt: str, system_prompt: str = "you are a helpfull assistant", model: str = "llama-3.1-70b-versatile") -> str:
    """
    use the groq api to generate text with prompt and system prompt
    """

    global groq_client

    try:
        chat_completion = groq_client.chat.completions.create(
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


def transcribe(file_path: str, model: str = "whisper-large-v3") -> str:
    """
    gets an audio file of max 25 mg and transcirbe it and then delets the file
    """

    global groq_client
    try:
        with open(file_path, "rb") as file:
            transcription = groq_client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model=model,
                response_format="verbose_json",
            )

            return transcription.text

    except Exception as error:
        print(error)
        return False

    finally:
        if path.isfile(file_path):
            print("file deleted")
            remove(file_path)
