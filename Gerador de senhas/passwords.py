import string
import random


def pass_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


for i in range(10):
    senha = pass_generator()
    print(f'Senha {i+1}: ', senha)
