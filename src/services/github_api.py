import requests
import json
from urllib.parse import urljoin
from datetime import date

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
        today = date.today().strftime('%Y-%m-%d')

        for issue in self.issues:
            created_at = issue["created_at"].split('T')[0]
            updated_at = issue["updated_at"].split('T')[0]
            
            if (created_at == today or updated_at == today):
                urls.append(issue['html_url'])

        return urls

