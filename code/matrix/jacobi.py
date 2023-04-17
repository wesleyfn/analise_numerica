from __tools import *

def jacobi(matrix_A, vector_b, x0, tol, max_iter=100):
    n = len(matrix_A)
    x = np.copy(x0)
    x_new = np.zeros_like(x).astype(np.float64)
    
    for k in range(max_iter):
        for i in range(n):     
            s = sum(matrix_A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vector_b[i] - s) / matrix_A[i, i]
            
        if np.linalg.norm((x - x_new) / x_new) < tol:
            return x_new
        
        x = x_new
    return x
    

def run():
    results = []
    x0 = [0., 0., 0.]
    mx_A, mx_b, tol = read_system('input.txt')
    
    results.append({'name': 'jacobi', 'result': jacobi(mx_A, mx_b, x0, tol)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    
