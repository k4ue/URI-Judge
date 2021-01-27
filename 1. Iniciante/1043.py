a, b, c = map(float, input().split(" "))
perimetro = 0
area = 0

if (a+b)>c and (b+c)>a and (c+a)>b:
    perimetro = a+b+c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = 0.5*(a+b)*c
    print("Area = {:.1f}".format(area))