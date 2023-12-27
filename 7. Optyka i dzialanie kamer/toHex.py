plik = open('dane4.txt', 'r')

dane = plik.readlines()

najwieksza = 1
najmniejsza = 1

#4.1
print(dane[0][:-1])
for element in range(len(dane)-1):
    if abs(int(dane[element+1][:-1]) - int(dane[element][:-1])) > najwieksza:
        najwieksza = int(dane[element+1][:-1]) - int(dane[element][:-1])
    if abs(int(dane[element+1][:-1]) - int(dane[element][:-1])) < najmniejsza:
        najmniejsza = int(dane[element+1][:-1]) - int(dane[element][:-1])

print("Największa luka:",najwieksza, "\n"+"Najmniejsza luka:",najmniejsza)
###########################################