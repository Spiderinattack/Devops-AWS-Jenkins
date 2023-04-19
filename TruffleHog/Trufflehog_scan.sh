#to install trfflehog if not
#pip3 install truffleHog

#to check trufflehog entropy
#trufflehog https://github.com/Spiderinattack/Devops-AWS-Jenkins.git
  
#to check trufflehog regex
#trufflehog --regex --entropy False https://github.com/Spiderinattack/Devops-AWS-Jenkins.git
  
#rm -f trufflehog_result.json || true
#pip3 install truffleHog
#sudo chmod 777 /home/ec2-user/Jenkins/Dev/Jenkins/workspace/Python_Job/TruffleHog/Trufflehog_scan.py

import trufflehog
trufflehog --json https://github.com/Spiderinattack/Devops-AWS-Jenkins.git >> trufflehog_result.json
trufflehog --json --regex --entropy False https://github.com/Spiderinattack/Devops-AWS-Jenkins.git >> trufflehog_result.json
#sudo chmod 777  /home/ec2-user/Jenkins/Dev/Jenkins/workspace/Python_Job/results/trufflehog_result.txt
