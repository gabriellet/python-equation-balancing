import sympy as sp

def buildMatrix(lhs, rhs):

    # figure out number columns
    cols = len(lhs) + len(rhs)

    # figure out number rows
    l = {key for c in lhs.values()
             for key in c}  # noqa

    r = {key for c in rhs.values()
            for key in c}   # noqa

    rows = len(l | r)
    mat = sp.zeros(rows, cols)

    print(rows)
    print(cols)
    print(mat)
