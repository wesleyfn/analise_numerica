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
            n_seg = int(f.readline())
            
        except (ValueError, TypeError):
            return None, .0, .0, 0

    return expr, a, b, n_seg

def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)


def trapz_integration_m(expr, a, b, n_seg) -> float:
    # Define a função f que retornará o resultado de f(x)
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    # Tamanho do subintervalo
    h = (b - a)
    n = n_seg + 1
    
    # Gera uma lista de n valores x entre a e b, inclusos, igualmente espaçados
    list_x = np.linspace(a, b, n)
    
    # Calcula a soma dos trapézios
    aprox_integral = (f(a) + f(b)) # Primeiro e último termo
    aprox_integral += (2 * sum(f(list_x[i]) for i in range(1, n))) / (2*n)

    aprox_integral *= h # Multiplica pela largura do subintervalo
    
    exact_integral = sp.integrate(expr, ('x', a, b))
    error_percentual = ((exact_integral - aprox_integral) / exact_integral) * 100 

    return aprox_integral, round(error_percentual, 2)

def run():
    FILE_NAME = 'multi_input.txt'
    expr, a, b, n_seg = read_file(FILE_NAME)
    
    if expr is not None:
        integral = trapz_integration_m(expr, a, b, n_seg)
        save_results('output.txt', f'trapz_integration_m: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()