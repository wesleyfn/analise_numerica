import os
import numpy as np
import sympy as sp

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            n = int(f.readline().strip())
            x_values, y_values = [], []
            for line in f.readlines():
                x_values += line.strip().split(';')[:1]
                y_values += line.strip().split(';')[1:]
                
            x_values = list(map(lambda x: sp.N(sp.sympify(x)), x_values))
            y_values = list(map(lambda x: sp.N(sp.sympify(x)), y_values))
            
        except (ValueError, TypeError):
            return None, None, 0

    return x_values, y_values, n
            
def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)

# Funções auxiliares para a aproximação
def lu_factorization(matrix_A):
    if np.linalg.det(matrix_A) == 0:
        raise Exception('> Derivada resultou em 0')
    
    n = len(matrix_A)
    matrix_L = np.eye(n)
    matrix_U = np.zeros((n,n))
    
    
    for k in range(n):
        matrix_U[k, k] = matrix_A[k, k] - np.dot(matrix_L[k, :k], matrix_U[:k, k])
        
        # Preenche a matriz L e a matriz U
        for i in range(k+1, n):
            matrix_L[i, k] = (matrix_A[i, k] - np.dot(matrix_L[i, :k], matrix_U[:k, k])) / matrix_U[k, k]
        for j in range(k+1, n):
            matrix_U[k, j] = matrix_A[k, j] - np.dot(matrix_L[k, :k], matrix_U[:k, j])
    
    return matrix_L, matrix_U

def lu_solve(matrix_A, vector_b):
    matrix_L, matrix_U = lu_factorization(matrix_A)

    n = len(matrix_A)
    y = x = np.zeros(n)

    # Resolve Ly = b
    for i in range(n):
        y[i] = vector_b[i] - np.dot(matrix_L[i, :i], y[:i])

    # Resolve Ux = y
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(matrix_U[i, i+1:], x[i+1:])) / matrix_U[i, i]
        
    return x[::-1]


def polyfit_discrete(list_x, list_y, degree):
    # Converte listas para arrays Numpy
    list_x = np.array(list_x)
    list_y = np.array(list_y)
    
    n = len(list_x)
    
    # Cria a matriz de Vandermonde
    matrix_u = np.vander(list_x, degree+1, increasing=True)

    matrix_A = []
    # Calcula os produtos internos para preencher a matriz A
    for i in range(degree+1):
        matrix_A.append(np.dot(matrix_u[:, i], matrix_u[:, range(degree+1)]))

    matrix_A = np.asfarray(matrix_A, np.float64)
    
    # Calcula o produto interno para obter o vetor b
    vector_b = np.asfarray(np.dot(list_y, matrix_u[:, range(degree+1)]), np.float64)
    
    # Resolve o sistema de equações lineares usando a fatorização LU
    coeffs = lu_solve(matrix_A, vector_b)
    
    # Calcula o coeficiente de determinação
    y_mean = np.mean(list_y)
    y_pred = np.polyval(coeffs, list_x)
    s_tot = np.sum((list_y - y_mean) ** 2)
    s_res = np.sum((list_y - y_pred) ** 2)
    r2 = 1 - (s_res / s_tot)
    
    # Calcula o desvio padrão (se houver mais de 2 pontos)
    std_dev = sp.sqrt(s_res / (n-degree-1)) if n-degree-1 > 0 else 0
    
    # Calcula o erro padrão da estimativa (se houver mais de 2 pontos)
    std_err = sp.sqrt(s_res / (n-degree-2)) if n-degree-2 > 0 else 0
    
    # Cria um polinomio utilizando os coeficientes gerados anteriormente
    poly = sp.N(sp.Poly.from_list(coeffs, sp.symbols('x')).as_expr(), 7)
    
    return poly, round(std_dev, 3), round(std_err, 3), round(r2, 3)


def run():
    FILE_NAME = 'discrete_input.txt'
    list_x, list_y, n = read_file(FILE_NAME)
    
    if list_x is not None:
        poly = polyfit_discrete(list_x, list_y, n)
        save_results('output.txt', f'polyfit_discrete: {poly}')
    
# Chama a função principal
if __name__ == '__main__':
    run()