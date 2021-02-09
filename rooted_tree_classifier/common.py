from itertools import chain, combinations

def get_constraints_for_labels(constraints,labels):
    constrains_for_label = dict()
    for label in labels:
        constrains_for_label[label] = []
    for constraint in constraints:
        constrains_for_label[constraint[1]].append(constraint[0] + constraint[2])
    return constrains_for_label


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))