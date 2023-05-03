import os
import subprocess


SERVICE_PROVIDER_PATH = os.path.abspath(os.path.join('./scripts/'))


# deploy into kubernetes cluster
def run_bash_script():
    status_subprocess = subprocess.run("./hello_world.sh", shell=True, executable="/bin/bash", cwd=SERVICE_PROVIDER_PATH)
    return str(status_subprocess.returncode)
