meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
for n in range(0, 6):
    print(meses[n])
tamanho = len(meses)
#percorrer
meses[2] = 'Gustavo Mioto'
for n in range(0, 6):
    print(meses[n])
tamanho = len(meses)