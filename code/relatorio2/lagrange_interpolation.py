from __tools import *
import sympy as sp


def lagrange_interpolation(x: list, y: list) -> list:
    # Converte para numpy array se necessário
    y = np.array(y)
    x = np.array(x)

    n = len(x)
    polynomials = []
    x_sp = sp.symbols('x')
    
    for i in range(n):
        # Calcula o polinômio de Lagrange correspondente ao i-ésimo ponto
        numerator = np.prod(x_sp - x[np.arange(n) != i])
        denominator = np.prod(x[i] - x[np.arange(n) != i])
        
        # Multiplica o polinômio de Lagrange pelo valor y correspondente 
                     
        polynomials.append((numerator / denominator) * y[i])
        
    print(polynomials) 
    # Soma os termos do polinômio interpolado
    interpolator = sum(polynomials)

    # Obtém os coeficientes do polinômio interpolado
    coeffs = sp.Poly(interpolator).all_coeffs()

    return coeffs

def run():
    x, y, _ = read_file('input.txt')
    coeffs = lagrange_interpolation(x, y)
    save_results('output.txt', f'lagrange_interpolation: {coeffs}')

# Chama a função principal
if __name__ == '__main__':
    run()