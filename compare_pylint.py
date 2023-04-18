import os
import subprocess
import re

os.system('pwd')
# os.system("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' results/pylint_result.txt")
os.chdir('results')
print('Current Working Directory is: ', os.getcwd())
# os.system('cd results')
# score = os.popen("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint_result.txt").read()
os.chdir('/home/ec2-user/Jenkins/Dev/Jenkins/workspace/new_Job/results/')
print('Current new Working Directory is: ', os.getcwd())
# score = subprocess.call(["sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint_result.txt"], shell=True)


regex = re.compile('s/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p')
with open("pylint_result.txt") as f:
    for line in f:
        score = regex.search(line)
print("score is: ", score)
print("Type of score is: ", type(score))

if score > 7:
  print("score > than 7")
else:
  print("score < than 7")
