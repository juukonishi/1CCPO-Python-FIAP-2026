from sklearn.decomposition import non_negative_factorization

print('ola mundo')

print(7+4)
print('7+4')
print('7'+'4') #CONCATENAÇÃO DE STRINGS

#Comentário e uma linha
'''COMENTÁRIOS
DE MÚLTIPLAS
LINHAS'''

#VARIÁVEIS
nome = 'Julia' #tipo de dado str
idade = 19 #tipo de dado int
peso = 70.2 #tipo de dado float

print(nome, idade, peso)
print(f'oii {nome}!!!')

#INPUT - SIMULAÇÃO DE FORMULARIOS NO CMD
nome = input('Digite o seu nome: ')
idade = int(input('Digite a idade: '))
peso = float(input('Digite o peso: '))

print(nome, idade, peso)
print(idade+1)

ano_nascimento = 2006
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'Sua idade é: {idade}')