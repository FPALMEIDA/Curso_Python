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

combustivel_utilizado = distancia_viagem / autonomia_veiculo
valor_total = combustivel_utilizado * valor_combustivel


# SAIDA DO PROCESSAMENTO

print()
print("----------------------------------------")
print("|              RESULTADO               |")
print("----------------------------------------")
print()
print(f"Modelo do veículo: {modelo_veiculo}")
print(f"Autonomia do veiculo: {autonomia_veiculo}Km/l")
print(f"Distancia percorrida: {distancia_viagem}Km")
print(f"Valor do combustivel: R${valor_combustivel}")
print()
print("----------------------------------------")
print(f"Quantidade de combustível utilizado: {combustivel_utilizado:.3f}l")
print(f"Total gasto com a viagem: R${valor_total:.2f}")
print("----------------------------------------")



