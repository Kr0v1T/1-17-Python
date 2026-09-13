numero = int(input("Digite um número inteiro: "))

a = 0
b = 1

for i in range(numero):
    print(a, end=" ")

    proximo = a + b
    a = b
    b = proximo
