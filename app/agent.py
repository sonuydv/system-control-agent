from tool_executor import execute_tools
from tools import TOOLS_SCHEMA, TOOLS
from llm import ask_llm
from prompt_builder import build_system_prompt


def run_agent(user_input:str):
    system_prompt = build_system_prompt()
    prompt = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    msg = ask_llm(prompt,TOOLS_SCHEMA)
    print("LLM Response : ",msg)

    # If tool requested
    if msg.tool_calls:
        try:
            return execute_tools(msg.tool_calls)
        except Exception as e:
            print(f"\nError parsing tool calls: {e}")
            return "Sorry I couldn't understand your query! please tell me again"

    return msg.content

