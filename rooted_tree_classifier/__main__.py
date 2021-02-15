import sys

from rooted_tree_classifier import decide_complexity




if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        VERBOSE = True
    constraints = input().split()
    decide_complexity(constraints)
