import matplotlib.pyplot as plt
import sympy as sp

from numpy import linspace

from euler import euler_method
from euler_modified import euler_modified
from huen import huen
from ralston import ralston
from runge_kutta import runge_kutta


def show_plot():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Função: -2x³ + 12x² - 20x + 8.5')
    plt.legend()
    plt.grid(True)
    plt.show()


def analytic_method():
    x = sp.symbols('x')
    expr = -2*x**3 + 12*x**2 - 20*x + 8.5

    list_x = linspace(0.0, 4, 100)
    list_y = []

    for x_val in list_x:
        y_val = sp.integrate(expr, x).subs({'x': x_val}) + 1
        list_y.append(y_val)

    return list_x, list_y
    
def run():
    list_x, list_y = euler_method.run()
    plt.plot(list_x, list_y, 
             marker='p', 
             ms = 10, 
             label='Euler')
    
    list_x, list_y = euler_modified.run()
    plt.plot(list_x, list_y, 
             marker='*', 
             color='gray',
             ms = 10,
             label='Euler Modified')
    
    list_x, list_y = huen.run()
    plt.plot(list_x, list_y, 
             marker='D', 
             color='gray', 
             ms = 8, 
             label='Huen')
    
    list_x, list_y = ralston.run()
    plt.plot(list_x, list_y, 
             marker='v', 
             color='gray', 
             ms = 8, 
             label='Ralston')
    
    list_x, list_y = runge_kutta.run()
    plt.plot(list_x, list_y, 
             marker='s', 
             color='gray', 
             ms = 8, 
             label='Runge-Kutta')
    
    list_x, list_y = analytic_method()
    plt.plot(list_x, list_y, 
             color='red', 
             label='Analytic')
    
    show_plot()

# Chama a função principal
if __name__ == '__main__':
    run()