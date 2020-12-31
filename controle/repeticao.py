#!python3

# imprime valores de 0 a 9
for i in range(10):
    print(i)

# imprime valores de 1 a 10
for i in range(1, 11):
    print(i)

# imprime valores de 2 a 100, pulando de 2 em 2
for i in range(2, 101, 2):
    print(i)

for i in range(99, 1, -2):
    print(i)

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=',')
