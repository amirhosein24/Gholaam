
from duckduckgo_search import DDGS

from trafilatura import fetch_url, extract
from threading import Thread, Lock

from credentials import creds
from groqapi import llama
llama = llama.Llama3(api_key=creds.GroqApiToken)

prompt = "is halsy sick ?"

search_prompt = llama.create_search_code(prompt)
print(search_prompt)

results = DDGS().text(search_prompt, max_results=4)
print(len(results), "searchoooo")
internet_content = dict()


def get_to_dict(numb, data):
    with Lock():
        internet_content[str(numb)] = data


def export_data(link__):
    downloaded = fetch_url(link__)
    result = extract(downloaded).replace("\n", " ").replace("  ", " ")
    result = llama.date_handler(f"title : {prompt}\ndata : {result}")
    return result


threads = []


def gogo(number, linker):
    try:
        newdata = export_data(linker)
        get_to_dict(number, newdata)
    except:
        print("erorreddd")

for num, link in enumerate(results):

    thread = Thread(target=gogo, args=(num, link["href"], ))
    threads.append(thread)
    print(num, link["href"])
    thread.start()


for thread in threads:
    print("wowwwwww")
    thread.join()



# print(internet_content)


answer = llama.ask_llama70(f"title: {prompt}\ndata: {internet_content}")

print("----------------------")
print(answer)







