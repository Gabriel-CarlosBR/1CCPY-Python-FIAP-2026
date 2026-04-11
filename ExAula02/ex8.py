print ("Compra de ferramentas")

peca = ["Chave de fenda", "Martelo"]
nuPec = []
prePec = [15, 20]
resCont = []


for i in range(2):
  print (f"{peca[i]} custa {prePec[i]}")

for i in range(2):
  nuPec.append (int(input(f"Quantas {peca[i]} vc quer comprar? ")))

for i in range(2):
  resCont.append (nuPec[i] * prePec[i])
  print (resCont[i])

print ("O valor total a pagar é ", resCont[0] + resCont[1])  