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


a, b = 0, 1

fibonacci = []

while a < 100:
    print(a, end=',')
    a, b = b, a+b
    fibonacci.append(a)

print('A sequencia de fibonacci é: ', fibonacci)
