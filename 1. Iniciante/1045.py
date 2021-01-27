array = list(map(float, input().split(' ')))

a, b, c = sorted(array, reverse= True)

if(a>=b+c):
    print("NAO FORMA TRIANGULO")
else:
    if pow(a, 2) == pow(b, 2) + pow(c,2):
        print("TRIANGULO RETANGULO")
    if pow(a, 2) > pow(b, 2) + pow(c,2):
        print("TRIANGULO OBTUSANGULO")
    if pow(a, 2) < pow(b, 2) + pow(c,2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b:
        print("TRIANGULO ISOSCELES")
    elif a == c:
        print("TRIANGULO ISOSCELES")
    elif b == c:
        print("TRIANGULO ISOSCELES")