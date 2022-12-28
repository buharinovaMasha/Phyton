from pyDatalog import pyDatalog


"""
Задание 1
Посчитать сумму ряда
"""


pyDatalog.create_terms('rowSum, N')

rowSum[N] = N + rowSum[N-1]
rowSum[1] = 1

print(rowSum[100]==N)


