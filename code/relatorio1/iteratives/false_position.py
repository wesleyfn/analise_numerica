from __tools import *


def false_position(expr, x_a: float, x_b: float, TOL: float, MAX_ITER: int = 100) -> float:
    f_a, f_b = fx(expr, x_a), fx(expr, x_b)
    
    if not is_valid_interval(f_a, f_b):
        return None
    
    for i in range(MAX_ITER):
        x_c = (f_b*x_a - f_a*x_b) / (f_b - f_a)
        f_c = fx(expr, x_c)
        
        try:
            if min(abs((x_b - x_a) / x_b), abs(f_c)) < TOL:
                print(f'> Posição Falsa: {i} repetições.')
                return x_c
        except TypeError and ZeroDivisionError:
            print('> Posição Falsa: indeterminação!')
            return None
        
        if sp.ask(sp.Q.negative(f_a * f_c)):
            x_b, f_b = x_c, f_c
        else:
            x_a, f_a = x_c, f_c
                        
    print('> O método da posição falsa atingiu o número máximo de iterações.')
    return x_c

def run():
    results = []
    expr, x_a, x_b, TOL, MAX_ITER = read_file('input.txt')
    
    results.append({
        'name': 'false_position', 
        'result': false_position(expr, x_a, x_b, TOL, MAX_ITER)
    })
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    