import subprocess
import os
import trufflehog3

# Specify the repository URL and directory to clone it to
repo_url = 'https://github.com/Spiderinattack/Devops-AWS-Jenkins.git'
repo_dir = '/var/lib/jenkins/workspace/Trufflehog_Job'
   
# subprocess.Popen() method is used to run the trufflehog3 command with the directory
# shell=True argument indicates that the command should be executed using a shell
# stdout=subprocess.PIPE argument redirects the output of the command to a pipe
# stderr=subprocess.PIPE argument redirects the error of the command to a pipe
# communicate() method waits for the command to complete and returns a tuple of (stdout, stderr) 
output = subprocess.Popen(['trufflehog /var/lib/jenkins/workspace/Trufflehog_Job', '/var/lib/jenkins/workspace/Trufflehog_Job'], shell=True, stdout=subprocess.PIPE).communicate()[0]

# Print the output
print(output.decode('utf-8'))

# Open the output file in write mode
#with open('TruffleHog/results.txt', 'w') as f:
    # Write the contents of the output variable to the file
    #f.write(output.decode())
