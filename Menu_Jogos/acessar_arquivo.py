import random

arquivo = open('lista_palavras_2.txt','w', encoding='UTF-8')
arquivo.write('teste\n')
arquivo.close

arquivo = open('lista_palavras_2.txt','a', encoding='UTF-8')
arquivo.write('aleatório\n')
arquivo.close

