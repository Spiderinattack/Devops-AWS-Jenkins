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
