linha = input().split(" ")

A, B, C = linha
A = float(A)
B = float(B)
C = float(C)

print("TRIANGULO: " + "{:.3f}".format((A*C)/2))
print("CIRCULO: " + "{:.3f}".format(3.14159 * pow(C, 2)))
print("TRAPEZIO: " + "{:.3f}".format(((A + B) * C)/2))
print("QUADRADO: " + "{:.3f}".format(pow(B, 2)))
print("RETANGULO: " + "{:.3f}".format((A * B)))