import random

file = open('input.in', 'w')

n = 1000000
for i in range(n):
    file.write(str(random.randint(-10000, 10000)) + '\n')