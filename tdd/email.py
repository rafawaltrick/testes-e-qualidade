import re


class Email:
    def __init__(self, address):
        self.address = address

    def is_valid(self):
        """Valida se o endereço de e-mail está no formato correto."""
        # Expressão regular aprimorada para validar o formato de email
        email_regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return bool(re.match(email_regex, self.address))

    def __str__(self):
        return self.address
