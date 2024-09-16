n=0
soma=0

alunos = int(input("Digite a quantidade de alunos: "))
while n<alunos:
    n = n+1
    nota = float(input("Digite a nota: "))
    soma += nota
media = soma / alunos
print(f"A média é: {media}")

