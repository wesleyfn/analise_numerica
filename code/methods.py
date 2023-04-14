from _tools import *

def bissection(x_a: float, x_b: float, tol: float, max_iter: int = 100) -> float:
    estimate = (x_a + x_b) / 2
    prev_estimate = 0

    for i in range(max_iter):
        prev_estimate = estimate

        #print(f'i = {i},  a = {x_a:.6f}, b = {x_b:.6f}, c = {estimate:.6f}')

        f_sign_product = fx_value(x_a) * fx_value(estimate)

        if sp.ask(sp.Q.zero(f_sign_product)):
            return estimate

        if sp.ask(sp.Q.negative(f_sign_product)):
            x_b = estimate
        else:
            x_a = estimate

        estimate = (x_a + x_b) / 2
        rel_error = abs((estimate - prev_estimate) / estimate)
        try:
            if rel_error < tol:
                return estimate
        except TypeError:
            return prev_estimate
        
    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return estimate


def false_position(x_a: float, x_b: float, tol: float, max_iter: int = 100) -> float:

    f_a, f_b = fx_value(x_a), fx_value(x_b)
    estimate = (x_a * f_b - x_b * f_a) / (f_b - f_a)
    prev_estimate = 0

    for i in range(max_iter):
        prev_estimate = estimate

        #print(f'i = {i},  a = {x_a:.6f}, b = {x_b:.6f}, c = {estimate:.6f}')

        f_sign_product = fx_value(x_a) * fx_value(estimate)
        if sp.ask(sp.Q.zero(f_sign_product)):
            return estimate

        if sp.ask(sp.Q.negative(f_sign_product)):
            x_b = estimate
        else:
            x_a = estimate

        f_a = fx_value(x_a)
        f_b = fx_value(x_b)

        estimate = (x_a * f_b - x_b * f_a) / (f_b - f_a)
        
        rel_error = abs((estimate - prev_estimate) / estimate)
        try:
            if rel_error < tol:
                return estimate
        except TypeError:
            return prev_estimate
     
    
    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return estimate


def newton_raphson(x0: float, tol: float, max_iter: int = 100) -> float:
    x = x0
    for i in range(max_iter):

        prev_x = x

        fx = fx_value(prev_x)
        diff = diff_value(prev_x)

        print(f'x{i} = {x}, f(x) = {fx:.6f}, f\'(x) = {diff:.6f}')

        try:
            x = prev_x - (fx / diff)

            rel_error = abs((x - prev_x) / x)
            if rel_error < tol or sp.ask(sp.Q.infinite(x)):
                return x

        except TypeError:
            print(f'> ERROR: A derivada de f(x) é 0.')

            x = prev_x - (fx / (1 + 1e-8 * diff))

            rel_error = abs((x - prev_x) / x)
            try:
                if rel_error < tol:
                    return x
            except TypeError:
                return prev_x

    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return x


def secant(x0: float, x1: float, tol: float, max_iter: float = 100) -> float:

    for i in range(max_iter):

        fx0, fx1 = fx_value(x0), fx_value(x1)

        x2 = (fx1 * x0 - fx0 * x1) / (fx1 - fx0)

        print(f'k = {i}, x0 = {x0}, x1 = {x1}, x2 = {x2}')

        rel_error = abs((x2 - x1) / x2)
        try:
            if rel_error < tol:
                return x2
        except TypeError:
            return x1

        x0, x1 = x1, x2

    print(f'> Número máximo de iterações ({max_iter}) atingido!')
    return x2
