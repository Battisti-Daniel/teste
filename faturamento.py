import random
import pandas as pd

faturamento = [random.randint(1000, 10000) for _ in range(30)]

'''
min

min_value = faturamento [0]
for i in range(1, len(faturamento)):
    if faturamento[i] < min_value:
        min_value = faturamento[i]

max

max_value = faturamento [0]
for i in range(1, len(faturamento)):
    if faturamento[i] > max_value:
        max_value = faturamento[i]

'''

print(min(faturamento))
print(max(faturamento))

media = sum(faturamento) // len(faturamento)

print(f'Faturamento supeiror a {media}')
for i in range(len(faturamento)):
    if faturamento[i] > media:
        print(f'No dia {i} um total de {faturamento[i]}')
