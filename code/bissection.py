import sympy as sp
import numpy as np

sp.init_printing(order='grlex')

expr = diff_expr = x_a = x_b = tol = 0


def read_file(file_name):
    with open(file_name, 'r') as f:
        expr = sp.parse_expr(f.readline())
        x_a = float(f.readline())
        x_b = float(f.readline())
        tol = float(f.readline())


def save_results(file_name, *results):
    with open(file_name, 'w') as f:
        for result in results:
            f.write(f'{result[0]}={result[1]}')


def fx(value):
    return expr.subs({'x': value})


def diff_value(value):
    return diff_expr.subs({'x': value})


def is_valid_interval(x_a, x_b):
    f_a, f_b = fx(x_a), fx(x_b)

    if not sp.ask(sp.Q.real(f_a) and sp.Q.real(f_b)):
        return False

    if sp.ask(sp.Q.negative(f_a * f_b)):
        return True
    else:
        return False


def pivoting(n, coef_mx, const_mx):
    for i in range(n-1):
        # Encontra o índice da linha com o maior valor absoluto na coluna abaixo do pivô atual
        max_index = i + np.argmax(abs(coef_mx[i:, i]))

        # Troca a linha atual com a linha do valor máximo
        coef_mx[[i, max_index]] = coef_mx[[max_index, i]]
        const_mx[[i, max_index]] = const_mx[[max_index, i]]


def bissection(x_a: float, x_b: float, tol: float, max_iter: int = 100) -> float:
    estimate = (x_a + x_b) / 2
    prev_estimate = 0

    for i in range(max_iter):
        prev_estimate = estimate
        
        f_sign_product = fx(x_a) * fx(estimate)

        if sp.ask(sp.Q.zero(f_sign_product)):
            return estimate
        elif sp.ask(sp.Q.negative(f_sign_product)):
            x_b = estimate
        else:
            x_a = estimate

        estimate = (x_a + x_b) / 2
        rel_error = abs((estimate - prev_estimate) / estimate)
        
        if rel_error < tol:
            return estimate
        
    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return estimate