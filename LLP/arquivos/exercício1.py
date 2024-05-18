def criarArquivo():
    try:
        arquivo = open("C:/Users/37046/documents/relatorio_temperaturas.txt", "w", encoding='UTF-8')
        return arquivo
    except FileNotFoundError:
        print("Falha na criação do arquivo! por favor tente novamente mais tarde...")
    except:
        print("Deu ruim.")
def processarTemperaturas(arquivo):
    try:
        temp = (input("Digite o valor da temperatura em ºC: "))
        if (temp == ""):
            arquivo.write("Nenhuma temperatura indicada!")
        else:
            temp = float(temp)
            arquivo.write("Lista de temperatura indicadas:\n")
            arquivo.write(str(temp))
            arquivo.write("ºC\n")
            menorTemperatura = temp
            maiorTemperatura = temp
            soma = temp
            quantidade = 1
            media = temp
            while True:
                temp = (input("Digite o valor da temperatura em ºC: "))
                if(temp == ""):
                    break
                else:
                    temp = float(temp)
                    arquivo.write(str(temp))
                    arquivo.write("ºC\n")
                    if (temp < menorTemperatura):
                        menorTemperatura = temp
                    if (temp > maiorTemperatura):
                        maiorTemperatura = temp
                    soma += temp
                    quantidade += 1
            media = soma / quantidade
            arquivo.write("A menor temperatura indicada foi: ")
            arquivo.write(str(menorTemperatura))
            arquivo.write("ºC\n")
            arquivo.write("A maior temperatura indicada foi: ")
            arquivo.write(str(maiorTemperatura))
            arquivo.write("ºC\n")
            arquivo.write("A média das temperaturas indicadas foi: ")
            arquivo.write(str(media))
            arquivo.write("ºC\n")
        return arquivo
    except ValueError:
        print("Valor de entrada inválido! Por favor rode novamente o programa!")
    except FileNotFoundError:
        print("Falha no processamento do arquivo! por favor tente novamente mais tarde...")
    except:
        print("Deu ruim.")
    
        
print("Programa de registros de temperatura! entre com a temperatura co valores referentes a graus celsius, e para encerrar entre com um valor vazio, apenas clicando ENTER!")

arquivo = criarArquivo()
processarTemperaturas(arquivo)
arquivo.close()
print("Programa executado com sucesso! Por favor verificar o relatório criado: relatorio_temperaturas.txt")