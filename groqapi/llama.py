
from groq import Groq


class Llama3:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def ask_llama70(self, prompt, model="llama3-70b-8192") -> str:

        chat_completion = self.client.chat.completions.create(

            messages=[
                {
                    "role": "system",
                    "content": "you are a helpfull assistant, dont say its based on sth or etc"
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content

    def ask_llama8(self, prompt, model="llama3-8b-8192") -> str:
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

    def date_handler(self, prompt, model="llama3-8b-8192") -> str:
        chat_completion = self.client.chat.completions.create(

            messages=[
                {
                    "role": "system",
                    "content": "do not answer the title from the user, only re-print the given data but remove the irrelevant data to title"  # , basicly you should shorten the text with out changing it (dont remove the important data)"
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content

    def create_search_code(self, prompt, model="llama3-70b-8192") -> str:
        chat_completion = self.client.chat.completions.create(

            messages=[
                {
                    "role": "system",
                    "content": "dont asnwer the prompt, rewrite it in a simple way so it can be use in a search engine like duckduckgo, dont write any explanation or anything else"
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content
