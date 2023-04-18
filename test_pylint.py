import argparse
import logging
from pylint.lint import Run
results = Run(['Programs/code1.py'], do_exit=False)
final_score = results.linter.stats.global_note
final_score
print("Type of score: ", type(final_score))
str_final_score = str(final_score)
print("Final score is",str_final_score)

# results = Run(['Programs/code1new.py'], do_exit=False)
# final_score = results.linter.stats.global_note
# final_score
