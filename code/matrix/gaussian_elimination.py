from __tools import *


def gaussian_elimination(matrix_A, vector_b):

    if determinant(matrix_A) == None:
        return None

    n = len(matrix_A)
    vector_x = np.zeros(n)

    for i in range(n-1):
        max_index = i + np.argmax(abs(matrix_A[i:, i]))

        matrix_A[[i, max_index]] = matrix_A[[max_index, i]]
        vector_b[[i, max_index]] = vector_b[[max_index, i]]

        for j in range(i+1, n):
            mult = matrix_A[j, i] / matrix_A[i, i]
            matrix_A[j, i:] -= mult * matrix_A[i, i:]
            vector_b[j] -= mult * vector_b[i]

    for i in range(n-1, -1, -1):
        vector_x[i] = np.dot(matrix_A[i, i + 1:], vector_x[i + 1:])
        vector_x[i] = (vector_b[i] - vector_x[i]) / matrix_A[i, i]

    return vector_x


def run():
    results = []
    mx_A, mx_b = read_system('input.txt')[:2]
    
    results.append({'name': 'gaussian_elimination', 'result': gaussian_elimination(mx_A, mx_b)})
    save_results('output.txt', results)


# Chama a função principal
if __name__ == '__main__':
    run()
    
