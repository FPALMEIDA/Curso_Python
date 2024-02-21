# PROGRAMA PARA CALCULAR MÉDIA FINAL
# Desenvolvido por Felipe Pereira

print("****************************************")
print("             NOTAS MENSAIS              ")
print("****************************************")
print()

# CRIAÇÃO DAS VARIAVEIS

nome = ""
bimestre1 = 0.0
bimestre2 = 0.0
bimestre3 = 0.0
bimestre4 = 0.0
nota_final = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o nome do aluno: ")
bimestre1 = float(input("Digite a nota do 1° bimestre: "))
bimestre2 = float(input("Digite a nota do 2° bimestre: "))
bimestre3 = float(input("Digite a nota do 3° bimestre: "))
bimestre4 = float(input("Digite a nota do 4° bimestre: "))


# PROCESSAR OS VALORES PARA OBTER O IMB

nota_final = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4


# SAIDA DO PROCESSAMENTO

print()
print("----------------------------------------")
print("|             MÉDIA FINAL              |")
print("----------------------------------------")
print()
print(nome+", a sua nota final é "+ str(nota_final))
