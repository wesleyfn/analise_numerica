from __tools import *


def newton_raphson(expr, x0: float, TOL: float, MAX_ITER: int = 100) -> float:
    for i in range(MAX_ITER):
        f_x0 = fx(expr, x0)
        df_x0 = diff_value(expr, x0)

        try:
            x1 = x0 - (f_x0 / df_x0)
            if min(abs((x1 - x0) / x1), abs(f_x0)) < TOL:
                print(f'> Newton-Raphson: {i} repetições.')
                return x1
        except TypeError:
            print('> Newton-Raphson: indeterminação!')
            return None
        
        x0 = x1

    print('> O método de Newton-Raphson atingiu o número máximo de iterações.')
    return x0
    
    
def run():
    results = []
    expr, x_a, x_b, TOL, MAX_ITER = read_file('input.txt')
    
    results.append({'name': 'newton-raphson', 'result': newton_raphson(expr, x_a, TOL, MAX_ITER)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    