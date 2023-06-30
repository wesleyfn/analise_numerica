import os
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            # Lê a primeira linha do arquivo e converte para expressão sympy
            expr = sp.parse_expr(f.readline())
            # Lê a segunda linha do arquivo e converte para float
            x = float(f.readline())
            # Lê a terceira linha do arquivo e converte para float
            h = float(f.readline())
            
        except (ValueError, TypeError):
            return None, 0.0, 0.0

    return expr, x, h
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)


def numerical_diff_2o(expr, x, h):
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    # Retorna a aproximação da derivada numérica de segunda ordem
    return sp.N(((f(x + h) - f(x))/h - (f(x) - f(x - h))/h) / h)

def run():
    FILE_NAME = '2o_input.txt'
    expr, x, h = read_file(FILE_NAME)
    
    if expr is not None:
        diff = numerical_diff_2o(expr, x, h)
        save_results('output.txt', f'numerical_derivative: {diff}')

# Chama a função principal
if __name__ == '__main__':
    run()