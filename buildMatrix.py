from itertools import chain
import sympy as sp

def buildMatrix(lhs, rhs):

    # figure out number columns
    cols = len(lhs) + len(rhs)

    # figure out number rows
    l = []
    for c in lhs:
        l = chain(l, list(lhs[c].keys()))

    for c in rhs:
        l = chain(l, list(rhs[c].keys()))

    t = list(l)
    r = set(t)
    rows = len(r)

    mat = sp.zeros(rows, cols)

    print(rows)
    print(cols)
    print(mat)
