import numpy as np
import math
import ctypes

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Funcao entrada de dados que recebe o parametro nome, o qual é um arquivo .txt que possui uma matriz com numeros binarios
# Para descobrir a dimensao, é usado o modo leitura, e usando o for, passamos o arquivo linha por linha para achar a sua qtd de linhas
# salva no nrows, que comeca em 0 e incrementa a cada linha nova encontrada, depois o arquivo é fechado
# logo depois o arquivo é aberto para criar nossa matriz numpy, com o numero maximo de linhas dado por nrows
# a dimensao sera dada pelo np.size que irá dar o tamanho total da matriz, para descobrirmos cada linha e nao o total linha X col, encontramos a raiz
# a raiz é encontrada pelo math.sqrt retornando um valor float para a variavel dimensao
# logo depois o programa vai para a funcao saidaDados
def entradaDados(nome):
    caminho = 'C:/Users/IGOR/Downloads/atv1grafos/' + nome + '.txt'
    arq = open(caminho,"r") 
    nrows = 0
    content = arq.read() 
    colist = content.split("\n") 
    for i in colist: 
        if i: 
            nrows += 1
    arq.close
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int32", max_rows=nrows)
    d = np.size(data)
    dimensao = math.sqrt(d)
    saidaDados(nome, dimensao)
    return data

# A funcao saida de dados vai receber o nome da instancia e sua dimensao
# a funcao comeca criando o arquivo resultado.txt, no modo de escrita w+, onde é criado o arquivo se ele nao existir 
# e é apagado seu conteudo se ele existir e tiver algo escrito nele
# logo depois escrevemos no arquivo, sendo que transformamos o float em int e depois em str
# a transformacao pra float é pro numero nao ter casas decimais (ex. 8.0)
# a transformacao para str é para escrever no arquivo e nao ocorrer problemas
# logo depois tambem printamos o resultado para o usuario na tela e fechamos o arquivo
def saidaDados(nome, dimensao):
    arq = open("C:/Users/IGOR/Downloads/atv1grafos/resultado.txt", "w+")
    arq.write("" +nome+ " = (" +str(int(dimensao))+ ", " +str(int(dimensao))+ ")")
    print(("" +nome+ " = (" +str(int(dimensao))+ ", " +str(int(dimensao))+ ")"))
    arq.close

# Press the green button in the gutter to run the script.
# a main ficou simples, com apenas a entrada do nome da instancia necessaria.
if __name__ == '__main__':
    nome = input("Insira o nome da instância:")
    data = entradaDados(nome)
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
