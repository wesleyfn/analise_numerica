import sympy as sp
import os

sp.init_printing(order='grlex')

def read_file(file_name) -> tuple:
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            expr = sp.parse_expr(f.readline())
            x_a = float(sp.parse_expr(f.readline()))
            x_b = float(sp.parse_expr(f.readline()))
            TOL = float(f.readline())
            MAX_ITER = int(f.readline())
        except ValueError and TypeError:
            print('> ERROR: Verifique a formatação do arquivo de entrada.')
            exit(-1)
    
    expr = sp.N(expr)
    return expr, x_a, x_b, TOL, MAX_ITER


def save_results(file_name: str, results: list):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        for dict in results:
            f.write(f'{dict["name"]}={dict["result"]}\n')


def fx(expr, value: float) -> float:
    return expr.subs({'x': value})


def diff_value(expr, value: float) -> float:
    diff_expr = sp.diff(expr)
    return diff_expr.subs({'x': value})


def is_valid_interval(f_a: float, f_b: float) -> bool:
    if sp.ask(sp.Q.negative(f_a * f_b)):
        return True
    else:
        return False