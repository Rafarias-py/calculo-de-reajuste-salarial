# Pegando as informações iniciais
salario = float(input("Salario: "))
falta = int(input("faltas: "))

# Validação de salário Negativo
if salario < 0:
    print("digite um valor positivo")

# Faixas baseadas em múltiplos de R$ 1302.00 (salário-mínimo)
else:
    if salario <= 2604:
        reajuste = 0.0645

    elif salario <= 6525:
        reajuste = 0.0455

    elif salario <= 13204:
        reajuste = 0.0289

    else:
        reajuste = 00

    salario_reajustado = salario + (salario * reajuste)
    
    # Regra de faltas e bônus
    if falta < 0:
        falta = 0
    elif falta == 0:
        bonus = 1302
    elif falta == 1:
        bonus = 500
    else:
        bonus = 0 

    ganho_total = salario_reajustado + bonus


    # Exibição do relatório formatado[cite: 2]
    print(f"Salário..............: R$ {salario:.2f}")
    print(f"Salário Reajustado...: R$ {salario_reajustado:.2f}")
    print(f"Bônus................: R$ {bonus:.2f}")
    print(f"Ganho total..........: R$ {ganho_total:.2f}")    