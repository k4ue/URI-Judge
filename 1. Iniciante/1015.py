x1, y1 = map(float, input().split(" ")) #Aprendi esse map. Nice. 
x2, y2 = map(float, input().split(" ")) 

print("{:.4f}".format(pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 1/2)))

