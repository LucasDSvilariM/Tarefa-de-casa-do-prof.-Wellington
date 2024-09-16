senhasecret = 9090
x = 0
tentativa = 3

senhadigitada = int(input("Digite sua senha: "))

while senhadigitada != senhasecret and tentativa > 1:
    tentativa -= 1

    if tentativa > 0:
        print(f"Após 3 tentativas sua senha será bloqueada. Seu número de tentativas é {tentativa}")
        senhadigitada = int(input("Digite sua senha novamente: "))


    if senhadigitada == senhasecret:
        print("Acesso liberado")


else:
    print("Senha bloqueada.")


