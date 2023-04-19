from bissection import bissection
from false_position import false_position
from secant import secant
from newton_raphson import newton_raphson
from __tools import read_file, save_results


def run_all():
    results = []
    expr, x_a, x_b, tol, max_iter = read_file('input.txt')
    
    results.append({
        'name': 'bissection', 
        'result': bissection(expr, x_a, x_b, tol, max_iter)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'false_position',
        'result': false_position(expr, x_a, x_b, tol, max_iter)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'secant', 
        'result': secant(expr, x_a, x_b, tol, max_iter)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'newton-raphson', 
        'result': newton_raphson(expr, x_a, tol, max_iter)
    })
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run_all()
    