#!/usr/bin/env python3

# sketch for an exponential algorithm determining whether problem is log* solvable or not
# missing to formally prove
# - iteratively building the set of equivalent labels by merging two sets is sound
# todo
#
# done
# - bugfix - removed separation of strongly connected components, fallback to try all subsets of labels
#   - assumption that log*n solvability of subset of labels implies log*n solvability for the whole strongly connected component is false (212 122 111 - by Aleksandr Tereshchenko)
# - print certificate for log*n solvability
# - alleviate assumption for reaching every other label
#   - by constructing a graph (hypergraph or normal with collapsed edges) and separate each strongly connected component
#       - "fine" as removal of a rule bridging s.c.c. cannot create problems because:
#           - either the "pointed" s.c.c. is log*n solvable, then such rule is useless.
#           - Otherwise, using a rule would force subtree to be ω(log n) solvable, so again useless.
import sys

VERBOSE = False

if __name__ == "__main__":
    from common import get_constraints_for_labels, powerset
else:
    from .common import get_constraints_for_labels, powerset



def is_log_star_solvable(constraints):
    labels = set("".join(constraints))
    log_star_solvable = False

    for reduced_labels in powerset(labels):
        reduced_constraints = [constraint for constraint in constraints if
                               (constraint[0] in reduced_labels and constraint[1] in reduced_labels and constraint[2] in reduced_labels)]
        if _is_log_star_solvable(reduced_constraints, list(reduced_labels)):
            log_star_solvable = True
            break
    return log_star_solvable



def _is_log_star_solvable(constraints, labels, a = "ε"):
    root_labels = [(set(label), label == a) for label in labels]

    if VERBOSE:
        certificate = dict()

    constrains_for_labels = get_constraints_for_labels(constraints, labels)

    while True:
        root_labels_enlarged = False
        for e1, a1 in root_labels:
            for e2, a2 in root_labels:
                new_root_labels = []
                for label in labels:
                    for constraint in constrains_for_labels[label]:
                        if (constraint[0] in e1 and constraint[1] in e2) or \
                                (constraint[1] in e1 and constraint[0] in e2):
                            new_root_labels.append(label)
                            break
                root_pair = (new_root_labels, a1 or a2)
                if root_pair not in root_labels:
                    root_labels.append(root_pair)
                    if VERBOSE:
                        certificate[tuple(root_pair)] = ((tuple(e1), a1), (tuple(e2), a2))
                    root_labels_enlarged = True
                    break
            if root_labels_enlarged:
                break
        if not root_labels_enlarged:
            break

    if (labels, a != "ε") not in root_labels or not constraints:  # not constraints here for the edge-case of a single label
        return False
    else:
        if VERBOSE:
            print("Certificate:", certificate)
            print("digraph certificate {")
            for node, children in certificate.items():
                print(f'"{node}" -> "{children[0]}";')
                print(f'"{node}" -> "{children[1]}";')
            print("}")
        return True

if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    if is_log_star_solvable(constraints):
        print("O(log*n)")
    else:
        print("ω(log*n)")
