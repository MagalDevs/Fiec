try:
    x = int(input("Digite o valor do primeiro número da divisão: "))
    y = int(input("Digite o valor do segundo número da divisão: "))
    print(x / y)
except ZeroDivisionError:
    print("Não é possível dividir por 0!")