import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            expr = sp.parse_expr(f.readline())
            x0 = float(f.readline())
            y0 = float(f.readline())
            h = float(f.readline())
            n = int(f.readline())
        except (ValueError, TypeError):
            return None, 0.0, 0.0, 0.0, 0

    return expr, x0, y0, h, n
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)
        
def euler_modified(expr, x0, y0, h, n_x):
    list_x = np.linspace(x0, x0 + n_x * h, n_x+1)
    list_y = np.zeros(n_x+1)
    list_y[0] = y0
    
    f = lambda x, y: sp.N(expr.subs({'x': x, 'y': y})) if hasattr(expr, 'subs') else expr
    for i in range(n_x):
        k1 = f(list_x[i], list_y[i])
        k2 = f(list_x[i] + h/2, list_y[i] + (h/2)*k1)
        list_y[i+1] = list_y[i] + h * k2

    return list(list_x), list(list_y)

def run():
    FILE_NAME = 'input.txt'
    expr, x0, y0, h, n = read_file(FILE_NAME)
    
    #if expr is not None:
    list_x, list_y = euler_modified(expr, x0, y0, h, n)
    save_results('output.txt', f'euler_modified: x={list_x}, y={list_y}')

# Chama a função principal
if __name__ == '__main__':
    run()