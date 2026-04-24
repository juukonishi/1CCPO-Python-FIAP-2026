#Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.

def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

NotaA = float(input("Digite a primeira nota: "))
NotaA = verificar_nota(NotaA)

NotaB = float(input("Digite a segunda nota: "))
NotaB = verificar_nota(NotaB)

media = (NotaA + NotaB) / 2
print(media)