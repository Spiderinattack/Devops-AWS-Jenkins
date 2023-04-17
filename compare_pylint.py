import os

os.system('pwd')
# os.system("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' results/pylint_result.txt")
score = int(os.popen("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' results/pylint_result.txt").read())
print("score is: ", score)
print("Type of score is: ", type(score))

if score > 7:
  print("score > than 7")
else:
  print("score < than 7")
