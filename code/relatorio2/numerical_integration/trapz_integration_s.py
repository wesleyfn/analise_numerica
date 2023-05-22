import os
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            expr = sp.parse_expr(f.readline())
            a = float(f.readline())
            b = float(f.readline())
            
        except (ValueError, TypeError):
            return None, .0, .0

    return expr, a, b

def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0) # Limpa o conteúdo do arquivo
        f.write(result)

# Função auxiliar para a aproximação
def numerical_diff_2o(expr, x, h):
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    # Retorna a aproximação da derivada numérica de segunda ordem
    return sp.N(((f(x + h) - f(x))/h - (f(x) - f(x - h))/h) / h)


def trapz_integration_s(expr, a, b):
    f = lambda x: sp.N(expr.subs({'x': x})) if hasattr(expr, 'subs') else expr
    
    h = (b - a)
    
    # Calcular a soma dos trapézios
    aprox_integral = h * ((f(a) + f(b)) / 2) 
    exact_integral = sp.integrate(expr, ('x', a, b))
    
    # Calcula o erro teórico
    diff_2o = numerical_diff_2o(expr, sp.symbols('x'), 1e-4)
    error_t = -(h**3) * (sp.integrate(diff_2o, ('x', a, b)) / h)/12
    error_percentual = ((exact_integral - aprox_integral) / exact_integral) * 100 
    
    # Retorna o resultado da integral aproximada e o erro teórico
    return aprox_integral, error_t, round(error_percentual, 2)


def run():
    FILE_NAME = 'simple_input.txt'
    expr, a, b = read_file(FILE_NAME)
    
    if expr is not None:
        integral = trapz_integration_s(expr, a, b)
        save_results('output.txt', f'trapz_integration_s: {integral}')

# Chama a função principal
if __name__ == '__main__':
    run()