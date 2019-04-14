import subprocess, sys, shutil
import gmod_cli.gmod_cli as gmod_cli

def main(argv):
    """Setup the necessary dependencies"""
    print("===Starting setup procedure===", end='\n\n', flush=True)
    print("Installing pip dependencies ... ", flush=True)
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], stdout=sys.stdout, check=True)
    except subprocess.CalledProcessError as err:
        print(err, flush=True)
        print("Error while attempting to install pip dependencies. Aborting", flush=True)
        sys.exit(1)
    print("Installing pip dependencies ... [DONE]", end='\n\n', flush=True)

    print("Localizing SteamCMD ... ", end="", flush=True)
    if gmod_cli.test_steamcmd():
        print("[Found]", end="\n\n", flush=True)
    else:
        print("[Not found]", flush=True)
        print("Could not find SteamCMD. Please install it by following the instructions on https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD", end="\n\n", flush=True)

    print("Localizing apt-get ... ", end="", flush=True)
    if check_apt_get():
        print("[Found]", end="\n\n", flush=True)
    else:
        print("[Not Found]", end="\n\n", flush=True)

    sys.exit(0)

def check_apt_get():
	return shutil.which("apt-get") != None

if __name__ == "__main__":
	main(sys.argv[1:])
