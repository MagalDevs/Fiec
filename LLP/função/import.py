from random import *
caracteres = "1234567890!@#$%¨&*()abcdeABCDE"
senha = ""

for i in range(0,10):
    senha += choice(caracteres)

print(senha)
