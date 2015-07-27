import pandas as pd
import sympy as sp
import toolz

def solve_matrix(lhs_mat, rhs_mat):
    matrix = toolz.merge(lhs_mat, rhs_mat)
    df = pd.DataFrame(matrix)
    df[list(rhs_mat.keys())] *= -1
    df.replace("nan", 0)
    matrix = sp.Matrix(df.values.astype(int))
    solns = matrix.nullspace()
    headings = list(df.columns)

    print(solns)
    print(headings)
