nomes = ["Jão","Ale","Bia","Jô"]

for i in range(len(nomes) - 1):
    for j in range(i+1, len(nomes)):
        print(nomes[i],nomes[j])

