
from groq import Groq


class Llama3:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def ask_llama(self, prompt: str, system_prompt: str = "you are a helpfull assistant", model: str = "llama3-70b-8192") -> str:

        chat_completion = self.client.chat.completions.create(

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

    def create_search_code(self, prompt: str, model="llama3-70b-8192") -> str:

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """You are a system that generates search queries optimized for DuckDuckGo. Your task is to convert user prompts into clear, concise, and highly relevant search queries that will yield the best search results. The output must be directly usable as search text in the DuckDuckGo search engine. Follow these guidelines:

Understand the Core Intent: Extract the main idea or question from the user prompt.
Use Keywords: Focus on the most important keywords and phrases related to the user's intent.
Be Concise: Keep the search query brief and to the point, avoiding unnecessary words (for example dont explain the output or dont say search query:).
Specificity: Add any relevant specifics or details to narrow down the search.
No Additional Text: Ensure the output is only the search query text, without any additional explanations or characters, dont answer the input but only convert it to search query.

Examples:
User Prompt: Tell me about the latest advancements in AI technology.
Search Query: latest advancements in AI technology

User Prompt: What are the best Italian restaurants in New York City?
Search Query: best Italian restaurants New York City

User Prompt: How do I fix a leaking faucet?
Search Query: how to fix leaking faucet guide

User Prompt: Who won the Nobel Prize in Literature in 2023?
Search Query: Nobel Prize in Literature 2023 winner

User Prompt: What are some good strategies for investing in stocks?
Search Query: good strategies for investing in stocks

Always prioritize accuracy and relevance in the generated search queries."""
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content

    def run_conversation(self, user_prompt):

        messages = [
            {
                "role": "system",
                "content": "you are a helpfull assisstant that can search the internet if more data is needed"
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ]
        tools = [

            {
                "type": "function",
                "function": {
                    "name": "start_search",
                    "description":  """this is a function that gets real time data from the internet, use this function when aditional data is needed""",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "search_text": {
                                "type": "string",
                                "description": """a query that goes in the search engine to get more data

Understand the Core Intent: Extract the main idea or question from the user prompt.
Use Keywords: Focus on the most important keywords and phrases related to the user's intent.
Be Concise: Keep the search query brief and to the point, avoiding unnecessary words (for example dont explain the output or dont say search query:).
Specificity: Add any relevant specifics or details to narrow down the search.
No Additional Text: Ensure the output is only the search query text, without any additional explanations or characters, dont answer the input but only convert it to search query.

Examples:
User Prompt: Tell me about the latest advancements in AI technology.
Search Query: latest advancements in AI technology

User Prompt: What are the best Italian restaurants in New York City?
Search Query: best Italian restaurants New York City

User Prompt: How do I fix a leaking faucet?
Search Query: how to fix leaking faucet guide

User Prompt: Who won the Nobel Prize in Literature in 2023?
Search Query: Nobel Prize in Literature 2023 winner

User Prompt: What are some good strategies for investing in stocks?
Search Query: good strategies for investing in stocks

Always prioritize accuracy and relevance in the generated search queries."""
                            }
                        },
                        "required": ["search_text"],
                    },
                },
            }
        ]

        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=8192
        )

        return response.choices[0].message
