import requests
from github import Github
import subprocess

access_token_git = "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"

g = Github(access_token_git)
repo = g.get_repo("Spiderinattack/Devops-AWS-Jenkins")
pulls = repo.get_pulls(state='open')

for pr in pulls:
    pr_title = pr.title
    pr_number = pr.number
    print(pr_title)
    print(pr_number)

username = 'Spiderinattack'
auth = (username, access_token_git)
git_headers = {
    "Accept": "application/vnd.github.v3+json"
}

owner = 'Spiderinattack'
repo = 'Devops-AWS-Jenkins'
comments_api_endpoint = f'https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments'

sed_command_pylint = "sed -n 's/.*Your code has been rated at \\([0-9]*\\.[0-9][0-9]\\).*/\\1/p' results/pylint_result.txt"
score = subprocess.check_output(sed_command_pylint, shell=True, text=True, encoding='utf-8')
print("Pylint score is", score)
comment_body = 'Pylint score is ' + score

response = requests.post(comments_api_endpoint, auth=auth, json={'body': comment_body})
print(response)

if response.status_code == 201:
    print('Comment added successfully.')
else:
    print('Failed to add comment.')
