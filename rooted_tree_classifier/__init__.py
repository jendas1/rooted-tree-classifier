from .constant_decider import is_constant_solvable
from .log_decider import is_log_solvable
from .log_star_decider import is_log_star_solvable


# Package version
__version__ = '0.1.9'

def decide_complexity(constraints):
    if is_log_solvable(constraints):  # is not empty
        if is_log_star_solvable(constraints):
            if is_constant_solvable(constraints):
                print("O(1)")
            else:
                print("Θ(log*n)")
        else:
            print("Θ(log n)")
    else:
        print("Ω(n)")
