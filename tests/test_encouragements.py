import unittest
import io
import sys
from aide_tutorial.encouragements import ethan92429, skyler1253,matanp,avtrigg, prevosis


class TestEncouragements(unittest.TestCase):
    """
    Test aide_tutorial's encouragements.
    """
    def test_ethan92429(self):
        """
        Test ethan92429's words of encouragement.
        """
        captured_output = io.StringIO()         # Create StringIO object
        sys.stdout = captured_output            # and redirect stdout.
        ethan92429()                            # Call unchanged function.
        sys.stdout = sys.__stdout__             # Reset redirect.
        self.assertEqual(captured_output.getvalue(), "This too shall pass.\n")

    def test_skyler1253(self):
        """
        TODO: Change this function to add your own encouragements.
        """
        captured_output = io.StringIO()         # Create StringIO object
        sys.stdout = captured_output            # and redirect stdout.
        skyler1253()                            # Call unchanged function.
        sys.stdout = sys.__stdout__             # Reset redirect.
        self.assertEqual(captured_output.getvalue(), "siempre hay un pelo en la sopa.\n")

    def test_matanp(self):
        """
        matanp test first contribution tutorial function
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        matanp()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(),
".__           .__  .__                               .__       .___\n|  |__   ____ |  | |  |   ____   __  _  _____________|  |    __| _/\n|  |  \_/ __ \|  | |  |  /  _ \  \ \/ \/ /  _ \_  __ \  |   / __ |\n|   Y  \  ___/|  |_|  |_(  <_> )  \     (  <_> )  | \/  |__/ /_/ |\n|___|  /\___  >____/____/\____/    \/\_/ \____/|__|  |____/\____ |\n     \/     \/                                                  \/ \n")


    def test_avtrigg(self):
        """
        Test avtrigg's words of encouragement.
        """
        captured_output = io.StringIO()         # Create StringIO object
        sys.stdout = captured_output            # and redirect stdout.
        avtrigg()                                 # Call unchanged function.
        sys.stdout = sys.__stdout__             # Reset redirect.
        self.assertEqual(captured_output.getvalue(), "Be kind, for everyone you know is fighting a hard battle.\n")

    def test_prevosis(self):
        """
        Test prevosis's words of encouragement.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        prevosis()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "valar morghulis\n")

    def test_TODO(self):
        """
        TODO: Change this function to add your own encouragements.
        """
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
