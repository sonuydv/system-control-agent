from app.sqlite_db import clear_all_chats
from env_helper import config
from sqlite_db import get_chat_history
from cmd_helpers import get_status, run_cmd
from services import SERVICES



def control_service(service, action):

    # Step 1: check service exists
    if service not in SERVICES:
        return f"Service '{service}' is not registered."

    # Step 2: check current status
    status = get_status(service)

    if action == "start":

        if status == "active":
            return f"{service} is already running."

        run_cmd(f"sudo systemctl start {service}")

    elif action == "stop":

        if status == "inactive":
            return f"{service} is already stopped."

        run_cmd(f"sudo systemctl stop {service}")

    elif action == "status":

        return f"{service} status: {status}"

    # Step 3: verify result
    final_status = get_status(service)

    return f"{service} executed '{action}'. Current status: {final_status}"

def list_services():

    services = "\n".join(SERVICES.keys())

    return f"""
Available services:

{services}

Actions available:
start <service>
stop <service>
status <status>
enable <service>
disable <service>
list services
"""



def get_rad_chats():
    return get_chat_history(config.TELEGRAM_ADMIN_USERNAME) or "no chat history found for rad bot"

def clear_all_chats():
    return  clear_all_chats()

TOOLS = {
    "control_service": control_service,
    "list_services": list_services,
    "get_rad_chats": get_rad_chats,
    "clear_all_chats" : clear_all_chats()
}

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "control_service",
            "description": "Control a service",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {"type": "string"},
                    "action": {
                        "type": "string",
                        "enum": ["start", "stop", "status"]
                    }
                },
                "required": ["service", "action"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_services",
            "description": "List available services",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_rad_chats",
            "description": "Get recent chat history of rad bot",
            "parameters": {"type": "object", "properties": {}}
        }
    },

    {
        "type": "function",
        "function": {
            "name": "clear_all_chats",
            "description": "clear or delete all chats",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]