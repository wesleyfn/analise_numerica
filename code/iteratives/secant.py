from __tools import *


def secant(expr, x0: float, x1: float, tol: float, max_iter: float = 100) -> float:
    f_x0, f_x1 = fx(expr, x0), fx(expr, x1)
    
    if sp.ask(sp.Q.zero(f_x0 * f_x1)):
        if sp.ask(sp.Q.zero(f_x0)):
            return x0
        else:
            return x1
    
    for i in range(max_iter):
        x2 = ((f_x1*x0 - f_x0*x1) / (f_x1 - f_x0))
        f_x2 = fx(expr, x2)
        
        try:
            if abs((x2 - x1) / x2) < tol:
                return x2
        except TypeError:
            print('> Secant: divisão por 0 (x2 = 0)')
            return None

        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f_x2

    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return x1

def run():
    results = []
    expr, x_a, x_b, tol = read_file('input.txt')
    
    results.append({'name': 'secant', 'result': secant(expr, x_a, x_b, tol)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    