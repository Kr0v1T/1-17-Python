import math

A = int(input("Inserir valor de A:"))
B = int(input("Inserir valor de B: "))
C = int(input("Inseir valor de C: "))

D = B**2 - 4*A*C

print("Delta =", D)

if D < 0:
    print("Não Existe raíze reais.")
elif D == 0:
    X = - B /(2 *A)
    print("Existe apenas uma raiz real.")
    print("X =" , X)
else:
    X1 = (-B + math.sqrt(D)) / (2*A)
    X2 = (-B - math.sqrt(D)) / (2*A)

    print("Existe duas raízes reais.")
    print("X1 =", X1)
    print("X2 =", X2)
