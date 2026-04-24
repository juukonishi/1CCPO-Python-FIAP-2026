#você foi contratado para criar um sistema de RH que calcula o salário final de um funcionário com base em diversos fatores: cargo, horas extras, faltas, bonus e descontos.
#requisitos: o programa deve solicitar
#- nome do funcionário
#- cargo (1-gerente, 2-analista, 3-assistente, 4-estagiario)
#- salário base (float)
#- total de horas extras trabalhadas
#- total de faltas no mês
#- se recebeu bonus por desempenho (s ou n)
#regras de cálculo:
#- valor da hora extra: 1.5% do salário base por hora extra
#- desconto por falt: 2% do salário base por falta
#- bônus (se aplicável): gerente: R$ 1000; analista: R$ 500; assistente: R$ 300; estagiário: R$ 100
#o sistema deve:
#- calcular e mostrar: salário bruto; total de acréscimos (horas extrar + bônus); total de descontos (faltas); salário final
#regras de implementação:
#crie funções como:
#def calcular_horas_extras(salario_base, horas) :
#def calcular_descontos_faltas(salario_base, faltas) :
#def calcular_bonus(cargo, recebeu_bonus) :

def calcular_horas_extras(salario_base, horas):
    valor_hora_extras = salario_base * 0.015
    return valor_hora_extras * horas

def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas

def calcular_bonus (cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 's':
        return 0
    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    elif cargo == 4:
        return 100
    else:
        return 0

print("\n--- Sistema de RH ---")
nome = input("Nome do funcionário: ")

cargo = 0
while cargo <1 or cargo > 4:
    cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
    if cargo <1 or cargo > 4:
        print("Cargo invalido!")

salario_base = -1
while salario_base < 0:
    salario_base = float(input("Salário base: R$ "))
    if salario_base < 0:
        print('Salário base invalido!')

horas_extras = -1
while horas_extras < 0:
    horas_extras = float(input("Horas extras: "))
    if horas_extras < 0:
        print('Horas extras invalido!')

faltas = -1
while faltas < 0:
    faltas = float(input("Faltas no mês: "))
    if faltas < 0:
        print('Faltas invalido!')

recebeu_bonus = ''
while recebeu_bonus != 's' and recebeu_bonus != 'n':
    recebeu_bonus = (input("Recebeu bônus? (s/n): "))
    if recebeu_bonus != 's' and recebeu_bonus != 'n':
        print('Digite apenas s ou n!')

horas_valor = calcular_horas_extras(salario_base, horas_extras)
descontos = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base
acrescimos = horas_valor + bonus
salario_final = salario_bruto + acrescimos - descontos

print('\n--- Resultado ---')
print('Funcionário:', nome)
print('Salário Bruto: R$', salario_bruto)
print('Acréscimos: R$', acrescimos)
print('Descontos: R$', descontos)
print('Salário Final: R$', salario_final)
