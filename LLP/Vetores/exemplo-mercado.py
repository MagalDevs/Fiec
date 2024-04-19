produtos = []
while True:
    ValorProduto = float(input("Digite o valor o produto ou 0 para finalizar: "))
    if (ValorProduto > 0):
        produtos.append(ValorProduto)
    else:
        break
print(produtos)
ValorTotal = 0
for i in range(0, len(produtos)):
    ValorTotal += produtos[i]
print("Valor total dos produtos:", ValorTotal)