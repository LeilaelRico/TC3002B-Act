"""
* Fabián Avilés
* Cristian Rico
* Actividad 4.2: Método Lineal Congruencial y Pruebas de Aleatoriedad
"""

# ---------- Caso de Prueba 1 ----------
def lcm(X0, a, c, m, n):
    numbers = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % m
        numbers.append(X / m)
    print("The numbers obtained are:", numbers)
    return numbers

# ---------- Caso de prueba 2 ----------
def perform_chi_squared_test(data_file):
    intervals = [(i * 0.1, (i + 1) * 0.1) for i in range(10)]
    observed = [0] * 10
    for number in data_file:
        for i, interval in enumerate(intervals):
            if interval[0] <= number < interval[1]:
                observed[i] += 1
                break
    expected = [len(data_file) / 10] * 10
    print("Intervals\t\t\tObserved\tExpected\t(O - E)^2 / E")
    for i in range(10):
        O_minus_E_squared_over_E = (
            (observed[i] - expected[i]) ** 2) / expected[i]
        print(f"[{intervals[i][0]:.4f} - {intervals[i][1]:.4f})\t\t{observed[i]}\t\t{expected[i]:.4f}\t\t{O_minus_E_squared_over_E:.4f}")
    print("------------------------------------------------------")
    print(f"Suma: {sum(observed)}\t\tX2 = {sum(O_minus_E_squared_over_E for i in range(10)):.4f}")
    print("\nH0: Generated numbers are not different from the uniform distribution")
    print("H1: Generated numbers are different from the uniform distribution\n")
    print(chi(observed, expected))

def chi(observed, expected):
    chi_squared = sum(
        ((observed[i] - expected[i]) ** 2) / expected[i] for i in range(len(observed)))
    critical_value = 16.91 
    if chi_squared > critical_value:
        return "H0 is rejected"
    else:
        return "H0 is not rejected"

# ---------- Caso de Prueba 3 ----------
def calculate_streaks(sequence):
    signs = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            signs.append('+')
        elif sequence[i] < sequence[i-1]:
            signs.append('-')
        else:
            signs.append('=')
    return signs

def count_runs(signs):
    runs = 1
    for i in range(1, len(signs)):
        if signs[i] != signs[i-1]:
            runs += 1
    return runs

def calculate_statistics(signs, runs):
    miu = (2 * len(signs) - 1) / 3
    sigma = ((16 * len(signs) - 29) / 90) ** 0.5
    z_score = (runs - miu) / sigma
    return miu, sigma, z_score

def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(float(line.strip()))
    return data

def main():
    # Definición de variables para ejercicio 1
    X0 = 6
    a = 32
    c = 3
    m = 80
    n = 10

    # Carga de Archivo para ejecicio 2
    filenameEx2 = ".\\M4_Act_4_2\\chi_data.txt"
    dataEx2 = read_data_from_file(filenameEx2)

    # Carga de Archivo para ejecicio 3
    filename = ".\\M4_Act_4_2\\runs_data.txt"
    data = read_data_from_file(filename)

    # Llamada de Ejercicio 1
    print("\n1) Linear congruential method")
    lcm(X0, a, c, m, n)

    # Llamada Ejecicio 2
    print("\n2) Chi-squared test")
    perform_chi_squared_test(dataEx2)

    # Llamada Ejercicio 3
    print("\n3) Streak runs")

    signs = calculate_streaks(data)
    print("Generated signs:")
    print(' '.join(signs))

    total_signs = len(signs)
    total_runs = count_runs(signs)
    print("\ntotal signs:", total_signs)
    print("total runs:", total_runs)

    miu, sigma, z_score = calculate_statistics(signs, total_runs)
    print("\nStatistics")
    print("Miu =", round(miu, 4))
    print("Sigma =", round(sigma, 5))
    print("Zscore =", round(z_score, 6))

    print("\nH0: Appereance of the numbers is random")
    print("H1: Appereance of the numbers is not random")

    if abs(z_score) < 1.96:
        print("Since |{}| < |1.96|, H0 is not rejected".format(round(z_score, 2)))
    else:
        print("Since |{}| >= |1.96|, H0 is rejected".format(round(z_score, 2)))

if __name__ == '__main__':
    main()