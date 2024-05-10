try:
    x = int(input("Digite o valor do primeiro número da divisão:"))
    y = int(input("Digite o valor do segundo número da divisão:"))

    if (y == 0):
        raise ZeroDivisionError("Não é possível dividir um número por 0! Por favor execute novamente o programa passando o segundo número diferente de 0.")
    else:
        resultado = x / y
except ValueError:    
    print("Entrada de dados inválida! Por favor digitar apenas números inteiros.")
#except Exception:
    #print("Erro não identificado! Tente rodar o programa novamente.")
else:
    print(resultado)
finally:
    print("Fim do programa!")