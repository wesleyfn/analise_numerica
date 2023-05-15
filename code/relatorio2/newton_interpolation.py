from __tools import *
import sympy as sp


def newton_interpolation(x, y):
    # Converte para numpy array se necessário
    y = np.array(y)
    x = np.array(x)

    x_sp = sp.symbols('x')
    n = len(x)
    a = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1]) / float(x[i] - x[i-j])
    
    # Multiplica cada coeficiente pelo produto dos termos (x - x_i) até o i-ésimo termo
    polynomial = sum(a[i] * np.prod([(x_sp - x[j]) for j in range(i)]) for i in range(n))

    return sp.Poly(polynomial).all_coeffs()


def run():
    x, y, _ = read_file('input.txt')
    coeffs = newton_interpolation(x, y)
    save_results('output.txt', f'newton_interpolation: {coeffs}')

# Chama a função principal
if __name__ == '__main__':
    run()