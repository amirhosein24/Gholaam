import ollama


def create_command(prompt, model):

    response = ollama.chat(model=model, messages=[
        {
            "role": "system",
            "content": "Act as a cmd code generator and generate pure cmd codes and don't say anything else"
        },
        {
            'role': 'user',
            'content': f"{prompt}",
        },
    ])

    return response['message']['content']


while True:

    print(create_command(input(">>> "), "llama3"))
