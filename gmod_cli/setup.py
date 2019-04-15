import subprocess, sys, shutil
import gmod_cli

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
        inst = input("Attempt to install SteamCMD? (yes/no) ")
        inst = gmod_cli.validate_input(inst, ["y", "n", "yes", "no"])
        if inst == "y" or inst == "yes":
            install_steamcmd()
        else:
            print("", flush=True)

    print("Validating installation ... ", end="", flush=True)
    if gmod_cli.test_prerequisites():
        print("[Installation sucessful]", end="\n\n", flush=True)
        print("Congratulations, you can now start using GMod-CLI.", flush=True)
        sys.exit(0)
    else:
        print("[Installation failed]", end="\n\n", flush=True)
        print("Warning, something went wrong. Please read the docs at https://kailijan.github.io/GMod-CLI/#installation.", flush=True)
        sys.exit(1)

def install_steamcmd():
    """Attempt to install SteamCMD"""
    print("Localizing apt-get ... ", end="", flush=True)
    if check_apt_get():
        print("[Found]", end="\n\n", flush=True)
        # Attempt to use apt-get
        try:
            print("Installing SteamCMD via apt-get ... ", flush=True)
            subprocess.run(["apt-get", "install", "steamcmd"], stdout=sys.stdout, check=True)
            print("Installing SteamCMD via apt-get ... [DONE]", flush=True)
            return
        except subprocess.CalledProcessError as err:
            print(err, flush=True)
            print("Please make sure your user is allowed to execute apt-get, or run setup.py using sudo.", flush=True)
    else:
        print("[Not Found]", flush=True)
        print("Could not install SteamCMD. Please install it by following the instructions on https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD", flush=True)

def check_apt_get():
    """Check presence of apt-get"""
    return shutil.which("apt-get") != None

if __name__ == "__main__":
	main(sys.argv[1:])
