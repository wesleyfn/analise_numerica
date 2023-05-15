from __tools import *


def linear_regression(x, y) -> tuple[np.float64]:
    # Converte listas para arrays Numpy
    x = np.array(x)
    y = np.array(y)
    
    # Atribui o numero de valores em n
    n = x.size

    # Cálculo dos coeficientes a1 e a0
    a1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
    a0 = np.mean(y) - a1 * np.mean(x)
    
    # Cálculo do coeficiente de determinacao
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    ss_res = np.sum((y - (a0 + a1 * x)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    
    # Retorna os coeficientes
    return round(a0, 7), round(a1, 7), {'R^2=': round(r2, 7), 'r=': round(np.sqrt(r2), 7)}


def run():
    FILE_NAME = 'output.txt'
    x_values, y_values, _ = read_file('input.txt')
    coeffs = linear_regression(x_values, y_values)
    
    save_results(FILE_NAME, f'linear_regression: {coeffs}')

# Chama a função principal
if __name__ == '__main__':
    run()