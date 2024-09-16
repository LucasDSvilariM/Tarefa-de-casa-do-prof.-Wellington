tipo = input("Informe o tipo de combistível"
             "E para E-etanol e G para Gasolina: ")
qtd = float(input("Quantos litros foram abastecidos? "))

if tipo == "G" or tipo == "g":
    resultado = qtd * 5.8
    print("gasolina")
    print(resultado)
elif tipo == "E" or tipo == "e":
    resultado = qtd * 4.9
    print("E-etanol")
    print(resultado)
else:
    print("tipo inválido")