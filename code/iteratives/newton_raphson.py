from __tools import *


def newton_raphson(expr, x0: float, tol: float, max_iter: int = 100) -> float:
    for i in range(max_iter):
        f_x0 = fx(expr, x0)
        df_x0 = diff_value(expr, x0)

        try:
            x1 = x0 - (f_x0 / df_x0)
            if abs((x1 - x0) / x1) < tol:
                return x1
        except TypeError:
            print(df_x0)
            print('> Newton-Raphson: divisão por 0 (f\'(x) = 0)')
            exit(-1)
        
        x0 = x1

    print('> O método de Newton-Raphson falhou em encontrar uma raiz dentro do número máximo de iterações.')
    return x0
    
    
def run():
    results = []
    expr, x_a, x_b, tol = read_file('input.txt')
    
    results.append({'name': 'newton-raphson', 'result': newton_raphson(expr, x_a, tol)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    