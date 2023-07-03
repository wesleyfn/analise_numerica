import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            exprs = [sp.sympify(line.strip()) for line in f.readline().split(';')]
            list_y0 = [float(line.strip()) for line in f.readline().split(';')]
            x0 = float(f.readline())
            xf = float(f.readline())
            h = float(f.readline())

        except (ValueError, TypeError):
            return None, [], 0.0, 0.0, 0.0, 0

    return exprs, list_y0, x0, xf, h

def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)
        

def f(expr, y1, y2):
    return expr.subs({'y1': y1, 'y2': y2})

def system_edo_euler(exprs, list_y0, x0, xf, h):
    # Obtém o número de variáveis dependentes
    n_y = len(list_y0)
    
    # Cria uma lista de pontos x
    list_x = list(np.arange(x0, xf + h, h))
    
    # Inicializa a matriz para armazenar as soluções
    n_x = len(list_x)
    yn = np.zeros((n_y, n_x))
    yn[:, 0] = list_y0
    
    # Itera sobre os passos de integração
    for i in range(n_x-1):
        # Calcula as derivadas para as variáveis dependentes atuais
        y1_next = yn[0, i] + h * f(exprs[0], yn[0, i], yn[1, i])
        y2_next = yn[1, i] + h * f(exprs[1], yn[0, i], yn[1, i])
        
        # Armazena as variáveis dependentes atualizadas
        yn[:, i+1] = [y1_next, y2_next]
    
    # Cria uma lista de listas com os valores das variáveis dependentes
    list_y = [list(yn[0, :]), list(yn[1, :])]
    
    # Retorna as listas de pontos x e valores y
    return list_x, list_y

def run():
    FILE_NAME = 'input.txt'
    exprs, list_y0, x0, xf, h = read_file(FILE_NAME)

    if exprs is not None:
        x_sol, y_sol = system_edo_euler(exprs, list_y0, x0, xf, h)

        # Formatando e salvando as soluções em um arquivo de saída
        output = "system_edo_euler:\n"
        for j in range(len(x_sol)):
            output += f"x = {x_sol[j]}, y1 = {y_sol[0][j]:.16f}, y2 = {y_sol[1][j]}\n"

        save_results('output.txt', output)

# Chama a função principal
if __name__ == '__main__':
    run()
