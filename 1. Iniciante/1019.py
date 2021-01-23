segundos = int(input())

horas = int(segundos / 3600)
minutos = int((segundos - (horas * 3600)) / 60)
segundos = int(segundos % 60)

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))