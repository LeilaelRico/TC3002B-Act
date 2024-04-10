"""
* Cristian Leilael Rico Espinosa
* Actividad 4.1
* El programa se hizo utilizando la versión 3.12.2 de Python
"""

import math
import matplotlib.pyplot as plt
import numpy as np

file_path = '.\\Act_4_1\\data02.txt'
decimal = 2

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

# print(num_array)

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

while intMax <= maxNum:
    count_interval = sum(1 for num in num_array if intMin <= num < intMax)
    print('[', intMin, ' - ', intMax, ') -->', count_interval)
    bcount += 1
    intMin = intMax
    intMax = round(intMin + W, decimal)

if intMin < maxNum:
    count_interval = sum(1 for num in num_array if intMin <= num <= maxNum)
    print('[', intMin, ' - ', maxNum, ') -->', count_interval)

plt.hist(num_array, bins= (bcount + 1), edgecolor='black', rwidth=0.8)
plt.ylabel('Frecuencia')
plt.xlabel('Valores')
plt.show()