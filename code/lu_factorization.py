import numpy as np
import sympy as sp

def check_matrix(matrix) -> bool:
    rank = np.linalg.matrix_rank(matrix)
    if rank == matrix.shape[0]:
        return True
    else:
        return False

def determinant(matrix) -> int | None:
    if not check_matrix(matrix):
        return None
    else:
        return np.linalg.det(matrix)

def read_system(file_name:str) -> tuple:
    with open(file_name) as f:
        system = [eq.strip() for eq in f.readlines()]

    try:
        exprs = [sp.parse_expr(eq.split('=')[0]) for eq in system]
        consts = [eq.split('=')[1] for eq in system]
    except SyntaxError as e:
        print(f'> ERROR: Verifique a formatação do arquivo de entrada.')
        exit(-1)
        
    vector_x = list(set().union(*[eq.free_symbols for eq in exprs]))
    vector_x = sorted(vector_x, key=lambda symbol: str(symbol))

    matrix_A = np.array([[eq.coeff(var) for var in vector_x] for eq in exprs], dtype=np.float64)
    vector_b = np.array(consts, dtype=np.float64)
    
    return matrix_A, vector_b


def lu_factorization(matrix_A):
    
    if determinant(matrix_A) == None:
        print('> ERROR: O sistema não tem solução ou possui multiplas soluções.')
        exit(-1)
    
    n = len(matrix_A)
    matrix_L = np.eye(n)
    matrix_U = np.zeros((n,n))
    
    for k in range(n):
        matrix_U[k, k] = matrix_A[k, k] - np.dot(matrix_L[k, :k], matrix_U[:k, k])
        for i in range(k+1, n):
            matrix_L[i, k] = (matrix_A[i, k] - np.dot(matrix_L[i, :k], matrix_U[:k, k])) / matrix_U[k, k]
        for j in range(k+1, n):
            matrix_U[k, j] = matrix_A[k, j] - np.dot(matrix_L[k, :k], matrix_U[:k, j])
            
    
    return matrix_L, matrix_U

def lu_solve(matrix_A, vector_b):
    L, U = lu_factorization(matrix_A)
    n = len(matrix_A)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        y[i] = vector_b[i] - np.dot(L[i, :i], y[:i])

    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x
    
mx_A, mx_b = read_system('../input_systems.txt')
print(lu_solve(mx_A, mx_b))
