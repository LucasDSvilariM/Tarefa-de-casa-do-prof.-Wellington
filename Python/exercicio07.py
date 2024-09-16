time1 = input("nome do primeiro time: ")
gols1= int(input(f"quantos gols o {time1} fez "))
time2 = input("nome do segundo time: ")
gols2= int(input(f"quantos gols o {time2} fez "))



if gols1 == gols2:
    print("partida terminou empatado")
elif gols1>gols2:
    print(f"O {time1} foi o vencedor")
else:
    print(f"O {time2} foi o vencedor")