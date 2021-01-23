linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, numPcs1, valor1 = linha1
cod2, numPcs2, valor2 = linha2

valorTotal = (int(numPcs1) * float(valor1)) + (int(numPcs2) * float(valor2))

print("VALOR A PAGAR: R$ " + "{:.2f}".format(valorTotal))