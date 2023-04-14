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


def gaussian_elimination(matrix_A, vector_b):

    if determinant(matrix_A) == None:
        print('> ERROR: O sistema não tem solução ou possui multiplas soluções.')
        exit(-1)

    n = len(matrix_A)
    vector_x = np.zeros(n)

    for i in range(n-1):
        max_index = i + np.argmax(abs(matrix_A[i:, i]))

        matrix_A[[i, max_index]] = matrix_A[[max_index, i]]
        vector_b[[i, max_index]] = vector_b[[max_index, i]]

        for j in range(i+1, n):
            mult = matrix_A[j, i] / matrix_A[i, i]
            matrix_A[j, i:] -= mult * matrix_A[i, i:]
            vector_b[j] -= mult * vector_b[i]

    for i in range(n-1, -1, -1):
        vector_x[i] = np.dot(matrix_A[i, i + 1:], vector_x[i + 1:])
        vector_x[i] = (vector_b[i] - vector_x[i]) / matrix_A[i, i]

    return vector_x


mx_A, mx_b = read_system('../input_systems.txt')
print(gaussian_elimination(mx_A, mx_b))
