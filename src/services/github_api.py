import sys
sys.path.append("..")

import requests
import json
from datetime import date

import env
from msgs import msg_generator

class GitHubApi:
    def __init__(self):
        self.url = env.COMMUNITY_GH_API_ISSUES
        self.issues = []
        self.api_issues()

    def api_issues(self):
        response = requests.get(self.url)
        data = json.loads(response.content)
        self.issues = data

    def get_jobs(self):
        urls = []
        today = date.today().strftime('%Y-%m-%d')

        for issue in self.issues:
            created_at = issue['created_at'].split('T')[0]
            updated_at = issue['updated_at'].split('T')[0]
            
            if (created_at == today or updated_at == today):
                urls.append(issue['html_url'])

        return urls

    def last_jobs(self, num=10):
        msg = ''
        if num == 1:
            msg = f'🗒️Essa foi a última vagas lançada 🗒️\n\n'
        else:
            msg = f'🗒️ Essas foram as {num} últimas vagas lançadas 🗒️\n\n'

        for issue in self.issues[:num]:
            msg += msg_generator.parse_jobs(issue)

        return msg
