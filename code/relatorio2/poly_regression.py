from __tools import *


""" def polyfit_discrete(x, y, N):
    # Converte listas para arrays Numpy
    y = np.array(y)
    matrix_u = np.vander(x, N+1, increasing=True)

    matrix_A = []
    for i in range(N+1):
        matrix_A.append(np.dot(matrix_u[:, i], matrix_u[:, range(N+1)]))

    matrix_A = np.asfarray(matrix_A, np.float64)
    vector_b = np.asfarray(np.dot(y, matrix_u[:, range(N+1)]), np.float64)
    
    coeffs = np.linalg.solve(matrix_A, vector_b)
    return tuple(coeffs) """
    

def polyfit_discrete(x, y, n):
    # Ajusta um polinômio de ordem n aos pontos de dados
    coeffs = np.polyfit(x, y, n)
    
    return coeffs


def polyfit_continuous(expr, a, b, n):
    # Gera pontos de amostra igualmente espaçados
    x = np.linspace(a, b, 10000)
    y = eval(expr, {'x': x})

    # Ajusta um polinômio de ordem n aos pontos de amostra
    coeffs = np.polyfit(x, y, n)

    # Retorna os
    return coeffs


def run():
    FILE_NAME = 'output.txt'
    try:
        x, y, n = read_intervals('input.txt')
        coeffs = polyfit_discrete(x, y, n)
        save_results(FILE_NAME, f'polyfit_discrete: {coeffs}')
    except:
        expr, a, b, n = read_file_expr('input.txt')
        coeffs = polyfit_continuous(expr, a, b, n)
        save_results(FILE_NAME, f'polyfit_continuous: {coeffs:.6}')
    
    
# Chama a função principal
if __name__ == '__main__':
    run()