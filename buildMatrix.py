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

    # return rows, cols, mat
    
    for j, chem in enumerate(lhs.keys()):
        for i, ele in enumerate(lhs[chem].keys()):
            mat[i,j] = lhs[chem][ele]
            
    for j, chem in enumerate(rhs.keys(), len(lhs)):
        for i, ele in enumerate(rhs[chem].keys()):
            mat[i,j] = -rhs[chem][ele]

    print(mat)

    return mat
