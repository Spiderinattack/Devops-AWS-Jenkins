import requests
import json

for i in range(4)
    print(i)
git_api_endpoint = "https://api.github.com/repos/Spiderinattack/Devops-AWS-Jenkins/pulls"
git_username = "Spiderinattack"
git_api_token = "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"
git_auth = (git_username, git_api_token)
git_headers = {
    "Accept": "application/vnd.github.v3+json"
}
git_response = requests.get(git_api_endpoint, auth=git_auth, headers=git_headers)
if git_response.status_code == 200:
    pulls = json.loads(git_response.text)
    if pulls and len(pulls) > 0:
        eligible_pulls = [p for p in pulls if p["state"] == "open"]
        if eligible_pulls:
            jenkins_url = "http://10.239.214.17:8080"
            jenkins_job_name = "new_job"
            jenkins_username = "Test-automation"
            jenkins_api_token = "118e182ced38aa12bf1af180bff2f6deec"
            jenkins_api_url = f"{jenkins_url}/job/{jenkins_job_name}/build"
            jenkins_auth = (jenkins_username, jenkins_api_token)
            jenkins_headers = {
                "Content-Type": "application/json"
            }
            jenkins_response = requests.post(jenkins_api_url, auth=jenkins_auth, headers=jenkins_headers)
            if jenkins_response.status_code == 201:
                print("Jenkins pipeline has been triggered successfully.")
            else:
                print(f"Failed to trigger Jenkins pipeline: {jenkins_response.text}")
        else:
            print("No eligible pull requests found.")
    else:
        print("No open pull requests found.")
else:
    print(f"Failed to retrieve pull requests: {git_response.text}")
