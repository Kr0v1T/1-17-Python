voltas = int(input("Digite o número de voltas: "))
extensao = float(input("Digite a extensão do circuito em metros: "))
tempo = float(input("Digite o tempo de duração em minutos: "))

distancia = voltas * extensao

distancia_km = distancia / 1000
tempo_horas = tempo / 60

velocidade = distancia_km / tempo_horas

print("A velocidade média é:", velocidade, "km/h")
