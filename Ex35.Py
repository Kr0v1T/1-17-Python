valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

soma = 0

for numero in range(menor, maior + 1):
    if numero % 2 != 0:
        soma = soma + numero

print("A soma dos números ímpares é:", soma)
