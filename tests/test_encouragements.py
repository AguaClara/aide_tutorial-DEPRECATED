import unittest
import io
import sys
from aide_tutorial.encouragements import ethan92429


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


    def test_TODO(self):
        """
        TODO: Change this function to add your own encouragements.
        """
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
