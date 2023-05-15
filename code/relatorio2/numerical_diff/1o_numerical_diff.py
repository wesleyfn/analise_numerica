from __tools import *

def numerical_diff_1o(expr, x, method='central', h=0.01):
    f = lambda a: eval(expr, {'x': a})

    if method == 'central':
        return (f(x + h) - f(x - h)) / (2 * h)
    elif method == 'forward':
        return (f(x + h) - f(x)) / h
    elif method == 'backward':
        return (f(x) - f(x - h)) / h
    else:
        raise ValueError("Método deve ser 'central', 'forward' ou 'backward'.")


def run():
    ## dx = f_read_expr('input.txt')
    coeffs = numerical_diff_1o('x**2', 2)
    save_results('output.txt', f'numerical_derivative: {coeffs}')

# Chama a função principal
if __name__ == '__main__':
    run()