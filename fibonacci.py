n = int(input("Digite a quantidade de elementos: "))
penultimo = ultimo= 1

if(n==1) or (n==2):
    print("1")
else:
    count=1
    while count <=n:
        if(count ==1) or (count==2):
            print("1")
            count+=1
        else:
            termo = ultimo + penultimo
            ultimo = penultimo
            penultimo = termo
            count+=1
            print(termo)
