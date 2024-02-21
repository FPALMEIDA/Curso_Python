# Programa para calcular IMC
# Desenvolvido por Felipe Pereira

print("****************************************")
print("*          CALCULADORA DE IMC          *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIAVEIS

nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMB

imc = peso / altura ** 2


# SAIDA DO PROCESSAMENTO

print()
print("****************************************")
print("*              RESULTADO               *")
print("****************************************")
print("*                                      *")
print("*NOME: " + nome)
print("*PESO: " + str(peso) + "Kg")
print("*ALTURA: " + str(altura) +"m")
print("*IMC: " + str(imc))
print("****************************************")
