nota1 = float(input("Sua primeira nota: "))
nota2 = float(input("Sua segunda nota: "))
nota3 = float(input("Sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"sua média foi {media}")
if media >= 7.0:
    print("aprovado")

elif media > 4:
    print("você está de recuperação")
else:
    print("reprovado")