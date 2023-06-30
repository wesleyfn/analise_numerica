import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.sympify(f.readline())
            x0 = float(f.readline())
            y0 = float(f.readline())
            h = float(f.readline())
            n_h = int(f.readline())
        except (ValueError, TypeError):
            return None, 0.0, 0.0, 0.0, 0

    return expr, x0, y0, h, n_h
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)

def show_plot(result_x, result_y):
    plt.plot(result_x, result_y, label='Euler Modified')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Resultado do Método de Euler')
    plt.legend()
    plt.grid(True)
    plt.show()
  
def euler_modified(expr, x0, y0, h, n_h):
    list_x = np.linspace(x0, x0 + n_h * h, n_h + 1)
    list_y = np.zeros(n_h + 1)
    list_y[0] = y0
    
    symbols = list(expr.free_symbols)
    symbols.append(sp.Symbol('y'))
    
    def f(x, y):
        if isinstance(expr, sp.Expr):
            return sp.N(expr.subs([(symbols[0], x), (symbols[1], y)]))
        else:
            return expr
    
    for i in range(n_h):
        k1 = f(list_x[i], 
               list_y[i])
        k2 = f(list_x[i] + h/2, 
               list_y[i] + (h/2)*k1)
        list_y[i+1] = list_y[i] + h * k2

    return list(list_x), list(list_y)

def run():
    FILE_NAME = 'input.txt'
    expr, x0, y0, h, n_h = read_file(FILE_NAME)
    
    if expr is not None:
        list_x, list_y = euler_modified(expr, x0, y0, h, n_h)
        output = 'euler_modified:\n'
        
        for i in range(len(list_x)):
            output += f"x = {list_x[i]}, y = {list_y[i]}\n"
        
        save_results('output.txt', output)
        
    show_plot(list_x, list_y)

# Chama a função principal
if __name__ == '__main__':
    run()