import os
import numpy as np


def lu_factorization(matrix_A):
    if np.linalg.det(matrix_A) == 0:
        raise Exception('> Derivada resultou em 0')
    
    n = len(matrix_A)
    matrix_L = np.eye(n)
    matrix_U = np.zeros((n,n))
    
    
    for k in range(n):
        matrix_U[k, k] = matrix_A[k, k] - np.dot(matrix_L[k, :k], matrix_U[:k, k])
        
        # Preenche a matriz L e a matriz U
        for i in range(k+1, n):
            matrix_L[i, k] = (matrix_A[i, k] - np.dot(matrix_L[i, :k], matrix_U[:k, k])) / matrix_U[k, k]
        for j in range(k+1, n):
            matrix_U[k, j] = matrix_A[k, j] - np.dot(matrix_L[k, :k], matrix_U[:k, j])
    
    return matrix_L, matrix_U

def lu_solve(matrix_A, vector_b):
    matrix_L, matrix_U = lu_factorization(matrix_A)

    n = len(matrix_A)
    y = x = np.zeros(n)

    # Resolve Ly = b
    for i in range(n):
        y[i] = vector_b[i] - np.dot(matrix_L[i, :i], y[:i])

    # Resolve Ux = y
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(matrix_U[i, i+1:], x[i+1:])) / matrix_U[i, i]
        
    return x


def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            n = int(f.readline().strip())
            x_values, y_values = [], []
            for line in f.readlines():
                x_values += line.strip().split(',')[:1]
                y_values += line.strip().split(',')[1:]
                
            x_values = list(map(lambda x: np.float64(eval(x)), x_values))
            y_values = list(map(lambda x: np.float64(eval(x)), y_values))
            
        except ValueError and TypeError:
            return None, None, None

    return x_values, y_values, n
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)


def polyfit_discrete(x, y, n):
    # Converte listas para arrays Numpy
    x = np.array(x)
    y = np.array(y)
    
    # Cria a matriz de Vandermonde
    matrix_u = np.vander(x, n+1, increasing=True)

    matrix_A = []
    # Calcula os produtos internos para preencher a matriz A
    for i in range(n+1):
        matrix_A.append(np.dot(matrix_u[:, i], matrix_u[:, range(n+1)]))

    matrix_A = np.asfarray(matrix_A, np.float64)
    
    # Calcula o produto interno para obter o vetor b
    vector_b = np.asfarray(np.dot(y, matrix_u[:, range(n+1)]), np.float64)
    
    # Resolve o sistema de equações lineares usando a fatorização LU
    coeffs = lu_solve(matrix_A, vector_b)
    return coeffs


def run():
    FILE_NAME = 'output.txt'
    x, y, n = read_file('input.txt')
    
    coeffs = polyfit_discrete(x, y, n)
    save_results(FILE_NAME, f'polyfit_discrete: {coeffs}')
    
# Chama a função principal
if __name__ == '__main__':
    run()