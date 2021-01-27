h1 , m1, h2, m2 = map(int, input().split(" "))
rh=h2-h1

if rh<0:
    rh=24+rh

rm=m2-m1

if rm<0:
    rm=60+rm
    rh-=1

if h1==h2 and m1==m2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(rh,rm))