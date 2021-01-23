def maior(a, b):
    a = int(a)
    b = int(b)

    return int((a + b + abs(a - b))/2)

dados = input().split(" ")
a, b, c = dados

print(maior(maior(a,b), c), "eh o maior")