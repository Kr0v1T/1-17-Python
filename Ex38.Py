maior = 0
menor = 0

for i in range(100):
    numero = int(input("Digite um número positivo: "))

    if numero > maior:
        maior = numero

    if menor == 0 or numero < menor:
        menor = numero

print("Maior valor:", maior)
print("Menor valor:", menor)
