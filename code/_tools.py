import sympy as sp
import numpy as np

# Inicializa a impressão das expressões matemáticas em formato bonito
sp.init_printing(order='grlex')


# Importa a função f(x) do arquivo de entrada
with open('../input.txt') as file:
    expr = sp.parse_expr(file.readline())
    lower_end, upper_end = map(float, file.readline().split())
    tol = float(file.readline())
    diff_expr = sp.diff(expr)
    print(expr)


# Define a função f(x) utilizando a expressão importada do arquivo de entrada
def fx_value(value):
    return expr.subs({'x': value})

# Define a função f'(x) utilizando a expressão importada do arquivo de entrada


def diff_value(value):
    return diff_expr.subs({'x': value})


# Verifica se um intervalo [lower_end, upper_end] é válido
def is_valid_interval(lower_end, upper_end):
    f_lower_end, f_upper_end = fx_value(lower_end), fx_value(upper_end)

    if not sp.ask(sp.Q.real(f_lower_end) and sp.Q.real(f_upper_end)):
        return False

    if sp.ask(sp.Q.negative(f_lower_end * f_upper_end)):
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
