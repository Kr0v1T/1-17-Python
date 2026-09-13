valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

print("Números primos entre", menor, "e", maior, ":")

for numero in range(menor, maior + 1):
    if numero < 2:
        continue

    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(numero, end=" ")
