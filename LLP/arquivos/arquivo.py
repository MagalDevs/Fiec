'''
try:
    arquivo = open("C:/Users/37046/Documents/Text.txt", "w", encoding='UTF-8') #escreve no arquivo, se o arquivo não existe ele cria
    arquivo.write("aula1\n")
    arquivo.write("aula2\n")
    arquivo.write("aula3\n")
    arquivo.write("aula4\n")
    arquivo.write("aula5\n")
    print("Arquivo criado com sucesso!")
    arquivo.close()
except Exception:
    print("Erro ao criar o arquivo!")
'''
""" 
try:
    arquivo = open("C:/Users/37046/Documents/Text.txt", "a", encoding='UTF-8') #append, adiciona ao arquivo já criado
    arquivo.write("gabigol1\n")
    arquivo.write("gabigol2\n")
    arquivo.write("gabigol3\n")
    arquivo.write("gabigol4\n")
    arquivo.write("gabigol5\n")
    print("Arquivo criado com sucesso!")
    arquivo.close()
except Exception:
    print("Erro ao criar o arquivo!")
"""

try:
    arquivo = open("C:/Users/37046/Documents/Text.txt", "r", encoding='UTF-8')
    linha = arquivo.readline()
    while linha != "":
        print(linha)
        linha = arquivo.readline()
    print("Arquivo lido com sucesso!")
    arquivo.close()
except Exception:
    print("Erro ao ler o arquivo!")