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

TOOLS = {
    "control_service": control_service,
    "list_services": list_services
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
    }
]