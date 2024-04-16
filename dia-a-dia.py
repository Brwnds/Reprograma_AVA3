horario = float(input("Informe o horário (em horas): "))

if horario < 5:
    print("Esperando em casa.")
elif 5 <= horario < 5.5:
    print("Pegando o primeiro ônibus para o Parkshopping.")
elif 5.5 <= horario < 6:
    print("Descendo na rodoviária interestadual de Brasília.")
elif 6 <= horario < 6.25:
    print("Pegando o BRT para chegar ao estágio na Agência Espacial Brasileira.")
elif 6.25 <= horario < 12:
    print("No estágio, trabalhando.")
elif 12 <= horario < 13:
    print("Almoçando.")
elif 13 <= horario < 14:
    print("Ajudando um funcionário a mexer com Arduino em C.")
elif 14 <= horario < 14.5:
    print("Preparando-me para sair.")
elif 14.5 <= horario < 15:
    print("Pegando o penúltimo ônibus para a rodoviária.")
else:
    print("Pegando o último ônibus para minha cidade.")
