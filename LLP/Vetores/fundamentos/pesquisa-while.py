nomes = ["Deyverson", "Caça Rato", "Neymar", "Dorival", "Bolsonaro", "Gabigol"]
tamanho = len(nomes)
nome = (input("Digite o Nome que você deseja pesquisar: "))
i = 0
existe = False
index = 0
while i < tamanho:
    if (nome.lower() == nomes[i].lower()):
        existe = True
        index = i + 1
        break
    i += 1
if existe == False:
    print("O nome que você digitou não se encontra na lista.")
else:
    print("O nome que você digitou se encontra na posição:", index, "da lista")