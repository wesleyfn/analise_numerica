import os
import sympy as sp


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
            
        except ValueError or TypeError:
            return None, 0.0, 0.0

    return expr, x, h
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)


def numerical_diff_2o(expr, x, h):
    def f(x):
        try:
            return sp.N(expr.subs({'x': x}))
        except AttributeError:
            return expr
    
    # Retorna a aproximação da derivada numérica de segunda ordem
    return sp.N(((f(x + h) - f(x))/h - (f(x) - f(x - h))/h) / h)

def run():
    FILE_NAME = 'input.txt'
    expr, x, h = read_file(FILE_NAME)
    
    coeffs = numerical_diff_2o(expr, x, h)
    save_results('output.txt', f'numerical_derivative: {coeffs}')

# Chama a função principal
if __name__ == '__main__':
    run()