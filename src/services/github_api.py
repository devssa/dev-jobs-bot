import sys

from requests import api
from requests import status_codes
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
        self.status = self.api_issues()

    def api_issues(self):
        response = requests.get(self.url)
        if (response.status_code <= 300):
            data = json.loads(response.content)
            self.issues = data

        elif (response.status_code > 300 and response.status_code < 500):
            self.issues.append('Client-Side Error')
            return 200

        elif (response.status_code >= 500):
            self.issues.append('Server-side error')
            return 200

        return response.status_code

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
