import os, unittest, filecmp
import gmod_cli.gmod_cli as gmod_cli

class TestScriptCreation(unittest.TestCase):
    def setUp(self):
        self.install_script_src = os.path.normpath("gmod_cli/tests/src/install_gmod.txt")
        self.install_script_tmp = os.path.normpath("gmod_cli/tests/tmp/install_gmod.txt")
        gmod_cli.write_install_update_script(".", rel_path="gmod_cli/tests/tmp/install_gmod.txt")

    def tearDown(self):
        os.remove(os.path.join(os.getcwd(), self.install_script_tmp))

    def test_install_script(self):
        """Test whether install script for SteamCMD can be created sucessfully"""
        self.assertTrue(filecmp.cmp(os.path.join(os.getcwd(), self.install_script_src), os.path.join(os.getcwd(), self.install_script_tmp)))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
