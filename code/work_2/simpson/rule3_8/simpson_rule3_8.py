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
            
        except (ValueError, TypeError):
            return None, .0, .0

    return expr, a, b

def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)


def simpson_integration3_8(expr, a, b):
    # Define a função f que retornará o resultado de f(value)
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr

    h = (b - a)  # Tamanho do subintervalo
    list_x = np.linspace(a, b, 4)
    
    # Calcula a soma dos trapézios
    aprox_integral = (f(a) + 3*f(list_x[1]) + 3*f(list_x[2]) + f(b)) / 8
    # Multiplica pela largura do subintervalo
    aprox_integral *= h  

    exact_integral = sp.integrate(expr, ('x', a, b))
    error_percentual = ((exact_integral - aprox_integral) / exact_integral) * 100 
    
    return aprox_integral, round(error_percentual, 2)


def run():
    FILE_NAME = '3_8_input.txt'
    expr, a, b = read_file(FILE_NAME)
    
    if expr is not None:
        integral = simpson_integration3_8(expr, a, b)
        save_results('output.txt', f'simpson_integration3_8: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()