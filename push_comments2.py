import requests
from github import Github

access_token_git = "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"

g = Github(access_token_git)
repo = g.get_repo("Spiderinattack/Devops-AWS-Jenkins")
pulls = repo.get_pulls(state='open')

for pr in pulls:
    pr_title = pr.title
    pr_number = pr.number
    print(pr_title)
    print(pr_number)
