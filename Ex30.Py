from datetime import date

dia_nascimento = int(input("Digite o dia de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
atual = date(ano_atual, mes_atual, dia_atual)

anos = ano_atual - ano_nascimento
meses = mes_atual - mes_nascimento
dias = dia_atual - dia_nascimento

if dias < 0:
    meses = meses - 1

    if mes_atual == 1:
        mes_anterior = 12
        ano_mes_anterior = ano_atual - 1
    else:
        mes_anterior = mes_atual - 1
        ano_mes_anterior = ano_atual

    ultimo_dia = (date(ano_mes_anterior, mes_anterior + 1, 1)
                  if mes_anterior < 12
                  else date(ano_mes_anterior + 1, 1, 1))

    primeiro_dia = date(ano_mes_anterior, mes_anterior, 1)

    dias_no_mes = (ultimo_dia - primeiro_dia).days

    dias = dias + dias_no_mes

if meses < 0:
    anos = anos - 1
    meses = meses + 12

print("Idade:", anos, "anos,", meses, "meses e", dias, "dias.")
