numero = int(input("Digite um número: "))

soma = 1
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i
    soma = soma + (1 / fatorial)

print("O resultado da série é:", soma)
