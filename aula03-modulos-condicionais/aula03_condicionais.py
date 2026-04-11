# RELACIONAIS
idade = 20

maior_idade = idade >= 18
print(maior_idade)

if maior_idade:
    print("Maior de idade")
else:
    print("aa")

#operadores Lógicos
#AND, OR, NOT

verifica_email = True
verifica_senha = False

login = verifica_senha and verifica_email
print(login)

if not login:
    print("Deu certo")

#notas....
print() #pular linha
nota_final = 2

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")



print("FIM")
