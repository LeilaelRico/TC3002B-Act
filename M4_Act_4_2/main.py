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


def chi(observed, expected):
    chi_squared = sum(
        ((observed[i] - expected[i]) ** 2) / expected[i] for i in range(len(observed)))
    critical_value = 16.91  # for alpha = 0.05
    if chi_squared > critical_value:
        return "H0 is rejected"
    else:
        return "H0 is not rejected"

# Caso de prueba 2
def perform_chi_squared_test(data_file):
    with open(data_file, 'r') as file:
        data = [float(line.strip()) for line in file]
    intervals = [(i * 0.1, (i + 1) * 0.1) for i in range(10)]
    observed = [0] * 10
    for number in data:
        for i, interval in enumerate(intervals):
            if interval[0] <= number < interval[1]:
                observed[i] += 1
                break
    expected = [len(data) / 10] * 10
    print("Intervals\tObserved\tExpected\t(O - E)^2 / E")
    for i in range(10):
        O_minus_E_squared_over_E = (
            (observed[i] - expected[i]) ** 2) / expected[i]
        print(f"[{intervals[i][0]:.4f} - {intervals[i][1]:.4f})\t\t{observed[i]
                                                                    }\t\t{expected[i]:.4f}\t\t{O_minus_E_squared_over_E:.4f}")
    print("------------------------------------------------------")
    print(f"Suma: {sum(observed)}\t\tχ2 = {
          sum(O_minus_E_squared_over_E for i in range(10)):.4f}")
    print("\nH0: Generated numbers are not different from the uniform distribution")
    print("H1: Generated numbers are different from the uniform distribution\n")
    print(chi(observed, expected))

# def runs():


if __name__ == '__main__':
    X0 = 6
    a = 32
    c = 3
    m = 80
    n = 10

    print("\n1) Linear congruential method")
    lcm(X0, a, c, m, n)

    print("\n2) Chi-squared test")
    # Ejecutar la prueba de Chi-cuadrada con el archivo proporcionado
    perform_chi_squared_test(".\\M4_Act_4_2\\chi_data.txt")
