def eh_triangulo(a, b, c):
  """
  Função que verifica se os lados formam um triângulo e retorna o tipo de triângulo.

  Argumentos:
    a (float): Medida do lado A.
    b (float): Medida do lado B.
    c (float): Medida do lado C.

  Retorno:
    str: "Triângulo Equilátero" se todos os lados forem iguais.
    str: "Triângulo Isósceles" se dois lados forem iguais.
    str: "Triângulo Escaleno" se todos os lados forem diferentes.
    str: "Não é um triângulo" se as medidas não formarem um triângulo.
  """
  # Condição para ser um triângulo
  if a < b + c and b < a + c and c < a + b:
    # Verificação do tipo de triângulo
    if a == b and b == c:
      return "Triângulo Equilátero"
    elif a == b or a == c or b == c:
      return "Triângulo Isósceles"
    else:
      return "Triângulo Escaleno"
  else:
    return "Não é um triângulo"

# Leitura dos lados do triângulo
a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

# Resultado
resultado = eh_triangulo(a, b, c)

# Exibição do resultado
print(f"\n{resultado}")
