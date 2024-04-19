import unittest
from triangulo import classificar_triangulo


class TestClassificarTriangulo(unittest.TestCase):

    def test_triangulo_escaleno(self):
        classificacao = classificar_triangulo(3, 4, 5)
        self.assertEqual(classificacao, "Escaleno")

    def test_triangulo_isosceles_1(self):
        classificacao = classificar_triangulo(4, 4, 3)
        self.assertEqual(classificacao, "Isósceles")

    def test_triangulo_isosceles_2(self):
        classificacao = classificar_triangulo(3, 4, 4)
        self.assertEqual(classificacao, "Isósceles")

    def test_triangulo_isosceles_3(self):
        classificacao = classificar_triangulo(4, 3, 4)
        self.assertEqual(classificacao, "Isósceles")

    def test_triangulo_equilatero(self):
        classificacao = classificar_triangulo(4, 4, 4)
        self.assertEqual(classificacao, "Equilátero")

    def test_triangulo_invalido_lado_zero(self):
        classificacao = classificar_triangulo(0, 4, 3)
        self.assertEqual(classificacao, "Inválido")

    def test_triangulo_invalido_lado_negativo(self):
        classificacao = classificar_triangulo(-1, 4, 3)
        self.assertEqual(classificacao, "Inválido")

    def test_triangulo_invalido_soma_menor_que_um_lado(self):
        classificacao = classificar_triangulo(1, 1, 3)
        self.assertEqual(classificacao, "Inválido")

    def test_triangulo_todos_lados_iguais_zero(self):
        classificacao = classificar_triangulo(0, 0, 0)
        self.assertEqual(classificacao, "Inválido")


if __name__ == "__main__":
    unittest.main()
