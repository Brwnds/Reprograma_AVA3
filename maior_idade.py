ano_nascimento = int(input("Informe o ano de nascimento: "))
tem_carteira = input("Possui carteira de motorista? (S/N): ")

idade = 2024 - ano_nascimento

if idade >= 18:
    if tem_carteira.upper() == 'S':
        print("Pode dirigir no Brasil.")
    else:
        print("Não pode dirigir no Brasil sem possuir carteira de motorista.")
else:
    print("Não possui idade suficiente para dirigir no Brasil.")
