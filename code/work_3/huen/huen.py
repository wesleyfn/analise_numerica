import os
import numpy as np
import sympy as sp

""" Entrada do arquivo:
    # expr - expressão algébrica
    # x0 - x inicial
    # xf - x final
    # y0 - y inicial
    # h - tamanho do passo
    # n_iterations - numero de iterações
"""

# Funções para entrada e saída de dados
def __read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.sympify(f.readline())
            x0 = float(f.readline())
            xf = float(f.readline())
            y0 = float(f.readline())
            h = float(f.readline())
            n_iterations = int(f.readline())
        except (ValueError, TypeError):
            return None, 0.0, 0.0, 0.0, 0, 0

    return expr, x0, xf, y0, h, n_iterations
            
def __save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)
   
     
def huen_method(expr, x0, xf, y0, h, n_iterations):
    list_x = np.arange(x0, xf + h, h)
    n_x = len(list_x)
    list_y = np.zeros(n_x)
    list_y[0] = y0
    
    symbols = list(sp.ordered(expr.free_symbols))
    symbols.append('y')
    def f(x, y):
        if isinstance(expr, sp.Expr):
            return sp.N(expr.subs([(symbols[0], x), (symbols[1], y)]))
        else:
            return expr
    
    for i in range(n_x-1):
        y_temp = list_y[i]
        for _ in range(n_iterations):
            k1 = f(list_x[i], 
                   y_temp)
            k2 = f(list_x[i+1], 
                   list_y[i] + h*k1)
            y_temp = list_y[i] + (h/2) * (k1+k2)

        list_y[i+1] = y_temp

    return list(list_x), list(list_y)

def run():
    FILE_NAME = 'input.txt'
    expr, x0, xf, y0, h, n_iterations = __read_file(FILE_NAME)
    
    if expr is not None:
        list_x, list_y = huen_method(expr, x0, xf, y0, h, n_iterations)
        output = 'huen_method:\n'
        
        for i in range(len(list_x)):
            output += f"x = {list_x[i]}, y = {list_y[i]}\n"
        
        __save_results('output.txt', output)
        return list_x, list_y

# Chama a função principal
if __name__ == '__main__':
    run()