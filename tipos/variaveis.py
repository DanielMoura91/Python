#!python3

a = 3
b = 4.4

print(a + b)

texto = 'Sua idade é '
idade = 29

print(texto + str(idade))
print(f'{texto}{idade}')

dayofweek = ['domingo', 'segunda', 'terça',
             'quarta', 'quinta', 'sexta', 'sábado']
print(f'{dayofweek}')

"""
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
     print(a, end=',')
     a, b = b, a+b
"""

a, b = 0, 1

fibonacci = []

while a < 100:    
    fibonacci.append(a)
    a = b 
    b = a+b    

print('A sequencia de fibonacci é: ', fibonacci)
