import unittest


class TestCalculadoraSalario(unittest.TestCase):

    def test_calcular_salario_desenvolvedor_maior_igual_3000(self):
        funcionario = Funcionario("Joao Silva", "joao@exemplo.com", 3500.00, "DESENVOLVEDOR")
        salario_liquido = funcionario.calcular_salario_liquido()
        self.assertEqual(salario_liquido, 2800.00)

    def test_calcular_salario_desenvolvedor_menor_que_3000(self):
        funcionario = Funcionario("Maria Silva", "maria@exemplo.com", 2800.00, "DESENVOLVEDOR")
        salario_liquido = funcionario.calcular_salario_liquido()
        self.assertEqual(salario_liquido, 2520.00)

    # ... (Testes para os outros cargos e situações de erro)


if __name__ == "__main__":
    unittest.main()
