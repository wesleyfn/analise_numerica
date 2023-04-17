from __tools import *


def gauss_seidel(matrix_A, vector_b, x0, tol, max_iter=100):
    n = len(matrix_A)
    x = np.copy(x0)
    x_new = np.zeros_like(x).astype(np.float64)
    
    for k in range(max_iter):
        aux = np.copy(x)
        for i in range(n):
            s = sum(matrix_A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vector_b[i] - s) / matrix_A[i, i]
            x[i] = x_new[i]
            
        if np.linalg.norm((aux - x_new) / x_new) < tol:
            return x_new
        
        x = x_new
    return x

def run():
    results = []
    x0 = [0., 0., 0.]
    mx_A, mx_b, tol = read_system('input.txt')
    
    results.append({'name': 'gauss_seidel', 'result': gauss_seidel(mx_A, mx_b, x0, tol)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    