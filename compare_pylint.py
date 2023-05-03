import os
import subprocess
import re

os.system('pwd')
os.system('pwd')
print('Current new Working Directory is: ', os.getcwd())

sed_command_pylint = "sed -n 's/.*Your code has been rated at \\([0-9]*\\.[0-9][0-9]\\).*/\\1/p' results/pylint_result.txt"
score = subprocess.check_output(sed_command_pylint, shell=True, text=True, encoding='utf-8')

grep_command_factload = "grep -o -i 'def test_case' PyUnit/PyUnit_fact_load.py | wc -l"
testcase_count = subprocess.check_output(grep_command_factload, shell=True, text=True, encoding='utf-8')
print("Test case count", testcase_count)

grep_command_pyunit = "grep -o -i 'ran successfully' results/pyunit_result.txt | wc -l"
successful_count = subprocess.check_output(grep_command_pyunit, shell=True, text=True, encoding='utf-8')
print("Successful count", successful_count)
print(score)

print("score is: ", score)
print("Type of score is: ", type(score))

if score > '7' and (testcase_count==successful_count):
  print("score > than 7 and all pyunit test cases ran successfully")
else:
  print("score < than 7 or all pyunit test cases didn't run successfully, hence failing")
  exit(1)
