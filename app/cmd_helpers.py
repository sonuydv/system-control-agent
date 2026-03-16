import subprocess

# Helper function to get service status
def get_status(service):

    cmd = f"sudo -n systemctl is-active {service}"

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()

# Helper function to run system commands
def run_cmd(cmd):

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout or result.stderr


