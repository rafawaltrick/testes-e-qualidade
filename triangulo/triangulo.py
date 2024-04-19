def classificar_triangulo(lado_a, lado_b, lado_c):
  """
  Classifica um triângulo com base nos comprimentos de seus lados.

  Argumentos:
    lado_a (int): Comprimento do lado A.
    lado_b (int): Comprimento do lado B.
    lado_c (int): Comprimento do lado C.

  Retorna:
    str: Classificação do triângulo ("Escaleno", "Isósceles", "Equilátero", "Inválido").
  """

  if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
    return "Inválido"

  if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
    return "Inválido"

  if lado_a == lado_b and lado_b == lado_c:
    return "Equilátero"
  elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    return "Isósceles"
  else:
    return "Escaleno"
