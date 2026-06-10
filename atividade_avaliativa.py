faturamento = 0
ticketmedio = 0
leve = 0
padrao = 0
pesado = 0
internacionais = 0
nacional = 0
contador = 0
while contador <= 9:
    contador = contador + 1
    print("-------------")
    print("pacote n:" + str(contador))
    print("Digite o peso do pacote")
    peso = float(input())
    print("O frete é internacional? sim/não")
    internacional = input()
    if peso <= 2:
        valor = 10
        leve = leve + 1
        print("peso leve")
        print("taxa base R$10")
    else:
        if peso > 2 and peso <= 10:
            valor = 20
            padrao = padrao + 1
            print("peso: padrao")
        else:
            valor = 30
            pesado = pesado + 1
            print("peso: pesado")
    if internacional == "sim":
        taxa = 1.2
        internacionais = internacionais + 1
        print("acrescimo internacional: 20%")
    else:
        taxa = 0
        nacional = nacional + 1
        print("sem acrescimo internacional")
    valorfinal = valor + valor * taxa
    faturamento = faturamento + valorfinal
    valorfinal = valorfinal + valor
    print("valor total acumulado: " + str(valorfinal))
ticketmedio = faturamento / 10
print("---------------")
print("RELATORIO FINAL")
print("--------------")
print("pacotes processados: 10")
print("pacotes leves:" + str(padrao))
print("pacotes padrao:" + str(padrao))
print("pacotes pesados:" + str(pesado))
print("--------------")
print("frete internacionais:" + internacional)
print("frete nacional:" + str(nacional))
print("--------------")
print("faturamento total: R$ " + str(faturamento))
print("ticket medio por pacote:" + str(ticketmedio))
print("--------------")
