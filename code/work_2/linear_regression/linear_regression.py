import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            list_x, list_y = [], []
            for line in f.readlines():
                list_x += line.strip().split(';')[:1]
                list_y += line.strip().split(';')[1:]
                
            list_x = list(map(lambda x: sp.N(sp.sympify(x)), list_x))
            list_y = list(map(lambda x: sp.N(sp.sympify(x)), list_y))
            
        except (ValueError, TypeError):
            return None, None

    return list_x, list_y
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)
        

def linear_regression(list_x, list_y):
    # Converte listas para arrays Numpy
    list_x = np.array(list_x)
    list_y = np.array(list_y)
    
    # Atribui o número de valores em n
    n = list_x.size

    # Cálculo dos coeficientes a1 e a0
    a1 = (n * np.sum(list_x * list_y) - np.sum(list_x) * np.sum(list_y))
    a1 /= (n * np.sum(list_x**2) - np.sum(list_x)**2)
    a0 = np.mean(list_y) - a1 * np.mean(list_x)
    
    # Soma dos quadrados totais
    s_tot = np.sum((list_y - np.mean(list_y)) ** 2)
    # Soma dos quadrados dos resíduos
    s_res = np.sum((list_y - (a0 + a1*list_x)) ** 2)

    # Cálculo do desvio padrão
    std_dev = (s_tot / (n - 1))**(1/2)
    # Cálculo do erro padrão da estimativa
    std_err = (s_res / (n - 2))**(1/2)
    # Cálculo do coeficiente de determinação
    r2 = 1 - (s_res / s_tot)
    
    # Cria um polinômio utilizando os coeficientes a1 e a0
    poly = sp.N(sp.Poly([a1, a0], sp.symbols('x')).as_expr(), 7)
    
    return poly, round(std_dev, 3), round(std_err, 3), round(r2, 3)


def run():
    FILE_NAME = 'linear_input.txt'
    list_x, list_y = read_file(FILE_NAME)
    
    if list_x is not None:
        poly = linear_regression(list_x, list_y)
        save_results('output.txt', f'linear_regression: {poly}')

# Chama a função principal
if __name__ == '__main__':
    run()