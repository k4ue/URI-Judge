inicio, fim = map(int, input().split(" "))

duracao = fim - inicio

if duracao < 0:
    duracao = 24 + (fim - inicio)

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU", duracao, "HORA(S)")