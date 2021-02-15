import sys

if __name__ == "__main__":
    from common import powerset
    from log_star_decider import _is_log_star_solvable
else:
    from .common import powerset
    from .log_star_decider import _is_log_star_solvable
    from .constant_synthesizer import find_algorithm

VERBOSE = False


def is_constant_solvable(constraints):
    labels = set("".join(constraints))

    for reduced_labels in powerset(labels):
        reduced_constraints = [constraint for constraint in constraints if
                               (constraint[0] in reduced_labels and constraint[1] in reduced_labels and constraint[
                                   2] in reduced_labels)]
        for label in reduced_labels:
            for constraint in reduced_constraints:
                if constraint.startswith(label + label) or constraint.endswith(label + label):
                    if _is_log_star_solvable(reduced_constraints, list(reduced_labels), label):
                        if VERBOSE:
                            find_algorithm(reduced_constraints)
                        return True

    return False


if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    if is_constant_solvable(constraints):
        print("O(1)")
    else:
        print("ω(1)")
