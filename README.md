# 1-17-Python
17 Exercícios na linguagem python, requisitados pelo professor Colevati

1°:"⦁	Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado."

Inicio⬇️ 
lado = float(input("digite o valor desejado"))

area = (lado ** 2)

print(f"A área do quadrado com lado {lado} é: {area}")
Fim⬆️

2°:"⦁	Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%."

Inicio⬇️
salario = float(input("qual é o seu salário?"))

novo_salario = int(salario * 1.15 * 100) / 100

print(f"O novo salário é R$ {novo_salario}")
Fim⬆️

3°:"⦁	Receba a base e a altura de um triângulo. Calcule e mostre a sua área."

Inicio⬇️
base = float(input("defina a base"))

altura = float(input("defina a altura"))

area = int(base * altura / 2)

print(f"A area do triangulo é {area}")
Fim⬆️

4°:"⦁	Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5."

Inicio⬇️
celsius = float(input("insira temperatura desejada:"))

fahreinheit = int(9 * celsius + 160) / 5

print(f"A temperatura convertida em F é {fahreinheit}")
Fim⬆️

5°:"⦁	Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes)."

Inicio⬇️
a = float(input("digite a:"))
b = float(input("digite b:"))
c = float(input("digite c:"))

delta = int(b ** 2) - (4 * a * c)

raiz1 = (-b + delta ** 0.5) / (2 * a)
raiz2 = (-b - delta ** 0.5) / (2 * a)



print(f"raiz 2: {raiz1}")
print(f"raiz 1: {raiz2}")
Fim⬆️

6°:"⦁	Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos."

Inicio⬇️
x = float(int("3"))
y = float(int("5"))


troca = (x)
x = y
y = troca


print(f"O novo x é {x}")
print(f"O novo y é {y}")
Fim⬆️


7°:"⦁	Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume."

Inicio⬇️
comprimento = float(input("digite comprimento:"))
largura = float(input("digite largura:"))
altura = float(input("digite altura:"))

volume = int(comprimento * altura * largura)


print(f"o volume do paralelepípedo é: {volume}")
Fim⬆️

8°⦁	Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m."

Inicio⬇️
depósito = float(input("digite o depósito:"))
rendimento = round(depósito * 1.013, 4)

print(f"o rendimento é de: {rendimento}")
Fim⬆️

9°:"⦁	Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados."

Inicio⬇️

N1 = float(input("Insira um primeiro número natural:"))
N2 = float(input("Insira um segundo número natural:"))

q1 = int(N1 ** 2)
q2 = int(N2 ** 2)

soma = int(q1 + q2)

print(f"A soma dos quadrados é: {soma}")
Fim⬆️

10°:"⦁	Receba 2 números reais. Calcule e mostre a diferença desses valores."

Inicio⬇️
R1 = float(input("Insira um primeiro número real:"))
R2 = float(input("Insira um segundo número real:"))

diferença = float(input(R1 - R2))


print(f"A diferença dos números reais é: {diferença}")
Fim⬆️

11°:"⦁	Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência"

Inicio⬇️
import math
raio= float(input("Insira o valor do raio:"))
comprimento = float(int(2 * math.pi * raio))

print(f"O comprimento da circunfêrencia é de: {comprimento}")
Fim⬆️

12°:"⦁	Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos."

Inicio⬇️
ano1= float(input("Insira o seu ano de nascimento:"))
ano2 = float(input("Insira o ano atual:"))

idade = float(int(ano2 - ano1))
idade2 = float(int(idade + 17))


print(f"Sua idade atual é: {idade}")
print(f"Sua idade em 17 anos será de: {idade2}")
Fim⬆️

13°:"⦁	Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia."

Inicio⬇️
q1= float(input("Insira a quantia, em quilos, dos alimentos disponíveis:"))
duração = float(int(q1 * 1000 / 50))

print(f"Essa quantia de alimentos será sufiente para: {duração} dias ")
Fim⬆️

14°:"⦁	Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo."

Inicio⬇️
ang1= float(input("Insira o valor do primeiro ângulo:"))
ang2= float(input("Insira o valor do segundo ângulo:"))

ang3 = float(int(ang1 + ang2) - 180 )

print(f"O valor do terceiro ângulo é de: {ang3} ")
Fim⬆️

15°:"⦁	Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa."

Inicio⬇️
import math
cateto1 = float(input("Insira o valor do primeiro cateto:"))
cateto2 = float(input("Insira o valor do segundo cateto:"))

hip = float(int(math.sqrt (cateto1 ** 2 + cateto2 ** 2)))

print(f"O valor da hipotenusa é: {hip} ")
Fim⬆️

16°:"⦁	Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber"

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

17°:"⦁	Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média."

Inicio⬇️
tempo = float(input("qual foi a duração da viagem em horas?:"))
vm = float(input("qual foi a velocidade média do percurso?:"))

litros = float(int(tempo * vm) / 12 )

print(f"Tendo em vista que o seu veículo consuma 12 litros por km, seu consumo foi de: {litros} litros")
Fim⬆️






