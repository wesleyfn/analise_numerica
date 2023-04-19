from __tools import *


def bissection(expr, x_a: float, x_b: float, TOL: float, MAX_ITER: int = 100) -> float:
    f_a, f_b = fx(expr, x_a), fx(expr, x_b)
    
    if not is_valid_interval(f_a, f_b):
        return None
    
    for i in range(MAX_ITER):
        x_c = (x_a + x_b) / 2
        f_c = fx(expr, x_c)
        
        try:
            if min(abs((x_b - x_a) / x_b), abs(f_c)) < TOL:
                print(f'> Bissecção: {i} repetições.')
                return x_c
        except TypeError and ZeroDivisionError:
            print('> Bissecção: indeterminação')
            return None
        
        if sp.ask(sp.Q.negative(f_a * f_c)):
            x_b = x_c
        else:
            x_a = x_c

 
    print('> O método da bissecção atingiu o número máximo de iterações.')
    return x_c
    
def run():
    results = []
    expr, x_a, x_b, TOL, MAX_ITER = read_file('input.txt')
    
    results.append({
        'name': 'bissection', 
        'result': bissection(expr, x_a, x_b, TOL, MAX_ITER)
    })
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    