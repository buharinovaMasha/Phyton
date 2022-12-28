from pyDatalog import pyDatalog
import random


"""
Задание 4
Посчитать медиану среди случайных чисел от 1 до 100
"""


pyDatalog.create_terms('randomMeanRow, rowSum, N')

rowSum[N] = random.randint(0,100) + rowSum[N-1]
rowSum[1] = random.randint(0,100)
randomMeanRow[N] = rowSum[N] / N

print(randomMeanRow[100]==N)


