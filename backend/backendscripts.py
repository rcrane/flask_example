"""Module to seperate frontend form backend and to run scripts."""
import os
import subprocess


SERVICE_PROVIDER_PATH = os.path.abspath(os.path.join('./scripts/'))


# deploy into kubernetes cluster
def run_bash_script():
    """Runs a simple script using subprocess"""

    status_subprocess = subprocess.run("./hello_world.sh",
                                       shell=True,
                                       executable="/bin/bash",
                                       cwd=SERVICE_PROVIDER_PATH,
                                       check=True)
    return str(status_subprocess.returncode)
