
from groq import Groq


class Llama3:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def ask_llama(self, prompt, model="llama3-70b-8192") -> str:

        chat_completion = self.client.chat.completions.create(

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )

        return chat_completion.choices[0].message.content
