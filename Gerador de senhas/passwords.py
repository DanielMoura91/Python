import string
import random

def pass_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

n = int(input('Quantas senhas seguras vc precisa? '))

for i in range(n):  
    print(f'Senha {i+1}: ', pass_generator())
