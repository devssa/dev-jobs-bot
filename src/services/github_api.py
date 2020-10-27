import requests
import json
from urllib.parse import urljoin


class GitHubApi:
    def __init__(self):
        self.base_url = 'https://api.github.com/repos/devssa/onde-codar-em-salvador/'
        self.issues = []

        self.api_issues()

    def api_issues(self):
        url = urljoin(self.base_url, 'issues')
        response = requests.get(url)
        data = json.loads(response.content)
        self.issues = data

    def get_jobs(self):
        urls = []
        for issue in self.issues:
            urls.append(issue["url"])

        print(urls)


GitHubApi().get_jobs()

