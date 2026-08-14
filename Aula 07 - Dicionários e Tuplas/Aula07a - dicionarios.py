eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno', #one e two são as chaves
    'two': 'dos',
}

#CONTAGEM DE LETRAS
def count_letters(s):
    d = dict() #abre um dicionario vazio
    for c in s: #se a letra não é uma chave do dicionario
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1 #se a letra ja apareceu no laço, ela soma 1
    return d #retorna o dicionario

dict_contagem = count_letters('ovo')
print(dict_contagem)