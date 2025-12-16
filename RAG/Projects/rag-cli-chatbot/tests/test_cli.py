import subprocess
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from src.cli import main

class TestCLI(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['What is the text all about?', 'exit'])
    def test_chatbot_response(self, mock_input, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Question:", output)
        self.assertIn("Answer:", output)

if __name__ == '__main__':
    unittest.main()