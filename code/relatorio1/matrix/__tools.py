import numpy as np
import sympy as sp
import os


def check_matrix(matrix) -> bool:
    rank = np.linalg.matrix_rank(matrix)
    if rank == matrix.shape[0]:
        return True
    else:
        return False


def determinant(matrix) -> int | None:
    if not check_matrix(matrix):
        return None
    else:
        return np.linalg.det(matrix)


def read_system(file_name: str) -> tuple[np.ndarray, np.ndarray, float, float]:
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        system = [eq.strip() for eq in f.readlines()]

    exprs, consts = [], []
    for i in range(len(system)-2):
        try:
            exprs.append(sp.parse_expr(system[i].strip().split('=')[0]))
            consts.append(sp.parse_expr(system[i].strip().split('=')[1]))
        except IndexError:
            consts.append(sp.parse_expr(system[i]).as_coefficients_dict()[1] * -1)
            exprs[i] = sp.parse_expr(system[i]) - (consts[i] * -1)
        except SyntaxError:
            print('> ERROR: Sintax incorreta no arquivo de entrada.')
            exit(-1)
    
    MAX_ITER = int(system.pop())
    TOL = float(system.pop())
    
    vector_x = list(set().union(*[eq.free_symbols for eq in exprs]))
    vector_x = sorted(vector_x, key=lambda symbol: str(symbol))

    matrix_A = np.array([[eq.coeff(var) for var in vector_x] for eq in exprs], dtype=np.float64)
    vector_b = np.array(consts, dtype=np.float64)

    return matrix_A, vector_b, TOL, MAX_ITER

def save_results(file_name: str, results: list):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        for dict in results:
            f.write(f'{dict["name"]}={dict["result"]}\n')

def pivoting(n: int, coef_mx, const_mx):
    for i in range(n-1):
        # Encontra o índice da linha com o maior valor absoluto na coluna abaixo do pivô atual
        max_index = i + np.argmax(abs(coef_mx[i:, i]))

        # Troca a linha atual com a linha do valor máximo
        coef_mx[[i, max_index]] = coef_mx[[max_index, i]]
        const_mx[[i, max_index]] = const_mx[[max_index, i]]
