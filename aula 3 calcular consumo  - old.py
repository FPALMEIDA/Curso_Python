# Programa para calcular CONSUMO DE COMBUSTIVEL
# Desenvolvido por Felipe Pereira

print("****************************************")
print("*      CONSUMO DE COMBUSTÍVEL          *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIAVEIS

modelo_veiculo = ""
autonomia_veiculo = 0
distancia_viagem = 0
valor_combustivel = 0.0
combustivel_utilizado = 0.0
valor_total = 0.0

# ENTRADA DOS DADOS
modelo_veiculo = input("Qual veiculo deseja realizar o calculo de consumo?: ")
autonomia_veiculo = int(input("Qual é a autonomia desse veiculo?: "))
distancia_viagem = int(input("Qual será a distancia da viagem?: "))
valor_combustivel = float(input("Qual o valor do combustivel?: "))

# PROCESSAR OS VALORES PARA OBTER O IMB

combustivel_utilizado = round(distancia_viagem / autonomia_veiculo,3)
valor_total = round(combustivel_utilizado * valor_combustivel,2)


# SAIDA DO PROCESSAMENTO

print()
print("----------------------------------------")
print("|              RESULTADO               |")
print("----------------------------------------")
print()
print("*Modelo do veículo: " + modelo_veiculo)
print("*Autonomia do veiculo: " + str(autonomia_veiculo) + "Km/l")
print("*Distancia percorrida: " + str(distancia_viagem) +"Km")
print("*Valor do combustivel: R$" + str(valor_combustivel))
print()
print("----------------------------------------")
print("Quantidade de combustível utilizado: "+ str(combustivel_utilizado) +"l")
print("Total gasto com a viagem: R$" + str(valor_total))
print("----------------------------------------")



