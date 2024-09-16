v3 = 1
while v3 !=2:
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))
    while valor2==0:
        valor2 = int(input("Valor inválido, digite o segundo valor novamente: "))
    divisao = valor1 / valor2
    print(f"resultado: {divisao}")
    v3 = int(input("Deseja continuar \n"
                      "1 para continuar  \n"
                      "2 para encerrar "))
    print("Encerrado.")
