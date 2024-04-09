"""
* Cristian Leilael Rico Espinosa
* Actividad 4.1
* El programa se hizo utilizando la versión 3.12.2 de Python
"""

import math
import matplotlib.pyplot as plt

file_path = '.\\Act_4_1\\data01.txt'
decimal = 4

count = 0
countf = 0
fcount = 0
bcount = 0

with open(file_path, 'r') as file:
    lines = file.readlines()
    data_array = [line.strip() for line in lines]
    # Convert elements in array to numbers
    num_array = [eval(i) for i in data_array]

file.close()

num_array.sort()

N = len(num_array)

print('Valor de N = ', N)

C = 1 + (3.3 * math.log10(N))

new_C = int(C) + 1

print('Valor de C = ', new_C)

minNum = round(min(num_array), decimal)
maxNum = round(max(num_array), decimal)

print('Minimo = ', minNum, '  Maximo = ', maxNum)

W = (maxNum - minNum) / new_C
W = round(W, decimal)

print('Valor de W = ', W)

intMax = round(minNum + W, decimal)
intMin = minNum

print('\n---------- INTERVALOS ----------\n')

for number in num_array:
    if number > intMin and number < intMax:
        count += 1
        if intMin + W > maxNum:
            countf += 1
        fcount += 1
    else:
        print('[', intMin, ' - ', intMax, ') -->', count)
        bcount += 1
        count = 0
        intMin = intMax
        intMax = round((intMin + W), decimal)

print('[', intMin, ' - ', intMax, ') -->', countf)

print('\nSuma de Frecuencias = ', fcount)

plt.hist(num_array, bins=(bcount + 1), edgecolor='black', rwidth=0.8)
plt.ylabel('Frecuencia')
plt.xlabel('Valores')
plt.show()