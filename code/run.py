from methods import *
from _tools import *


def run():
    if is_valid_interval(lower_end, upper_end):
        print('Bissecção: %25.5f' % bissection(lower_end, upper_end, tol))

    print('Posição Falsa: %21.5f' % false_position(lower_end, upper_end, tol))
    print('Newton-Raphson: %20.5f' % newton_raphson(lower_end, tol))
    print('Secant: %28.5f' % secant(lower_end, upper_end, tol))


# Chama a função principal
if __name__ == '__main__':
    run()
