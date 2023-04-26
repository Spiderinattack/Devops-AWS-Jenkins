import subprocess
import os

os.environ['PATH'] +=  ':/home/ec2-user/.local/bin/'
print(os.environ['PATH'])

install_trufflehog = subprocess.Popen(["pip install trufflehog"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(install_trufflehog.stdout.read())
trufflehog_dir=os.getcwd()
print(trufflehog_dir)

root_login = subprocess.Popen(["which trufflehog"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(root_login.stdout.read())
print(root_login.stderr.read())

output_txt = subprocess.Popen(["trufflehog https://github.com/Spiderinattack/Devops-AWS-Jenkins.git"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(output_txt.stdout.read())
print(output_txt.stderr.read())
print("done")

#with open('output.txt' , 'w') as outfile:
#    output_txt = subprocess.Popen(["sudo -n trufflehog https://github.com/Spiderinattack/Devops-AWS-Jenkins.git"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#    for line in output_txt.stdout:
#        outfile.write(line)
#        print(line, end='')
#    for line in output_txt.stderr:
#        outfile.write(line)
#        print(line, end='')
        
#with open('output.txt','r') as infile:
#    output = infile.read()
#print(output)

#os.chdir('/var/lib/jenkins/workspace/TruffleHog_Job')
print(os.getcwd())
#output_txt1 = subprocess.Popen(["ls -l /var/lib/jenkins/workspace/TruffleHog_Job/TruffleHog/Trufflehog_python_script.py"], shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#output_stream=output_txt1.stdout
#output_string=output_stream.read()
#print (output_string)

# Specify the repository URL and directory to clone it to
repo_url = 'https://github.com/Spiderinattack/Devops-AWS-Jenkins.git'
repo_dir = '/var/lib/jenkins/workspace/Trufflehog_Job'
print(repo_dir)

#trufflehog1 = subprocess.run('/home/ec2-user/.local/bin/trufflehog  https://github.com/Spiderinattack/Devops-AWS-Jenkins.git', shell=True, capture_output=True, text=True)
#print(trufflehog1.stdout)
#print("Hello")

#find1 = subprocess.run('find /var/lib/jenkins/workspace/TruffleHog_Job/ -name "Trufflehog_python_script.py"', shell=True, capture_output=True, text=True)
#print(find1.stdout)
#print("Hello")

#permission_check = subprocess.run('ls -l /var/lib/jenkins/workspace/TruffleHog_Job/TruffleHog/Trufflehog_python_script.py', shell=True, capture_output=True, text=True)
#print(permission_check.stdout)
#print("Hello")

#output = subprocess.Popen(['trufflehog /var/lib/jenkins/workspace/Trufflehog_Job', '/var/lib/jenkins/workspace/Trufflehog_Job'], shell=True, stdout=subprocess.PIPE).communicate()[0]

# Print the output
#print(output.decode())

#result1 = subprocess.run(['ls -l $(which trufflehog3)', '/var/lib/jenkins/workspace/Trufflehog_Job'], capture_output=True, text=True)
#print(result1.stdout)

#result2 = subprocess.run(['chmod +x $(which trufflehog3)', '/var/lib/jenkins/workspace/Trufflehog_Job'], capture_output=True, text=True)
#print(result2.stdout)

#result = subprocess.run(['trufflehog3', '/var/lib/jenkins/workspace/Trufflehog_Job'], capture_output=True, text=True)
#print(result.stdout)

#output = subprocess.check_output('trufflehog3 https://github.com/Spiderinattack/Devops-AWS-Jenkins.git', shell=True, text=True, encoding='utf-8')
#print("Output :", output)

# subprocess.Popen() method is used to run the trufflehog3 command with the directory
# shell=True argument indicates that the command should be executed using a shell
# stdout=subprocess.PIPE argument redirects the output of the command to a pipe
# stderr=subprocess.PIPE argument redirects the error of the command to a pipe
# communicate() method waits for the command to complete and returns a tuple of (stdout, stderr) 
#output = subprocess.Popen(['trufflehog3 /var/lib/jenkins/workspace/Trufflehog_Job', '/var/lib/jenkins/workspace/Trufflehog_Job'], shell=True, stdout=subprocess.PIPE).communicate()[0]

# Print the output
#print(output.decode())

# Open the output file in write mode
#with open('TruffleHog/results.txt', 'w') as f:
    # Write the contents of the output variable to the file
    #f.write(output.decode())
