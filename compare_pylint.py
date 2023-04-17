import os

os.system('pwd')
os.system("sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' results/pylint_result.txt")
