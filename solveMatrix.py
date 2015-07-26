import pandas as pd
import sympy as sp
import toolz

def solve_matrix(lhs_mat, rhs_mat):
    matrix = toolz.merge(lhs_mat, rhs_mat)
    matrix = pd.DataFrame(matrix)
    matrix = matrix[list(rhs_mat.keys())] *= -1
    matrix.replace("nan", 0)
    matrix = sp.Matrix(matrix.values.astype(int))
    solns = matrix.nullspace()
    
    print(solns)



