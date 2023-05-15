import os
import sympy as sp


def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0) # Limpa o conteúdo do arquivo
        f.write(result)

def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            # Lê a expressão da primeira linha do arquivo e avalia como uma expressão sympy
            expr = sp.parse_expr(f.readline())
            
            # Lê as linhas restantes como valores x e os converte para float
            list_x = list(map(lambda line: float(line), f.readlines()))
            
        except ValueError and TypeError:
            return None, []

    return expr, list_x


def trapz_integration_m(expr: sp.Expr, x: list) -> float:
    # Define a função f que retornará o resultado de f(value)
    f = lambda value: sp.N(expr.subs({'x': value}))
    
    n = len(x) - 1  # Número de subintervalos
    h = (x[-1] - x[0]) / n  # Tamanho do subintervalo

    # Calcula a soma dos trapézios
    integral = (f(x[0]) + f(x[-1])) / 2  # Primeiro e último termo
    integral += sum(f(x[i]) for i in range(1, n))

    integral *= h  # Multiplica pela largura do subintervalo

    return integral

def run():
    expr, list_x = read_file('input.txt')
    
    if expr is not None:
        integral = trapz_integration_m(expr, list_x)
        save_results('output.txt', f'trapz_integration_m: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()