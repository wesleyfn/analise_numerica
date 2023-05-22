import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            list_x, list_y = [], []
            for line in f.readlines():
                list_x += line.strip().split(',')[:1]
                list_y += line.strip().split(',')[1:]
                
            list_x = list(map(lambda x: float(sp.parse_expr(x)), list_x))
            list_y = list(map(lambda x: float(sp.parse_expr(x)), list_y))
            
        except (ValueError, TypeError):
            return None, None

    return list_x, list_y
            
def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)
        

def linear_regression(list_x, list_y):
    # Converte listas para arrays Numpy
    list_x = np.array(list_x)
    list_y = np.array(list_y)
    
    # Atribui o numero de valores em n
    n = list_x.size

    # Cálculo dos coeficientes a1 e a0
    a1 = (n * np.sum(list_x * list_y) - np.sum(list_x) * np.sum(list_y))
    a1 /= (n * np.sum(list_x**2) - np.sum(list_x)**2)
    a0 = np.mean(list_y) - a1 * np.mean(list_x)
    
    # Cálculo do coeficiente de determinacao
    ss_tot = np.sum((list_y - np.mean(list_y)) ** 2)
    ss_res = np.sum((list_y - (a0 + a1 * list_x)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    
    # Cria um polinomio utlizando os coedicientes a1 e a0
    poly = sp.N(sp.Poly([a1, a0], sp.symbols('x')).as_expr(), 7)
    
    # Retorna o polinomio linear e os coeficientes de determinação e correlação respectivamente
    return poly, round(r2, 7), round(np.sqrt(r2), 7)


def run():
    FILE_NAME = 'linear_input.txt'
    list_x, list_y = read_file(FILE_NAME)
    
    if list_x is not None:
        poly = linear_regression(list_x, list_y)
        save_results('output.txt', f'linear_regression: {poly}')

# Chama a função principal
if __name__ == '__main__':
    run()