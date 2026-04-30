#Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis deuplas que podem ser formadas.
#Primeiro, crie um vetor e coloque quatro nomes nele. - João, Lucas, Jair, Luís
#A seguir, exiba as possíveis duplas.

nomes = ['João', 'Lucas', 'Jair', 'Luís']

for i in range(len(nomes)):
    for j in range (i+1, len(nomes)):
        print(nomes[i], nomes[j])

#i=linha; j=coluna



