Inicio⬇️
horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor ganho por hora: "))
perctd = float(input("Digite o percentual de desconto (apenas números): "))
dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas * valor
valor_desconto = salario_bruto * (perctd / 100)
salario_liquido_inicial = salario_bruto - valor_desconto
acrescimo_dependentes = dependentes * 100

salario_final = salario_liquido_inicial + acrescimo_dependentes

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Salário Líquido (após desconto): R$ {salario_liquido_inicial:.2f}")
print(f"Bônus por Dependentes: R$ {acrescimo_dependentes:.2f}")
print(f">>Salário a Receber: R$ {salario_final:.2f}<<")
Fim⬆️
