numero = int(input("Digite um número: "))

soma = 0

for i in range(1, numero + 1):
    soma = soma + (1 / i)

print("O resultado da série é:", soma)
