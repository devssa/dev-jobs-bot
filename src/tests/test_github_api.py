import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from services.github_api import GitHubApi

import unittest

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.api = GitHubApi()
    
    def test_API_status_not_ok(self):
        status_code = self.api.status_code
        self.assertEqual(status_code, 200, "The status_code doesn't ok")


if __name__ == '__main__':
    unittest.main()

    
