class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo

    def calcular_salario_liquido(self):
        taxa_desconto = self.obter_taxa_desconto()
        desconto = self.salario_base * taxa_desconto
        salario_liquido = self.salario_base - desconto
        return salario_liquido

    def obter_taxa_desconto(self):
        if self.cargo == "DESENVOLVEDOR":
            if self.salario_base >= 3000.00:
                return 0.2
            else:
                return 0.1
        elif self.cargo == "DBA":
            if self.salario_base >= 2000.00:
                return 0.25
            else:
                return 0.15
        # ... (Implementar lógica para os outros cargos)

class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario):
        return funcionario.calcular_salario_liquido()

    # ... (Métodos para calcular salário de acordo com o cargo, se necessário)
