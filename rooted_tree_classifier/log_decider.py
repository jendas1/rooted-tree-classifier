#!/usr/bin/env python3
import math

if __name__ == "__main__":
    from common import get_constraints_for_labels
else:
    from .common import get_constraints_for_labels

from math import gcd
from functools import reduce
import sys

VERBOSE = False

def listGcd(arr):
  return reduce(gcd, arr)

def countWalks(graph, src, dst, maxWalkLength):
    # Table to be filled up using DP.
    # The value count[i][j][e] will
    # store count of possible walks from
    # i to j with exactly k edges
    count = {i: {j: [0 for k in range(maxWalkLength + 1)] for j in graph} for i in graph}

    # Loop for number of edges from 0 to k
    for e in range(maxWalkLength + 1):
        for i in graph:  # for source
            for j in graph:  # for destination
                # initialize value
                count[i][j][e] = 0

                # from base cases
                if e == 0 and i == j:
                    count[i][j][e] = 1
                if e == 1 and (j in graph[i]):
                    count[i][j][e] = 1

                # go to adjacent only when the
                # number of edges is more than 1
                if e > 1:
                    for a in graph:
                        if a in graph[i]:  # adjacent of source i
                            count[i][j][e] += count[a][j][e - 1]
    return count[src][dst]

def isFlexible(graph, node):
    walkCounts = countWalks(graph, node, node, 2 * len(graph))
    bigL = []
    for idx, count in enumerate(walkCounts):
        if idx > 0 and count > 0:  # disregard a walk with 0 edges
            bigL.append(idx)
    return len(bigL) > 0 and listGcd(bigL) == 1

def isReachable(graph, src, dst):
  return len(list(filter(lambda x: x > 0, countWalks(graph, src, dst, len(graph))[1:]))) > 0

def isRepeatable(graph, node):
  return isReachable(graph, node, node)

def inflexible_labels(constraints, labels):
    graph = create_graph_from_problem(constraints, labels)
    il = []
    for label in labels:
        if not isFlexible(graph, label):
            il.append(label)
    return il

def unrepeatable_labels(constraints, labels):
    graph = create_graph_from_problem(constraints, labels)
    ul = []
    for label in labels:
        if not isRepeatable(graph, label):
            ul.append(label)
    return ul

def create_graph_from_problem(constraints, labels):
    constraints_for_labels = get_constraints_for_labels(constraints, labels)
    graph = {label: [] for label in labels}
    for label in labels:
        for constraint in constraints_for_labels[label]:
            if constraint[0] not in graph[label]:
                graph[label].append(constraint[0])
            if constraint[1] not in graph[label]:
                graph[label].append(constraint[1])
    return graph


def is_log_solvable(constraints):
    labels = list(set("".join(constraints)))

    while inflexible_labels(constraints, labels):
        il = inflexible_labels(constraints, labels)
        updated_constraints = []
        for constraint in constraints:
            if not (set(il) & set(constraint)): # keep only flexible labels
                updated_constraints.append(constraint)
        constraints = updated_constraints
        labels = list(set("".join(constraints)))
    if VERBOSE:
        print("Constraints:", constraints)
    return True if constraints else False

def polynomial_complexity(constraints):
    labels = list(set("".join(constraints)))
    k = 0
    ul = set(unrepeatable_labels(constraints, labels))

    constraints = recursive_removal_of_labels(constraints, labels, ul)
    labels = list(set("".join(constraints)))

    while inflexible_labels(constraints, labels):
        il = set(inflexible_labels(constraints, labels))
        constraints = recursive_removal_of_labels(constraints, labels, il)
        labels = list(set("".join(constraints)))
        k += 1
    if VERBOSE:
        print("Constraints:", constraints)
    return math.inf if constraints else k


def recursive_removal_of_labels(constraints, original_labels, labels_to_remove):
    while labels_to_remove:
        updated_constraints = []
        for constraint in constraints:
            if not (labels_to_remove & set(constraint)):  # keep only flexible labels
                updated_constraints.append(constraint)
        new_labels = set([constraint[1] for constraint in constraints])
        labels_to_remove = (set(original_labels) - labels_to_remove) - new_labels
        constraints = updated_constraints
    return constraints


def log_decider(constraints):
    if is_log_solvable(constraints):  # is not empty
        print("O(log n)")
    else:
        print("Ω(n)")

if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    log_decider(constraints)
