n = int(input("Digite a quantidade de elementos: "))
ultimo =  0
penultimo = termo= 1

while termo <=n:
    if(termo!=2):
        print(termo)
    termo = ultimo + penultimo
    ultimo = penultimo
    penultimo = termo




