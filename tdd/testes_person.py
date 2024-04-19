import unittest
from person import Person, Email


class TestIsValidToInclude(unittest.TestCase):
    def setUp(self):
        self.valid_person = Person("Joao Silva", 30)
        self.valid_person.add_email(Email("joao.silva@exemplo.com"))

        self.invalid_person = Person("Joao", 201)

    def test_nome_invalido_menos_que_2_partes(self):
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "Nome inválido. Deve ter pelo menos 2 partes e conter apenas letras.")

    def test_nome_invalido_sem_letras(self):
        self.invalid_person.name = "123 Joao"
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "Nome inválido. Deve ter pelo menos 2 partes e conter apenas letras.")

    def test_nome_invalido_vazio(self):
        self.invalid_person.name = ""
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "Nome inválido. Deve ter pelo menos 2 partes e conter apenas letras.")

    def test_idade_invalida_maior_que_200(self):
        self.invalid_person.age = 301
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "Idade inválida. Deve estar entre 1 e 200 anos.")

    def test_idade_invalida_menor_que_um(self):
        self.invalid_person.age = 0
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "Idade inválida. Deve estar entre 1 e 200 anos.")

    def test_sem_email(self):
        self.valid_person.emails = []
        errors = self.valid_person.isValidToInclude()
        self.assertEqual(errors[0], "Pelo menos um e-mail é obrigatório.")

    def test_email_invalido_formato(self):
        self.invalid_person.add_email(Email("joaosilva.com"))
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "E-mail inválido. Formato esperado: nome@dominio.extensao.")

    def test_email_invalido_partes_vazias(self):
        self.invalid_person.add_email(Email("@exemplo.com"))
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "E-mail inválido. Formato esperado: nome@dominio.extensao.")

    def test_email_invalido_menos_que_um_caractere_por_parte(self):
        self.invalid_person.add_email(Email("jo@exemplo.com"))
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "E-mail inválido. Formato esperado: nome@dominio.extensao.")

    def test_varios_emails_validos(self):
        self.valid_person.add_email(Email("outro.email@exemplo.com.br"))
        errors = self.valid_person.isValidToInclude()
        self.assertEqual(errors, [])

    def test_varios_emails_invalidos(self):
        self.invalid_person.add_email(Email("joaosilva.com"))
        self.invalid_person.add_email(Email("@exemplo.com"))
        self.invalid_person.add_email(Email("jo@exemplo.com"))
        errors = self.invalid_person.isValidToInclude()
        self.assertEqual(errors[0], "E-mail inválido. Formato esperado: nome@dominio.extensao.")
        self.assertEqual(errors[1], "E-mail inválido. Formato esperado: nome@dominio.extensao.")
        self.assertEqual(errors[2], "E-mail inválido. Formato esperado: nome@dominio.extensao.")


if __name__ == "__main__":
    unittest.main()
