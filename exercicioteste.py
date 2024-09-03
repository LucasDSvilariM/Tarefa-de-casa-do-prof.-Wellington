tipo = input("Informe o tipo de combustível: "
             "E para E-etanol e G para gasolina ")
qtd = float(input("Quantos litros foram abastecidos? "))

if tipo == "E" or tipo == "e":
    resultado = qtd * 4.9
    print(f"Total de E-etanol abastecidos: ", resultado)

elif tipo == "G" or tipo == "g":
    resultado = qtd * 5.8
    print(f"Total de Gasolina abastecidos: ", resultado)
else:
   print("tipo inválido")

