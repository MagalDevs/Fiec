produtos = [1.99 , 2.99 ,5.99, 100.99]
tamanho = len(produtos)
ValorTotal = 0
for n in range(0,  tamanho):
    ValorTotal += produtos[n]
print(ValorTotal)
n = 0
ValorTotal = 0
while (n < tamanho):
    ValorTotal += produtos[n]
    n += 1
print(ValorTotal)
ValorSum = sum(produtos)