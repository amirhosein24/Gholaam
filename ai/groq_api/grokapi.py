from groq import Groq
token = "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"


# from groq import Groq

# client = Groq(
#     api_key=token,
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "یک مقاله پزشکی در مورد چشم انسان بنویس به زبان فارسی",
#         }
#     ],
#     model="llama3-70b-8192",
# )

# print(chat_completion.choices[0].message.content)


client = Groq(api_key=token)
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "story writer"
        },
        {
            "role": "user",
            "content": "write me a 50 word story about a alien cat"
        }
    ],
    temperature=1,
    max_tokens=8192,
    top_p=1,
    stream=False,
    stop=None,
)


print(completion.choices[0])

print("\n\n")

print(completion.usage)