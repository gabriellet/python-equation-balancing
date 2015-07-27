import pandas as pd
import sympy as sp
import toolz

def solve_matrix(lhs_mat, rhs_mat):
    df = toolz.merge(lhs_mat, rhs_mat)
    df = pd.DataFrame(df)
    df[list(rhs_mat.keys())] *= -1
    # df.replace("nan", 0)
    df = df.fillna(value=0)
    matrix = sp.Matrix(df.values.astype(int))
    consts = matrix.nullspace()
    headings = list(df.columns)
    consts = consts[0].values()
    solns = list(toolz.interleave([headings, consts]))
    solns = list(toolz.partition(2, solns))
    return solns
