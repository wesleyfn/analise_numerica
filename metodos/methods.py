from _tools import *

# Implementa o método da bisseção para encontrar uma raiz
# da função f(x) dentro do intervalo [lower_end, upper_end]


def bissection(lower_end: float, upper_end: float,
               tolerance: float, max_iterations: int = 100) -> float:
    estimate = (lower_end + upper_end) / 2
    prev_estimate, i = 0, 0

    # Executa o método da bisseção até encontrar uma raiz ou atingir o número máximo de iterações
    while True:
        prev_estimate = estimate

        # Verifica se o número máximo de iterações foi atingido
        if i >= max_iterations:
            print(f'> Número máximo de iterações ({max_iterations}) atingido!')
            break

        print(f'i = {i},  a = {lower_end:.6f}, b = {upper_end:.6f}, c = {estimate:.6f}')

        # Calcula o produto f(lower_end) * f(estimate) para
        # verificar se estimate é a raiz ou se está no intervalo correto
        f_sign_product = fx_value(lower_end) * fx_value(estimate)

        # Se estimate é a raiz, retorna seu valor
        if sp.ask(sp.Q.zero(f_sign_product)):
            return estimate

        # Se estimate não é a raiz, atualiza o intervalo [lower_end, upper_end]
        # e estimate de acordo com o sinal de f_sign_product
        if sp.ask(sp.Q.negative(f_sign_product)):
            upper_end = estimate
        else:
            lower_end = estimate

        estimate = (lower_end + upper_end) / 2

        # Calcula o erro relativo e verifica se é menor ou igual à tolerância desejada
        relative_error = abs((estimate - prev_estimate) / estimate)
        if relative_error <= tolerance:
            return estimate

        i += 1

# Implementa o método da posição falsa para encontrar uma
# raiz da função f(x) dentro do intervalo [lower_end, upper_end]


def false_position(lower_end: float, upper_end: float,
                   tolerance: float, max_iterations: int = 100) -> float:

    f_lower_end, f_upper_end = fx_value(lower_end), fx_value(upper_end)
    estimate = (lower_end * f_upper_end - upper_end *
                f_lower_end) / (f_upper_end - f_lower_end)
    prev_estimate = 0
    i = 0

    # Executa o método da posição falsa até encontrar uma raiz ou atingir o número máximo de iterações
    while True:
        prev_estimate = estimate

        # Verifica se o número máximo de iterações foi atingido
        if i >= max_iterations:
            print(f'> Número máximo de iterações ({max_iterations}) atingido!')
            break

        print(
            f'i = {i},  a = {lower_end:.6f}, b = {upper_end:.6f}, c = {estimate:.6f}')

        # Calcula o produto f(lower_end) * f(estimate) para verificar se estimate é a raiz ou se está no intervalo correto
        f_sign_product = fx_value(lower_end) * fx_value(estimate)

        # Se estimate é a raiz, retorna seu valor
        if sp.ask(sp.Q.zero(f_sign_product)):
            return estimate

        # Se estimate não é a raiz, atualiza o intervalo [lower_end, upper_end] e estimate de acordo com o sinal de f_sign_product
        if sp.ask(sp.Q.negative(f_sign_product)):
            upper_end = estimate
        else:
            lower_end = estimate

        f_lower_end = fx_value(lower_end)
        f_upper_end = fx_value(upper_end)

        # Calcula o novo valor de estimate
        estimate = (lower_end * f_upper_end - upper_end *
                    f_lower_end) / (f_upper_end - f_lower_end)

        # Calcula o erro relativo e verifica se é menor ou igual à tolerância desejada
        if abs((estimate - prev_estimate) / estimate) <= tolerance:
            return estimate

        i += 1

# Implementa o método de Newton-Raphson para
# encontrar uma raiz da função f(x) a partir do ponto x0


def newton_raphson(x0: float, tolerance: float, max_iterations: int = 100) -> float:
    x = x0
    i = 0

    # Loop para calcular as iterações
    for i in range(max_iterations):

        # Armazena o valor atual de x para uso posterior
        prev_x = x

        # Calcula o valor de f(x) e f'(x) para o valor atual de x
        fx = fx_value(prev_x)
        diff = diff_value(prev_x)

        print(f'x{i} = {x}, f(x) = {fx:.6f}, f\'(x) = {diff:.6f}')

        try:
            # Calcula o novo valor de x usando a fórmula do método de Newton-Raphson
            x = prev_x - (fx / diff)

            # Calcula o erro relativo
            error = abs((x - prev_x) / x)

            # Se o erro for menor ou igual à tolerância, termina o loop
            if error <= tolerance:
                break

        # Se a derivada for igual a zero, a fórmula do método de Newton-Raphson não pode ser usada
        except TypeError:
            print(f'> WARNING: The derivative of f(x) is 0!')

            # Adiciona uma pequena quantidade a f'(x) para contornar o problema de derivada zero
            x = prev_x - (fx / (diff + 1e-8))

            # Calcula o erro relativo com base no novo valor de x
            error = abs((x - prev_x) / x)

            # Se o erro for menor ou igual à tolerância, termina
            if error < tolerance:
                break

    # Retorna o valor atual de x
    return x

# Implementa o método da secante para encontrar
# uma raiz da função f(x) a partir dos pontos x0 e x1


def secant(x0: float, x1: float, tolerance: float, max_interations: float = 100) -> float:

    # Executa o loop com o número máximo de iterações fornecido como parâmetro
    for i in range(max_interations):

        # Calcula os valores de f(x) nos pontos x0 e x1
        fx0, fx1 = fx_value(x0), fx_value(x1)

        # Calcula o valor de x2 de acordo com o método da secante
        x2 = (fx1 * x0 - fx0 * x1) / (fx1 - fx0)

        print(f'k = {i}, x0 = {x0}, x1 = {x1}, x2 = {x2}')

        # Calcula o erro relativo
        error = abs((x2 - x1) / x2)

        # Verifica se o erro é menor que a tolerância fornecida como parâmetro
        if error < tolerance:
            break

        # Atualiza os valores de x0 e x1 para a próxima iteração
        x0, x1 = x1, x2

    # Retorna o valor atual de x1
    return x1
