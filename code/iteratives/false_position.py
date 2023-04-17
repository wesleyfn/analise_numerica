from __tools import *


def false_position(expr, x_a: float, x_b: float, tol: float, max_iter: int = 100) -> float:
    f_a, f_b = fx(expr, x_a), fx(expr, x_b)
    
    
    if sp.ask(sp.Q.zero(f_a * f_b)):
        if sp.ask(sp.Q.zero(f_a)):
            return x_a
        else:
            return x_b
    
    if not is_valid_interval(f_a, f_b):
        return None
    
    f_c = 0
    for i in range(max_iter):
        x_c = (x_a*f_b - x_b*f_a) / (f_b - f_a)
        f_c = fx(expr, x_c)
        
        if sp.ask(sp.Q.zero(f_c)) or f_c < tol:
            return x_c
        elif sp.ask(sp.Q.negative(f_a * f_c)):
            x_b = x_c
            f_b = f_c
        else:
            x_a = x_c
            f_a = f_c
        
        try:
            if abs((f_a - f_b) / f_a) < tol:
                return f_c
        except:
            print('> Posição Falsa: divisão por 0 (f_a = 0)')
            return None
                        
    print('> O método da posição falsa falhou em encontrar uma raiz dentro do número máximo de iterações.')
    return f_c

def run():
    results = []
    expr, x_a, x_b, tol = read_file('input.txt')
    
    results.append({'name': 'false_position', 'result': false_position(expr, x_a, x_b, tol)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    