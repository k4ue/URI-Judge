codigo, qtd = map(int, input().split(" "))
total = 0.00

if codigo == 1:
    total = qtd * 4.00
elif codigo == 2:
    total = qtd * 4.50
elif codigo == 3:
    total = qtd * 5.00
elif codigo == 4:
    total = qtd * 2.00
elif codigo == 5:
    total = qtd * 1.50

print("Total: R$ " + "{:.2f}".format(total))
