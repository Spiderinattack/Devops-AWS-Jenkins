import os
import subprocess

os.system('pwd')
# os.system("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' results/pylint_result.txt")
os.chdir('results')
print('Current Working Directory is: ', os.getcwd())
# os.system('cd results')
# score = os.popen("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint_result.txt").read()
score = subprocess.call(["sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint_result.txt"], shell=True)
print("score is: ", score)
print("Type of score is: ", type(score))

if score > 7:
  print("score > than 7")
else:
  print("score < than 7")
