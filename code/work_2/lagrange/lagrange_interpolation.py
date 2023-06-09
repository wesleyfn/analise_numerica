import os
import numpy as np
import sympy as sp

"""
    lagrange_input (pontos):
        1; ln(1)
        4; ln(4)
        6; ln(6)
        5; ln(5)
"""

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            list_x, list_y = [], []
            for line in f.readlines():
                list_x += line.strip().split(';')[:1]
                list_y += line.strip().split(';')[1:]
                
            list_x = list(map(lambda x: sp.N(sp.sympify(x)), list_x))
            list_y = list(map(lambda x: sp.N(sp.sympify(x)), list_y))
            
        except (ValueError, TypeError):
            return None, None

    return list_x, list_y
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)
        

# Funções auxiliares para a aproximação
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
        
    return x[::-1]


def lagrange_interpolation(list_x, list_y):
    # Converte para numpy array se necessário
    list_y = np.array(list_y)
    list_x = np.array(list_x)

    n = len(list_x)
    polynomials = []
    
    for i in range(n):
        # Calcula o polinômio de Lagrange correspondente ao i-ésimo ponto
        index = np.arange(n) != i
        numerator = np.prod(sp.symbols('x') - list_x[index])
        denominator = np.prod(list_x[i] - list_x[index])
        
        # Multiplica o polinômio de Lagrange pelo valor y correspondente 
        polynomials.append(sp.N((numerator / denominator) * list_y[i], 7))
        
    # Soma os termos do polinômio interpolado
    interpolator = sum(polynomials)
    interpolator = sp.Poly(interpolator).as_expr() 
    
    return interpolator

def run():
    FILE_NAME = 'lagrange_input.txt'
    list_x, list_y = read_file(FILE_NAME)
    
    if list_x is not None:
        poly = lagrange_interpolation(list_x, list_y)
        save_results('output.txt', f'lagrange_interpolation: {poly}')

# Chama a função principal
if __name__ == '__main__':
    run()