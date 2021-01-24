dias = int(input())
anos = int(dias / 365)
meses = int((dias - (anos * 365)) / 30)
dias = int(dias % 365 % 30)

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")