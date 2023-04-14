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


def read_system(file_name: str) -> tuple:
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

def gauss_seidel(matrix_A, vector_b, x0, tol, max_iter=100):
    n = len(matrix_A)
    x = np.copy(x0)
    x_new = np.zeros_like(x).astype(np.float64)
    
    for k in range(max_iter):
        aux = np.copy(x)
        for i in range(n):
            s = sum(matrix_A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vector_b[i] - s) / matrix_A[i, i]
            x[i] = x_new[i]
            
        if np.linalg.norm((aux - x_new) / x_new) < tol:
            return x_new
        
        x = x_new
    return x
    
mx_A, mx_b = read_system('../input_systems.txt')
print(gauss_seidel(mx_A, mx_b, [0.,0.,0.], 1e-4))