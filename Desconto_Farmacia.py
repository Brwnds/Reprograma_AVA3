codigo1 = input("Informe o código do primeiro produto: ")
codigo2 = input("Informe o código do segundo produto: ")

if codigo1 == codigo2:
    valor_total = 10  # Preço de dois produtos iguais
    valor_total -= 5  # Aplicando desconto de R$ 5,00
elif '0054' in [codigo1, codigo2]:
    valor_total = 10  # Preço de dois produtos diferentes
    valor_total -= 5  # Aplicando desconto de 50% em um dos produtos
else:
    valor_total = 10  # Preço de dois produtos diferentes

print("Valor total a pagar:", valor_total)
