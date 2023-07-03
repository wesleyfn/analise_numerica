import matplotlib.pyplot as plt
import sympy as sp

from numpy import arange

from euler import euler_method
from euler_modified import euler_modified
from huen import huen
from ralston import ralston
from runge_kutta import runge_kutta


def show_plot(title):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'f(x) = {title}')
    plt.legend()
    plt.grid(True)
    plt.show()

def analytic_method(func):
    x = sp.symbols('x')
    expr = sp.sympify(func)
    
    list_x = arange(0.0, 4.1, 0.1)
    list_y = []

    for x_val in list_x:
        y_val = sp.integrate(expr, x).subs({'x': x_val}) + 1
        list_y.append(y_val)

    return list_x, list_y
    
    
def run():
    FUNCTION = '-2*x**3 + 12*x**2 - 20*x + 8.5'
    
    list_x, list_y = euler_method.run()
    plt.plot(list_x, list_y, 
             marker='o',
             #color='gray', 
             #ms = 10, 
             label='Euler')
    
    list_x, list_y = euler_modified.run()
    plt.plot(list_x, list_y, 
             marker='o', 
             #color='gray',
             #ms = 10,
             label='Euler Modified')
    
    list_x, list_y = huen.run()
    plt.plot(list_x, list_y, 
             marker='o', 
             #color='gray', 
             #ms = 8, 
             label='Huen')
    
    list_x, list_y = ralston.run()
    plt.plot(list_x, list_y, 
             marker='o', 
             #color='gray', 
             #ms = 8, 
             label='Ralston')
    
    list_x, list_y = runge_kutta.run()
    plt.plot(list_x, list_y, 
             marker='o', 
             #color='gray', 
             #ms = 8, 
             label='Runge-Kutta')
    
    list_x, list_y = analytic_method(FUNCTION)
    plt.plot(list_x, list_y, 
             color='red', 
             label='Analytic')
    
    show_plot(FUNCTION)

# Chama a função principal
if __name__ == '__main__':
    run()