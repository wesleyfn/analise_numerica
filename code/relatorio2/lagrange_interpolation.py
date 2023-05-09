from __tools import *

def lagrange_interpolation(x, y, x_interp):
    # Converte para numpy array se necessário
    x = np.array(x)
    y = np.array(y)
    x_interp = np.array(x_interp)

    # Verifica se x e y têm o mesmo tamanho
    if x.size != y.size:
        raise ValueError("x e y devem ter o mesmo tamanho.")

    # Verifica se x_interp tem tamanho maior que zero
    if x_interp.size == 0:
        raise ValueError("x_interp deve ter tamanho maior que zero.")

    # Calcula o número de pontos conhecidos
    n = x.size

    # Inicializa a matriz que armazenará os valores dos polinômios de Lagrange
    L = np.zeros((n, x_interp.size))

    # Calcula os polinômios de Lagrange
    for i in range(n):
        # Calcula o denominador da fórmula de Lagrange
        denominator = np.prod(x[i] - x[np.arange(n) != i])

        # Calcula o numerador da fórmula de Lagrange
        numerator = x_interp - x[np.arange(n) != i]
        numerator = np.prod(numerator, axis=0)

        # Armazena o resultado na matriz L
        L[i, :] = numerator / denominator

    # Calcula os valores interpolados correspondentes a x_interp
    y_interp = np.dot(y, L)

    return y_interp

def run():
    x, y = read_intervals('input.txt')
    a0, a1, a2 = lagrange_interpolation(x, y, 2)
    save_results('output.txt', f'poly_regression: P(x)={a0:.7} + {a1:.7}x + {a2:.7}x²')

# Chama a função principal
if __name__ == '__main__':
    run()