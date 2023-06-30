from lu_factorization import lu_solve
from gauss_seidel import gauss_seidel
from gaussian_elimination import gaussian_elimination
from jacobi import jacobi
from __tools import read_system, save_results


def run_all():
    results = []
    x0 = [0., 0., 0.]
    matrix_A, vector_b, TOL, MAX_ITER = read_system('input.txt')
    
    results.append({
        'name': 'gaussian_elimination', 
        'result': gaussian_elimination(matrix_A, vector_b)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'lu_method', 
        'result': lu_solve(matrix_A, vector_b)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'jacobi',
        'result': jacobi(matrix_A, vector_b, x0, TOL, MAX_ITER)
    })
    save_results('output.txt', results)
    
    results.append({
        'name': 'gauss_seidel', 
        'result': gauss_seidel(matrix_A, vector_b, x0, TOL, MAX_ITER)
    })
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run_all()
    