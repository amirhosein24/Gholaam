
from groq import Groq


import json

token = "---"
client = Groq(api_key = token)
MODEL = 'llama3-70b-8192'



def get_time(counrty_name):

    if "iran" in counrty_name.lower():
        return "todays date in iran is 1402/03/24 and time is 11:25 AM"

    return "get time function unavailabe"



def run_conversation(user_prompt):
    
    messages=[
        {
            "role": "system",
            "content": "you are a helpfull assisstant with function calling ability, call the functions when more data is needed otherwise answer normally"
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
                "name": "get_time",
                "description": "function to get the date and time of a country",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "country_name": {
                            "type": "string",
                            "description": "name the country that you need its date and time",
                        }
                    },
                    "required": ["country_name"],
                },
            },
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=4096
    )

    
    response_message = response.choices[0].message
    
    print(response_message.content)
    tool_calls = response_message.tool_calls
    
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        available_functions = {
            "get_time": get_time,
        }
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            function_to_call = available_functions[function_name]

            function_response = function_to_call(
                counrty_name=function_args.get("country_name")
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )  # get a new response from the model where it can see the function response
        return second_response.choices[0].message.content

    else:
        return response


user_prompt = "say hi"
# user_prompt = "whats the time in iran ?"
print(run_conversation(user_prompt))

