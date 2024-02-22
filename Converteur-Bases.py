N = int(input("Entrer un nombre : "))
B = int(input("Entrer La base de Nombre précédent : "))
Con = int(input("La base tu veux convert? : "))

R = 0
ord = 0
while N != 0:
    reste = N % Con
    p = 10 ** ord
    p = B ** ord
    R = R + reste * p
    ord = ord + 1
    N = N // Con
print(R)
    