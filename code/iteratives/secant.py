from __tools import *


def secant(expr, x0: float, x1: float, TOL: float, MAX_ITER: float = 100) -> float:
    f_x0, f_x1 = fx(expr, x0), fx(expr, x1)
    
    for i in range(MAX_ITER):
        x2 = x1 - (f_x1*(x1 - x0)) / (f_x1 - f_x0)
        f_x2 = fx(expr, x2)

        try:
            if min(abs((x1 - x0) / x1), abs(f_x2)) < TOL:
                print(f'> Secant: {i} repetições.')
                return x2
        except TypeError and ZeroDivisionError:
            print('> Secant: indeterminação!')
            return None

        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f_x2

    print('> O método da secant atingiu o número máximo de iterações.')
    return x2

def run():
    results = []
    expr, x_a, x_b, TOL, MAX_ITER = read_file('input.txt')
    
    results.append({
        'name': 'secant', 
        'result': secant(expr, x_a, x_b, TOL, MAX_ITER)
    })
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    