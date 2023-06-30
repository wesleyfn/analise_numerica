import os
import sympy as sp

"""
    1o_input:
        expr = 2*x**2 - 5*x
        x = 2.0
        h = 1e-4
        method = forward
"""

def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            # Lê a primeira linha do arquivo e converte para expressão sympy
            expr = sp.parse_expr(f.readline())
            # Lê a segunda linha do arquivo e converte para float
            x = float(f.readline())
            # Lê a terceira linha do arquivo e converte para float
            h = float(f.readline())
            # Lê a quarta linha do arquivo
            method = f.readline().strip()
            
        except (ValueError, TypeError):
            return None, 0.0, 0.0, ''

    return expr, x, h, method
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)
        

def numerical_diff_1o(expr, xi, method='central', h=0.01):
    
    # A função hasattr verifica se há o atributo subs em expr, evita o AttributeError
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr

    if method == 'central' or method == '':
        return (f(xi + h) - f(xi - h)) / (2 * h)
    elif method == 'forward':
        return (f(xi + h) - f(xi)) / h
    elif method == 'backward':
        return (f(xi) - f(xi - h)) / h
    else:
        raise ValueError("Método deve ser 'central', 'forward' ou 'backward'.")


def run():
    FILE_NAME = '1o_input.txt'
    
    expr, x, h, method = read_file(FILE_NAME)
    if expr is not None:
        diff = numerical_diff_1o(expr, x, method, h)
        save_results('output.txt', f'numerical_derivative: {diff}')

# Chama a função principal
if __name__ == '__main__':
    run()