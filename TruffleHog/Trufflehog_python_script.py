import subprocess
import os

#install_trufflehog=subprocess.call("pip install trufflehog3",shell=true)
install_trufflehog = subprocess.run('pip install trufflehog3', shell=True, capture_output=True, text=True)
print(install_trufflehog)
      
# Specify the repository URL and directory to clone it to
repo_url = 'https://github.com/Spiderinattack/Devops-AWS-Jenkins.git'
repo_dir = '/var/lib/jenkins/workspace/Trufflehog_Job'

#install_trufflehog1 = subprocess.run('trufflehog3 -h', shell=True, capture_output=True, text=True)
#print(install_trufflehog1)

result = subprocess.run(['trufflehog3', '/var/lib/jenkins/workspace/Trufflehog_Job'], capture_output=True, text=True)
print(result.stdout)

#output = subprocess.check_output('trufflehog3 https://github.com/Spiderinattack/Devops-AWS-Jenkins.git', shell=True, text=True, encoding='utf-8')
#print("Output :", output)

# subprocess.Popen() method is used to run the trufflehog3 command with the directory
# shell=True argument indicates that the command should be executed using a shell
# stdout=subprocess.PIPE argument redirects the output of the command to a pipe
# stderr=subprocess.PIPE argument redirects the error of the command to a pipe
# communicate() method waits for the command to complete and returns a tuple of (stdout, stderr) 
#output = subprocess.Popen(['trufflehog3 /var/lib/jenkins/workspace/Trufflehog_Job', '/var/lib/jenkins/workspace/Trufflehog_Job'], shell=True, stdout=subprocess.PIPE).communicate()[0]

# Print the output
#print(output.decode('utf-8'))

# Open the output file in write mode
#with open('TruffleHog/results.txt', 'w') as f:
    # Write the contents of the output variable to the file
    #f.write(output.decode())
