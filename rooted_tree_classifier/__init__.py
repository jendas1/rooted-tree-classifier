from .constant_decider import is_constant_solvable
from .log_decider import is_log_solvable
from .log_star_decider import is_log_star_solvable


# Package version
__version__ = '0.2.1'

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
        k = polynomial_complexity(constraints)
        if k == 0:
            print("unsolvable")
        elif k == 1:
            print("Θ(n)")
        else:
            print(f"Θ(n^(1/{k}))")
