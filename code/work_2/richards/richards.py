import os

# Funções para entrada e saída de dados
def read_file(file_name: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'r') as f:
        try:
            h1 = float(f.readline())
            h2 = float(f.readline())
            
        except (ValueError, TypeError):
            return None, 0.0

    return h1, h2

def save_results(file_name: str, result: str):
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(path_file, 'w') as f:
        f.write(result)


def richardson_extrapolation(h1, h2):
    result = (4/3)*h2 - (1/3)*h1
    
    return result

def run():
    FILE_NAME = 'richards_input.txt'
    h1, h2 = read_file(FILE_NAME)
    
    if h1 is not None:
        aprox = richardson_extrapolation(h1, h2)
        save_results('output.txt', f'richardson_extrapolation: {aprox}')

# Chama a função principal
if __name__ == '__main__':
    run()