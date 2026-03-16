from tools import TOOLS
import json

def execute_tools(tool_calls):

    results = []

    for call in tool_calls:

        tool_name = call.function.name

        args = call.function.arguments

        if args:
            args = parse_args(args)
        else:
            args = {}

        tool = TOOLS.get(tool_name)

        if not tool:
            results.append(f"Tool {tool_name} not found")
            continue

        output = tool(**args)

        results.append(f"{output}")

    return "\n\n".join(results)

def parse_args(raw_args):

    if not raw_args:
        return {}

    try:
        args = json.loads(raw_args)

        if args is None:
            return {}

        return args

    except Exception as e:
        return {}