from z3 import *
import numpy as np


def constraints_to_internal(constraints):
    labels = "".join(set("".join(constraints)))
    numbered_constraints = []
    for constraint in constraints:
        c = ""
        for i in range(len(constraint)):
            c += str(labels.find(constraint[i]))
        numbered_constraints.append(c)
    constraints = numbered_constraints
    configurations = {label: [] for label in range(len(labels))}
    for c in constraints:
        configurations[int(c[1])].append((int(c[0]), int(c[2])))
    return configurations, len(labels)


def find_algorithm(constraints, max_rounds=12):
    configurations, labels = constraints_to_internal(constraints)
    for rounds in range(max_rounds):
        nodes = 2 ** (rounds)
        xs = np.array([[Bool(f'x_{i}_{j}') for j in range(labels)] for i in range(nodes)])
        and_rules = []
        # every node can have only one color
        for node_id in range(nodes):
            or_rules = []
            for i in range(labels):
                other_labels = []
                for j in range(labels):
                    if i == j:
                        other_labels.append(xs[node_id, j])
                    else:
                        other_labels.append(Not(xs[node_id, j]))
                or_rules.append(And(other_labels))
            and_rules.append(Or(or_rules))

        # constraints have to be satisfied
        for label in range(labels):
            for node_id in range(nodes):
                or_rules = []
                for confg in configurations[label]:
                    left_child = (node_id * 2 + 1) % nodes
                    right_child = (node_id * 2) % nodes
                    or_rules.append(And(xs[left_child, confg[0]], xs[right_child, confg[1]]))
                    or_rules.append(And(xs[left_child, confg[1]], xs[right_child, confg[0]]))
                and_rules.append(Implies(xs[node_id, label], Or(or_rules)))

        s = Solver()
        s.add(And(and_rules))

        if s.check() == z3.sat:
            model = s.model()

            algo = []
            for node_id in range(nodes):
                for label in range(labels):
                    if model[xs[node_id, label]]:
                        algo.append(label + 1)
            print("rounds:", rounds)
            print("algorithm:", "".join(map(str, algo)))
            break
    else:
        print(f"complexity is more than {max_rounds} rounds.")


def check(algo, constraints):
    constraints = constraints.split(" ")
    n = len(algo)
    for i in range(len(algo)):
        lc = (i * 2) % n
        rc = (i * 2 + 1) % n
        if not algo[lc] + algo[i] + algo[rc] in constraints and not algo[rc] + algo[i] + algo[lc] in constraints:
            return False
    return True
