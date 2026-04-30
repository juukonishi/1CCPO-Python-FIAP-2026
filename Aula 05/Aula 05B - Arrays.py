from requests.utils import unquote_header_value

lista_frutas = ['laranja', 'uva', 'melão']

#lista_frutas[0] =  laranja
#lista_frutas[1] = uva
#lista_frutas[2] = melão

print(lista_frutas[1])

lista_frutas.append("maçã")
print(lista_frutas)
#lista_frutas[3] = maçã

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)