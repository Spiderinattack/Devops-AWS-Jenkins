import argparse
import logging
from pylint.lint import Run
results = Run(['Programs/code1.py'], do_exit=False)
final_score = results.linter.stats.global_note
final_score

results = Run(['Programs/code1new.py'], do_exit=False)
final_score = results.linter.stats.global_note
final_score

# adding dummy line
