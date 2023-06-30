import os
import numpy as np
import sympy as sp

def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.parse_expr(f.readline())
            a = float(f.readline())
            b = float(f.readline())
            n = int(f.readline())
            
        except (ValueError, TypeError):
            return None, .0, .0, 0

    return expr, a, b, n
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)


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

def gauss_quadrature(expr, a, b, n):
    f = lambda expr, x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    # Obtem n pontos e pesos da quadratura de gauss
    list_x, list_c = np.polynomial.legendre.leggauss(n)
    
    new_expr = expr
    if ([a, b] != [-1.0, 1.0]):
        x = ((b - a) + (b - a)*sp.symbols('x')) / 2
        dx = (b - a) / 2
        new_expr = (f(expr, x)) * dx

    aprox_integral = sum(list_c[i]*f(new_expr, list_x[i]) for i in range(n))
    return aprox_integral

def polyfit_continuous(expr, a, b, n):
    k = [sp.parse_expr(f'x**{i}') for i in range(n+1)]

    matrix_A = []
    # Calcula o produto externo resultando em uma matriz de ordem n+1
    for i in range(n+1):
        for j in range(n+1):
            product = k[i] * k[j]
            integral = gauss_quadrature(product, a, b, n*n)
            matrix_A.append(integral)
    
    vector_b = [expr * k[i] for i in range(n+1)]
    vector_b = [gauss_quadrature(e, a, b, n*n) for e in vector_b]

    matrix_A = np.array(matrix_A, dtype=float).reshape(n+1,n+1)
    vector_b = np.array(vector_b, dtype=float)
    
    poly = sp.N(sp.Poly(lu_solve(matrix_A, vector_b), sp.symbols('x')).as_expr())
    return poly

def run():
    FILE_NAME = 'continuous_input.txt'
    expr, a, b, n = read_file(FILE_NAME)
    
    if expr is not None:
        poly = polyfit_continuous(expr, a, b, n)
        save_results('output.txt', f'polyfit_continuous: {poly}')
    
# Chama a função principal
if __name__ == '__main__':
    run()