import os
import sympy as sp

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


def trapz_integration_s(expr, a, b):
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    h = (b - a)
    
    # Calcular a soma dos trapézios
    aprox_integral = h * ((f(a) + f(b)) / 2) 
    exact_integral = sp.integrate(expr, ('x', a, b))
    
    # Calcula o erro teórico
    error_percentual = ((exact_integral - aprox_integral) / exact_integral) * 100 
    
    # Retorna o resultado da integral aproximada e o erro teórico
    return aprox_integral, round(error_percentual, 2)


def run():
    FILE_NAME = 'simple_input.txt'
    expr, a, b = read_file(FILE_NAME)
    
    if expr is not None:
        integral = trapz_integration_s(expr, a, b)
        save_results('output.txt', f'trapz_integration_s: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()