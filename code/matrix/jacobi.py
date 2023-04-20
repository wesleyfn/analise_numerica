from __tools import *


def jacobi(matrix_A, vector_b, x0, TOL, MAX_ITER=100):
    n = len(matrix_A)
    x = np.copy(x0)
    x_new = np.zeros_like(x).astype(np.float64)
    
    for k in range(MAX_ITER):
        for i in range(n):     
            s = sum(matrix_A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vector_b[i] - s) / matrix_A[i, i]
            
        if np.linalg.norm((x - x_new) / x_new) < TOL:
            return x_new
        
        x = x_new
    
    print('> O método de Jacobi atingiu o número máximo de iterações.')
    return x
    

def run():
    results = []
    x0 = [0., 0., 0.]
    mx_A, mx_b, TOL, MAX_ITER = read_system('input.txt')
    
    results.append({'name': 'jacobi', 'result': jacobi(mx_A, mx_b, x0, TOL, MAX_ITER)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    
