preco_atual = float(input("Digite o preço atual: "))
venda_mensal = int(input("Digite a média mensal de vendas: "))

if venda_mensal < 500 and preco_atual < 30:
    preco_novo = preco_atual * 1.10

elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
    preco_novo = preco_atual * 1.15

elif venda_mensal >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual * 0.95

else:
    preco_novo = preco_atual

print("O novo preço é: R$", preco_novo)
