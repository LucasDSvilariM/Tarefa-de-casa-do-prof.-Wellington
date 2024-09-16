tipo = input("Informe o tipo de combustível"
             "E para E-etanol e G para Gasolina ")

qtd = float(input("Quantos litros foram abastecidos? "))

if tipo == "G":
    resultado = qtd * 5.8
else:
    resultado = qtd * 4.9

print(f"foram abastecidos {qtd} de {tipo} e custou  {resultado} reais")
