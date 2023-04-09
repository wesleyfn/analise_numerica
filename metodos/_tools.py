import sympy as sp 


# Inicializa a impressão das expressões matemáticas em formato bonito
sp.init_printing(order='grlex')


# Importa a função f(x) do arquivo de entrada
with open('../input.txt') as file:
    expr = sp.parse_expr(file.readline())
    diff_expr = sp.diff(expr)
    lower_end, upper_end = map(float, file.readline().split())
    tolerance = float(file.readline())


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