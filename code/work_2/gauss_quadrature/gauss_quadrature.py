import os
import sympy as sp
import numpy as np

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            expr = sp.sympify(f.readline())
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
    exact_integral = sp.integrate(expr, ('x', a, b))
    
    error_perc = ((exact_integral - aprox_integral) / exact_integral) * 100
    
    return aprox_integral, round(error_perc, 2) 


def run():
    FILE_NAME = 'gauss_input.txt'
    expr, a, b, n = read_file(FILE_NAME)
    
    if expr is not None:
        integral = gauss_quadrature(expr, a, b, n)
        save_results('output.txt', f'gauss_quadrature: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()