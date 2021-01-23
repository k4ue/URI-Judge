numFunc = int(input())
numHoraTrab = int(input())
valorPorHora = float(input())
salario = numHoraTrab * valorPorHora

print("NUMBER =", numFunc)
print("SALARY = U$ " + "{:.2f}".format(salario))