""" README
A CLI for managing a gmod server instance
Author: Kai Frankenhaueser
E-Mail: kailijan@flauschig.net
"""

import sys, getopt, os, shutil

verbose = False
steamcmd = ""

def main(argv):
	global verbose, steamcmd
	action = ""
	try:
		opts, args = getopt.getopt(argv, "hva:", ["verbose", "help", "action=", "steamcmd="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-v", "--verbose"):
			verbose = True
		elif opt in ("-h", "--help"):
			usage()
			sys.exit(0)
		elif opt in ("-a", "--action"):
			action = arg
		elif opt == "--steamcmd":
			steamcmd = arg
	if action == "":
		debug("No action provided, receiving input")
		list_actions()
		action = input("Please choose an action by name or number: ")
		action = validate_input(*action, ["1", "install"])
	debug("Action is: " + str(action))
	call_routine(action)

def call_routine(action):
	"""Call the function linked to the given action"""
	if action == "install" or action == "1":
		install()
	else:
		print("Error: Unrecognized action!")
		usage()
		sys.exit(2)

def install():
	"""Install gmod via steamcmd to given directory"""
	debug("Starting install routine.")
	debug("Checking if steamCMD is installed...")
	if not test_steamcmd():
		print("Could not find SteamCMD. Please install it by following the instructions on https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD")
		print("Should this error persist after installing SteamCMD, please provide the destination of the executable by appending --steamcmd <path>")
		sys.exit(1)
	dest = input("Install directory (" + os.getcwd() + "): ")
	if dest == "":
		dest = os.getcwd()
	dest = os.path.expanduser(dest)
	if not os.path.isdir(dest):
		create = input("Directory does not exist. Create it? (yes/no): ")
		create = validate_input(create, ["y", "n", "yes", "no"])
		if create == "y" or create == "yes":
			try:
				os.makedirs(dest)
			except OSError as err:
				print(err)
				print("Could not create directory " + dest)
				return install()
		else:
			return install()

def validate_input(inpt, options):
	"""Return an elemnent of options, selected by input"""
	while not inpt in options:
		inpt = input("Please enter a valid input: ")
	return inpt

def test_prerequisites():
	return test_steamcmd()

def test_steamcmd():
	"""Return True when SteamCMD is installed, otherwise return False"""
	global steamcmd
	if steamcmd != "" and os.path.isfile(steamcmd):
		return True
	else:
		path = shutil.which("steamcmd")
		return path != None

def write_install_update_script(dest, rel_path="scripts/install_update_gmod.txt"):
	"""Write installation procedure to script at '<current work directory>/scripts/<script name>.txt'"""
	rel_path = os.path.normpath(rel_path)
	content =	("// install_gmod.txt\n"
			"//\n"
			"@ShutdownOnFailedCommand 1\n"
			"@NoPromptForPassword 1\n"
			"login anonymous\n"
			"force_install_dir \"" + str(dest) + "\"\n"
			"app_update 4020 validate\n"
			"quit\n")
	f = open(os.path.join(os.getcwd(), rel_path), "w")
	f.write(content)
	f.close()

def check():
	status = 'SUCCESS'
	print("Testing SteamCMD...")
	if test_steamcmd():
		print("OK")
	else:
		status = 'FAILURE'
		print("FAIL")
	print("Check finished: " + status)


def debug(msg):
	"""Print msg when in verbose mode"""
	if verbose == True:
		print(msg)

def usage():
	"""Print usage info"""
	print("Usage: setup.py [-a <action>] [-v]")
	list_actions()

def list_actions():
	"""Print list of possible actions"""
	print("Possible actions:")
	print("(1) install	- Installs gmod to the given directory")
#	print("(2) update	- Updates gmod")
#	print("(3) start	- Starts the server")
#	print("(4) stop	- Stops the server")
#	print("(5) remove	- Removes gmod")
	print("(6) check	- Check all the dependencies")

if __name__ == "__main__":
	main(sys.argv[1:])
