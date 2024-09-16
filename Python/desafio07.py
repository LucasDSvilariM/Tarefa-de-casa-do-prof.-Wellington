qnt = int(input("Digita a quantidade de alunos: "))
soma = 0
for i in range(1,qnt+1):
    n = float(input("Digite a nota: "))
    soma = soma + n
media = soma / qnt
print(f"a média dos alunos é: {media}")