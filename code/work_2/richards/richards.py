import os
import sympy as sp
import numpy as np

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            h1 = float(f.readline())
            h2 = float(f.readline())
            
        except (ValueError, TypeError):
            return None, 0.0

    return h1, h2

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

def trapz_integration_m(expr, a, b, n) -> float:
    # Define a função f que retornará o resultado de f(x)
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    # Tamanho do subintervalo
    h = (b - a)

    # Gera uma lista de n valores x entre a e b, inclusos, igualmente espaçados
    list_x = np.linspace(a, b, n)
    
    # Calcula a soma dos trapézios
    integral_aprox = (f(a) + f(b)) # Primeiro e último termo
    integral_aprox += (2 * sum(f(list_x[i]) for i in range(1, n))) / (2*n)

    integral_aprox *= h  # Multiplica pela largura do subintervalo

    return integral_aprox

def richardson_extrapolation(h1, h2):
    result = (4/3)*h2 - (1/3)*h1
    
    return result

def run():
    FILE_NAME = 'richards_input.txt'
    h1, h2 = read_file(FILE_NAME)
    
    if h1 is not None:
        aprox = richardson_extrapolation(h1, h2)
        save_results('output.txt', f'richardson_extrapolation: {aprox}')

# Chama a função principal
if __name__ == '__main__':
    run()