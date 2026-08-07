endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]
def analise_endpoint(codigos):
    total = len(codigos)

    sucessos = sum(1 for codigo in codigos if 200 <= codigo <= 299)

    porcentagem = (sucessos / total) * 100

    erro_consecutivo = False

    for i in range(len(codigos) - 1):
        erro_atual = not (200 <= codigos[i] <= 299)
        proximo_erro = not (200 <= codigos[i + 1] <= 299)

        if erro_atual and proximo_erro:
            erro_consecutivo = True
            break

    if erro_consecutivo:
        classificacao = "CRÍTICO"
    elif porcentagem >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return porcentagem, classificacao, erro_consecutivo

endpoint_maior_erro = ""
maior_quantidade_erros = 0

for i in range(len(endpoints)):
    porcentagem, classificacao, critico = analise_endpoint(status[i])

    erros = sum(1 for codigo in status[i] if not (200 <= codigo <= 299))

    if erros > maior_quantidade_erros:
        maior_quantidade_erros = erros
        endpoint_maior_erro = endpoints[i]

    print(f"Endpoint: {endpoints[i]}")
    print(f"Taxa de sucesso: {porcentagem:.2f}%")
    print(f"Classificação: {classificacao}")
    print("-" * 30)

print(f"Endpoint com mais erros: {endpoint_maior_erro}")
print(f"Quantidade de erros: {maior_quantidade_erros}")
