import subprocess, sys

try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], stdout=sys.stdout, check=True)
except CalledProcessError as err:
    print(err)
    sys.exit(1)

sys.exit(0)
