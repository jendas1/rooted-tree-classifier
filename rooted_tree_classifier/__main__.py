import sys

from .log_decider import is_log_solvable
from .log_star_decider import is_log_star_solvable

if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    if is_log_solvable(constraints):  # is not empty
        if is_log_star_solvable(constraints):
            print("O(log*n)")
        else:
            print("Θ(log n)")
    else:
        print("Ω(n)")
