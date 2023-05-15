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
            expr = sp.parse_expr(f.readline())
            a, b = list(map(lambda line: float(line), f.readlines()))
            
        except ValueError and TypeError:
            return None, .0, .0

    return expr, a, b


def trapz_integration_s(expr, a: float, b: float) -> float:
    # f = f(x)
    def f(x):
        try:
            return sp.N(expr.subs({'x': x}))
        except AttributeError:
            return expr
        
    h = (b - a)  # Tamanho do subintervalo
    
    # Calcular a soma dos trapézios
    integral = h * ((f(a) + f(b)) / 2) 
    
    diff_2o = numerical_diff_2o(expr)
    error = -(h**3) * (sp.integrate(diff_2o, ('x', a, b)) / h)/12
    
    return integral, error


def run():
    expr, a, b = read_file('input.txt')
    
    if expr is not None:
        integral = trapz_integration_s(expr, a, b)
        save_results('output.txt', f'trapz_integration_m: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()