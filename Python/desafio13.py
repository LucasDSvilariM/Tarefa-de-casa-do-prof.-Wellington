opcao = 1
while opcao != 2:

    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Nota inválida."
                            "Digite a primeira nota novamente: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Nota inválida."
                        "Digite a segunda nota novamente: "))

    media = (nota1+nota2)/2
    print(media)
    opcao = int(input("Deseja realizar um novo cálculo?\n"
                      "1 para continuar ou"
                      " 2 para encerrar:"))

