import pandas as pd
import sympy as sp
import toolz
from fractions import Fraction

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
    consts = [float(x) for x in consts]
    consts = [Fraction(x).limit_denominator() for x in consts]

    solns = list(toolz.interleave([headings, consts]))
    solns = list(toolz.partition(2, solns))
    return solns

def print_solns(solns):
    for a, b in solns:
        print(b + ': ' + a)

# things I did not consider: printing the equation in the correct order. oops
