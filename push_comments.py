import requests
import json
import subprocess

owner = 'Spiderinattack'
repo = 'Devops-AWS-Jenkins'
git_username = "Spiderinattack"
git_api_token = "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"

git_api_endpoint = f'https://api.github.com/repos/{owner}/{repo}/pulls'
git_auth = (git_username, git_api_token)
git_headers = {
    "Accept": "application/vnd.github.v3+json"
}
git_response = requests.get(git_api_endpoint, auth=git_auth, headers=git_headers)
print(git_response)
if git_response.status_code == 200:
    pulls = json.loads(git_response.text)
    if pulls and len(pulls) > 0:
        for pr in pulls:
            pr_number = pr['number']
            pr_title = pr['title']
            print(pr_number)
            print(pr_title)
    else:
        print("There are no open PRs")
    
    comments_api_endpoint = f'https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments'
    sed_command_pylint = "sed -n 's/.*Your code has been rated at \\([0-9]*\\.[0-9][0-9]\\).*/\\1/p' results/pylint_result.txt"
    score = subprocess.check_output(sed_command_pylint, shell=True, text=True, encoding='utf-8')
    print("Pylint score is", score)
    comment_body = 'Pylint score is ' + score
    response = requests.post(comments_api_endpoint, auth=git_auth, json={'body': comment_body})
    print(response)
    
    if response.status_code == 201:
        print('Comment added successfully.')
    else:
        print('Failed to add comment.')
else:
    print(f"Failed to retrieve pull requests: {git_response.text}")
