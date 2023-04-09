from methods import *
from _tools import *


def run():
    if is_valid_interval(lower_end, upper_end):
        print(f'\nBissecção:\n')
        print(f'{bissection(lower_end, upper_end, tolerance):.6f}')

    print(f'\nPosição Falsa:\n')
    print(f'{false_position(lower_end, upper_end, tolerance):.6f}')

    print(f'\nNewton-Raphson:\n')
    print(f'{newton_raphson(lower_end, tolerance):.6f}')

    print(f'\nSecant:\n')
    print(f'{secant(lower_end, upper_end, tolerance):.6f}')


# Chama a função principal
if __name__ == '__main__':
    run()
