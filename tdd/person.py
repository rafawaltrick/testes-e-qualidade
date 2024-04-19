from email import Email


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.emails = []

    def add_email(self, email):
        if isinstance(email, Email) and email.is_valid():
            self.emails.append(email)
        else:
            raise ValueError("E-mail inválido.")

    def isValidToInclude(self):
        """Verifica se a pessoa é válida para inclusão (nome, idade, e-mail)."""
        errors = []

        # Validação de nome
        if not self.name or len(self.name.split()) < 2 or not self.name.isalpha():
            errors.append("Nome inválido. Deve ter pelo menos 2 partes e conter apenas letras.")

        # Validação de idade
        if not 1 <= self.age <= 200:
            errors.append("Idade inválida. Deve estar entre 1 e 200 anos.")

        # Validação de email (pelo menos um)
        if not self.emails:
            errors.append("Pelo menos um e-mail é obrigatório.")

        return errors

    def __str__(self):
        return f"Nome: {self.name}\nIdade: {self.age}\nEmails: {', '.join(str(email) for email in self.emails)}"
