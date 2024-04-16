"""
* Fabián Avilés
* Cristian Rico
* Actividad 4.2: Método Lineal Congruencial y Pruebas de Aleatoriedad
"""

def lcm(X0, a, c, m, n):
    numbers = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % m
        numbers.append(X / m)
    print(numbers)
    return numbers

# def chi():

# def runs():


if __name__ == '__main__':
    X0 = 6
    a = 32
    c = 3
    m = 80
    n = 10

    lcm(X0, a, c, m, n)
