import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def __read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.sympify(f.readline())
            x0 = float(f.readline())
            y0 = float(f.readline())
            h = float(f.readline())
            n_h = int(f.readline())
        except (ValueError, TypeError):
            return None, 0.0, 0.0, 0.0, 0, 0

    return expr, x0, y0, h, n_h
            
def __save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)

    
def runge_kutta_o4(expr, x0, y0, h, n_x):
    list_x = np.linspace(x0, x0 + n_x * h, n_x+1)
    list_y = np.zeros(n_x+1)
    list_y[0] = y0
    
    symbols = list(expr.free_symbols)
    symbols.append(sp.Symbol('y'))
    
    def f(x, y):
        if isinstance(expr, sp.Expr):
            return sp.N(expr.subs([(symbols[0], x), (symbols[1], y)]))
        else:
            return expr
        
    for i in range(n_x):
        k1 = f(list_x[i], 
               list_y[i])
        k2 = f(list_x[i] + h/2, 
               list_y[i] + (h/2) * k1)
        k3 = f(list_x[i] + h/2, 
               list_y[i] + (h/2) * k2)
        k4 = f(list_x[i] + h, 
               list_y[i] + h * k3)

        list_y[i+1] = list_y[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6

    return list(list_x), list(list_y)

def run():
    FILE_NAME = 'input.txt'
    expr, x0, y0, h, n_h = __read_file(FILE_NAME)
    
    if expr is not None:
        list_x, list_y = runge_kutta_o4(expr, x0, y0, h, n_h)
        output = 'runge_kutta_o4:\n'
        
        for i in range(len(list_x)):
            output += f"x = {list_x[i]}, y = {list_y[i]}\n"
        
        __save_results('output.txt', output)
        return list_x, list_y

# Chama a função principal
if __name__ == '__main__':
    run()