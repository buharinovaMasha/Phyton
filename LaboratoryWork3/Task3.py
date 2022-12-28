from pyDatalog import pyDatalog
import random


"""
Задание 3
Посчитать произведение случайных чисел от 1 до 100
"""


pyDatalog.create_terms('randomMultiplication, N')

randomMultiplication[N] = random.randint(0,100) * randomMultiplication[N-1]
randomMultiplication[1] = random.randint(0,100)

print(randomMultiplication[100]==N)


