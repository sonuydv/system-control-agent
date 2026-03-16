from groq import Groq

from env_helper import config

client = Groq(
    api_key=config.GROQ_API_KEY
)

def ask_llm(messages:str,tools_schema,tool_calls:str='auto'):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        tools=tools_schema,
        tool_choice=tool_calls
    )
    return response.choices[0].message
