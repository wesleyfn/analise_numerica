import os
import sympy as sp


def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.sympify(f.readline())
            x = sp.sympify(f.readline())
            h = sp.sympify(f.readline())
            method = f.readline().strip()
            
        except (ValueError, TypeError):
            return None, 0.0, 0.0, ''

    return expr, x, h, method
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
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