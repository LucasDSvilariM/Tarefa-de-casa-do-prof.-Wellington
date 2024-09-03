tipo = input("Informe o tipo de combustível: "
             "E para E-etanol e G para gasolina ")
qtd = float(input("Quantos litros foram abastecidos? "))

if tipo == "E" or tipo == "e":
    resultado = qtd * 4.9
    print("E-etanol")
    print(resultado)

elif tipo == "G" or tipo == "g":
    resultado = qtd * 5.8
    print("gasolina")
    print(resultado)
else:
   print("tipo inválido")

