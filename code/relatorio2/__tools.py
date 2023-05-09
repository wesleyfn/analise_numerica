import os
import numpy as np


def read_intervals(file_name: str) -> tuple:
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            n = int(f.readline().strip())
            x_values, y_values = [], []
            for line in f.readlines():
                x_values += line.strip().split(',')[:1]
                y_values += line.strip().split(',')[1:]
                
            x_values = list(map(lambda x: np.float64(x), x_values))
            y_values = list(map(lambda x: np.float64(x), y_values))
            
        except ValueError and TypeError:
            return None

    return x_values, y_values, n


def read_file_expr(file_name: str) -> tuple:
    path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
    with open(path_file, 'r') as f:
        try:
            expr = f.readline().strip()
            a, b = f.readline().strip().split(',')
            n = f.readline().strip()

        except ValueError and TypeError:
            return None
    
    return expr, float(a), float(b), int(n)
            

def save_results(file_name: str, result: str):
    with open(file_name, 'a+') as f:
        f.truncate(0)
        f.write(result)