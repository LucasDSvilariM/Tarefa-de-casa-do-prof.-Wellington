h1 = int(input("Informe o primeiro horário: "))
m1 = int(input("Informe o primeiro minuto: "))
h2 = int(input("Infome o segundo horário': "))
m2 = int(input("Informe o segundo minuto: "))

hora_extra =  (m1 + m2) // 60
minuto = (m1 + m2) % 60
horas = h1 + h2 + hora_extra - 24

if horas < 0:
    horas = horas * -1
if horas > 12:
    horas = horas - 12
print(f"{horas}:{minuto:02d}")