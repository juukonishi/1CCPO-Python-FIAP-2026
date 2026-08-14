endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],#cod_http de /login
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# print (endpoints[0])
# print (status[0])

#FUNÇÃO QUE VERIFICA SE UM CÓDIGO HTTP DA REQUISIÇÃO DE UM
#ENDPOINT É SUCESSO OU NÃO
# 200 --> TRUE
# 401 --> FALSE

def sucesso(codigo):
    return codigo >= 200 and codigo <= 299

#FUNÇÃO QUE VERIFICA DE TEM 2 ERROS SEGUIDOS NA
#LISTA DE REQUISIÇÕES DE UM ENDPOINT

def dois_erros_seguidos(lista_req):
    for i in range(len(lista_req) - 1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i + 1]

        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(lista_req):
    qtd_sucessos = 0

    for codigo in lista_req:
        if sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(lista_req)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucessos = qtd_sucessos / qtd_total_req * 100

    tem_erros_seguidos = dois_erros_seguidos(lista_req)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

#PERCORRER A MATRIZ STATUS
qtd_maior_erros = 0
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(reqs_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {reqs_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual de sucesso: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("-" * 30)

    if erros > qtd_maior_erros:
        qtd_maior_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint maior erro: {endpoint_maior_erro} ({qtd_maior_erros})")