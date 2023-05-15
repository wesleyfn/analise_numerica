import os
import numpy as np
import sympy as sp


def numerical_diff_2o(expr, x=sp.symbols('x'), h=1e-4):
    def f(x):
        try:
            return sp.N(expr.subs({'x': x}))
        except AttributeError:
            return expr
     
    # Retorna a aproximação da derivada numérica de segunda ordem
    return sp.N(((f(x + h) - f(x))/h - (f(x) - f(x - h))/h) / h)

def trapz_integration_s(expr, a: float, b: float) -> float:
    # f = f(x)
    def f(x):
        try:
            return sp.N(expr.subs({'x': x}))
        except AttributeError:
            return expr
        
    h = (b - a)  # Tamanho do subintervalo
    
    # Calcular a soma dos trapézios
    integral = h * ((f(a) + f(b)) / 2) 
    
    diff_2o = numerical_diff_2o(expr)
    error = -(h**3) * (sp.integrate(diff_2o, ('x', a, b)) / h)/12
    
    return integral, error

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
            # Lê a primeira linha do arquivo e converte para expressão sympy
            expr = sp.parse_expr(f.readline())
            # Lê a segunda linha do arquivo e converte para inteiro
            n = int(f.readline())
            # Lê a terceira linha do arquivo e converte para float os limites do intervalo
            a, b = list(map(lambda x: float(eval(x)), f.readline().split(',')))
            
        except ValueError or TypeError:
            return None, 0.0, 0.0, 0

    return expr, a, b, n
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)


def polyfit_continuous(expr, a, b, n):
    # Gera pontos de amostra igualmente espaçados
    x, _ = trapz_integration_s(expr, a, b)

    k = [1, sp.parse_expr('x'), sp.parse_expr('x**2')]

    matrix_u = []
    for i in range(n+1):
        for j in range(n+1):
            matrix_u.append(k[i] * k[j])
            
    print(matrix_u)        
    matrix_u = [trapz_integration_s(e, a, b)[0] for e in matrix_u]

    print(matrix_u)

def run():
    FILE_NAME = 'output.txt'
    expr, a, b, n = read_file('input.txt')
    polyfit_continuous(expr, a, b, n)
    
    """ coeffs = polyfit_continuous(expr, list_x, list_y, n)
    save_results(FILE_NAME, f'polyfit_continuous: {coeffs}') """
    
# Chama a função principal
if __name__ == '__main__':
    run()