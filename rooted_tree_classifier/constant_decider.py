import sys

if __name__ == "__main__":
    from common import powerset
    from log_star_decider import _is_log_star_solvable
else:
    from .common import powerset
    from .log_star_decider import _is_log_star_solvable


def is_constant_solvable(constraints):
    labels = set("".join(constraints))
    constant_solvable = False

    for reduced_labels in powerset(labels):
        reduced_constraints = [constraint for constraint in constraints if
                               (constraint[0] in reduced_labels and constraint[1] in reduced_labels and constraint[
                                   2] in reduced_labels)]
        has_aab = False
        for label in reduced_labels:
            for constraint in constraints:
                if constraint.startswith(label + label) or constraint.endswith(label + label):
                    has_aab = True

        if has_aab and _is_log_star_solvable(reduced_constraints, list(reduced_labels)):
            constant_solvable = True
            break
    return constant_solvable


if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    if is_constant_solvable(constraints):
        print("O(1)")
    else:
        print("ω(1)")
