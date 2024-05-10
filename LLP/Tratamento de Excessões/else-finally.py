try:
    x = int(input("Digite o valor do primeiro número da divisão: "))
    y = int(input("Digite o valor do segundo número da divisão: "))
    resultado = (x / y)
except ZeroDivisionError:
    print("Não é possível dividir por 0!")
except ValueError:
    print("Entrada de dados inválida!")
except Exception:
    print("Erro não identificado.")
finally: #sempre executável#
    print("Fim do programa!")