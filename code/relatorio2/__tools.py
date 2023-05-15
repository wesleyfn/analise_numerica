import numpy as np
import sympy as sp


def lu_factorization(matrix_A):
    if sp.det(matrix_A) == 0:
        raise Exception('> Derivada resultou em 0')
    
    n = len(matrix_A)
    matrix_L = np.eye(n)
    matrix_U = np.zeros((n,n))
    
    for k in range(n):
        max_idx = k + np.argmax(np.abs(matrix_A[k:, k]))
        matrix_A[[k, max_idx]] = matrix_A[[max_idx, k]]
        matrix_U[k, k] = matrix_A[k, k] - np.dot(matrix_L[k, :k], matrix_U[:k, k])
        
        for i in range(k+1, n):
            matrix_L[i, k] = (matrix_A[i, k] - np.dot(matrix_L[i, :k], matrix_U[:k, k])) / matrix_U[k, k]
        for j in range(k+1, n):
            matrix_U[k, j] = matrix_A[k, j] - np.dot(matrix_L[k, :k], matrix_U[:k, j])
    
    return matrix_L, matrix_U


def lu_solve(matrix_A, vector_b):
    matrix_L, matrix_U = lu_factorization(matrix_A)
    
    n = len(matrix_A)
    y = x = np.zeros(n)

    for i in range(n):
        y[i] = vector_b[i] - np.dot(matrix_L[i, :i], y[:i])

    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(matrix_U[i, i+1:], x[i+1:])) / matrix_U[i, i]

    return x


