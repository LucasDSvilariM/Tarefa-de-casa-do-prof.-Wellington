opcao = 1
while opcao !=2:
    cont = 0
    for x in range(10):
        val = int(input("Digite o valor: "))
        if val < 0:
            cont = cont + 1
    print(f"Valores negativos são: {cont}")
    opcao = int(input("Deseja continar 1 - sim ou 2 para cacelar "))
print("cancelado.")