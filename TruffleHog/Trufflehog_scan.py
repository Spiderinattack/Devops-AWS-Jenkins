#to install trfflehog if not
pip3 install truffleHog

#to check trufflehog entropy
trufflehog https://github.com/Spiderinattack/Devops-AWS-Jenkins.git
  
#to check trufflehog regex
trufflehog --regex --entropy False https://github.com/Spiderinattack/Devops-AWS-Jenkins.git
