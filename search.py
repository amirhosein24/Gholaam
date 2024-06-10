

import json
import concurrent.futures
from credentials import creds
from groqapi import llama


import trafilatura
from duckduckgo_search import DDGS
from threading import Lock


llama = llama.Llama3(api_key=creds.GroqApiToken)

# internet_content = []


def start_search(search_text: str) -> str:

    global internet_content
    internet_content = {}

    results = DDGS().text(search_text, max_results=3, safesearch='off', timelimit='y')
    print(len(results))

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        thread_list = []

        for id, result in enumerate(results):
            try:
                thread = executor.submit(
                    search_thread, id, result["href"], search_text)
                thread_list.append(thread)
            except Exception as error:
                print(
                    f"error in start_thread, id:{id}, result:{result}, error:{error}")

        concurrent.futures.wait(thread_list)

    return internet_content


def search_thread(id, link, title):
    fetch_data = trafilatura.fetch_url(link)
    plain_data = trafilatura.extract(
        fetch_data).replace("\n", " ").replace("  ", " ").replace("{", "").replace("{", "")

    plain_data = llama.ask_llama(f"title : {title}\ndata : {plain_data}",
                                 system_prompt="rewrite the date without unrelevant data to the title, make sure to only remove the unrelevant data from the title", model="llama3-70b-8192")
    print(id, link, plain_data)
    with Lock():
        internet_content[str(id)] = plain_data


prompt = "write me a short story on how hitler died?"


functions = {
    "start_search": start_search
}

answer = llama.run_conversation(prompt)
print(answer)

if answer.tool_calls:

    for tool in answer.tool_calls:
        print(tool.function.name)
        print(tool.function.arguments)

        arg = json.loads(tool.function.arguments)

        data = functions[tool.function.name](search_text=arg["search_text"])

        print(data)
print("----------------------")
