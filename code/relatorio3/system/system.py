import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            exprs = [sp.sympify(line.strip()) for line in f.readline().split(';')]
            list_y = [float(line.strip()) for line in f.readline().split(';')]
            x0 = float(f.readline())
            h = float(f.readline())
            n_x = int(f.readline())
        except (ValueError, TypeError):
            return None, [], 0.0, 0.0, 0, 0

    return exprs, list_y, x0, h, n_x

def save_results(file_name: str, result: str):
    with open(file_name, 'w') as f:
        f.write(result)

def fyy(solutions_y, expr):
    y_n = {}  # Dicionário para armazenar os valores de y
    last_key = list(solutions_y.keys())[-1]   # Obtém a última chave do dicionário
    last_index = len(solutions_y[last_key])-1  # Obtém o índice do último elemento na lista correspondente a last_key
    
    if hasattr(expr, 'subs'):  # Verifica se a expressão possui o método subs()
        for key, value_list in solutions_y.items():
            # Verifica se a chave é diferente da última chave
            # Se for diferente, o valor correspondente é obtido a partir do índice
            # Caso contrário, o valor correspondente é o último elemento da lista
            y_n[key] = value_list[last_index] if key != last_key else value_list[-1]
        
        return sp.N(expr.subs(y_n))  # Substitui os símbolos na expressão pelos valores de y e retorna o resultado numérico
    else:
        return expr  # Retorna a expressão original sem alterações


def runge_kutta_o4(expr, x0, solutions_y, h, n_x):
    pass


def euler_method(expr, x0, solutions_y, h, n_x):
    list_x = np.linspace(x0, x0 + n_x * h, n_x + 1)  # Lista de pontos x
    list_y = solutions_y['y' + str(len(solutions_y))][:]  # Copia a última lista de y disponível

    for _ in range(n_x):
        y0 = list_y[-1]  # Obtém o último valor de y
        list_y.extend([y0 + h * fyy(solutions_y, expr)])  # Calcula o próximo valor de y e o adiciona à lista
        solutions_y['y' + str(len(solutions_y))].append(list_y[-1])  # Adiciona o novo valor de y à lista correspondente

    return list(list_x), list(list_y)

def runge_kutta_o4(expr, x0, solutions_y, h, n_x):
    list_x = np.linspace(x0, x0 + n_x * h, n_x + 1)  # Lista de pontos x
    list_y = solutions_y['y' + str(len(solutions_y))][:]  # Copia a última lista de y disponível

    for _ in range(n_x):
        y0 = list_y[-1]  # Obtém o último valor de y
        k1 = h * fyy(solutions_y, expr)
        k2 = h * fyy(solutions_y, expr + k1 / 2)
        k3 = h * fyy(solutions_y, expr + k2 / 2)
        k4 = h * fyy(solutions_y, expr + k3)
        dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        list_y.extend([y0 + dy])  # Calcula o próximo valor de y e o adiciona à lista
        solutions_y['y' + str(len(solutions_y))].append(list_y[-1])  # Adiciona o novo valor de y à lista correspondente

    return list(list_x), list(list_y)

def system(exprs, list_y0, x0, h, n_x):
    # Inicializando as listas para armazenar as soluções
    list_x_sol = []
    list_y_sol = []
    solutions_y = {}

    # Loop para calcular as soluções para cada equação do sistema
    for i, expr in enumerate(exprs):
        key = 'y' + str(i + 1)
        solutions_y[key] = [list_y0[i]]

        # Chamando a função euler_method para calcular a solução para a equação i do sistema
        x_sol, y_sol = runge_kutta_o4(expr, x0, solutions_y, h, n_x)

        # Armazenando as soluções nas listas correspondentes
        list_x_sol.append(x_sol)
        list_y_sol.append(y_sol)
        solutions_y[key] = y_sol

    return list_x_sol, list_y_sol


def run():
    FILE_NAME = 'input.txt'
    exprs, list_y, x0, h, n_x = read_file(FILE_NAME)
    
    if exprs is not None:
        list_x_sol, list_y_sol = system(exprs, list_y, x0, h, n_x)

        # Formatando e salvando as soluções em um arquivo de saída
        output = ''
        for i in range(len(list_x_sol)):
            output += f"Solução para y{i + 1}(x):\n"
            for j in range(len(list_x_sol[i])):
                output += f"x = {list_x_sol[i][j]}, y{i + 1} = {list_y_sol[i][j]}\n"
            output += "\n"

        save_results('output.txt', output)

# Chama a função principal
if __name__ == '__main__':
    run()
