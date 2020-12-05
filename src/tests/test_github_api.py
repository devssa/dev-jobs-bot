import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

import unittest

from services.github_api import GitHubApi


class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.api = GitHubApi()
    
    def test_API_status_not_ok(self):
        self.assertEqual(self.api.status, 200, 'The status_code doesn\'t ok.')

    def test_case_client_side_error(self):
        self.assertFalse(self.api.status > 300 and self.api.status < 500, 'Client-side error.')

    def test_case_server_side_error(self):
        self.assertFalse(self.api.status >= 500, 'Server-side error.')


if __name__ == '__main__':
    unittest.main()

    
