### Exercício: Classificação de Triângulos

**Descrição:**

Este projeto implementa um programa em Python que classifica um triângulo com base nos comprimentos de seus lados. O programa verifica se os lados formam um triângulo válido e, em seguida, classifica-o como escaleno, isósceles ou equilátero.

**Estrutura de Diretórios:**

```
triangulo/
├── __init__.py
├── testes_triangulo.py
└── triangulo.py
```

**Instruções de Build:**

Para executar os testes, execute o seguinte comando no diretório raiz do projeto:

```bash
python3 -m unittest testes_triangulo
```

**Descrição dos Casos de Teste:**

Os casos de teste cobrem uma variedade de cenários, incluindo:

* Triângulos válidos: escaleno, isósceles e equilátero
* Permutações de valores válidos
* Valores inválidos: zero, negativo, violação da desigualdade do triângulo
* Casos de borda: todos os valores iguais a zero


## Implementação TDD da Validação de Pessoas

**Objetivo:**

Implementar o método `isValidToInclude` na classe `Person` utilizando a abordagem TDD (Desenvolvimento Guiado por Testes) para validar a inclusão de novos objetos `Person` em uma lista.

**Etapas:**

**1. Criar os Testes (testes_person.py):**

* Crie um novo arquivo `testes_person.py` para armazenar os testes unitários.
* Utilize a biblioteca `unittest` para definir a estrutura básica dos testes.
* Crie uma classe `TestIsValidToInclude` que herda de `unittest.TestCase`.
* Dentro da classe `TestIsValidToInclude`, defina métodos de teste para cada regra de validação:
    * Nome inválido (vazio, sem letras, menos de 2 partes).
    * Idade inválida (fora do intervalo [1, 200]).
    * Ausência de e-mail.
    * E-mail inválido (formato incorreto, partes vazias, menos de 1 caractere por parte).
* Cada método de teste deve:
    * Criar um objeto `Person` com dados válidos e outro com dados inválidos para a regra específica.
    * Chamar o método `isValidToInclude` no objeto válido e verificar se a lista de erros está vazia.
    * Chamar o método `isValidToInclude` no objeto inválido e verificar se a lista de erros contém a mensagem de erro esperada.
* Execute os testes usando o comando `python3 -m unittest testes_person.py`.

**2. Implementar o método `isValidToInclude` (person.py):**

* Crie um novo arquivo `person.py` para definir as classes `Person` e `Email`.
* Na classe `Person`, defina o método `isValidToInclude` que recebe um objeto `Person` como parâmetro:
    * Crie uma lista vazia para armazenar os erros.
    * Valide o nome:
        * Verifique se o nome está vazio ou contém apenas espaços.
        * Verifique se o nome possui pelo menos 2 partes separadas por espaços.
        * Verifique se todas as partes do nome contêm apenas letras.
        * Adicione a mensagem de erro para cada regra violada à lista de erros.
    * Valide a idade:
        * Verifique se a idade está dentro do intervalo [1, 200].
        * Adicione a mensagem de erro à lista de erros se a idade for inválida.
    * Valide a existência de pelo menos um e-mail:
        * Verifique se a lista de e-mails do objeto `Person` está vazia.
        * Adicione a mensagem de erro à lista de erros se não houver e-mails.
    * Valide cada e-mail:
        * Crie um método auxiliar para validar o formato do e-mail (formato esperado: nome@dominio.extensao).
        * Para cada e-mail na lista, utilize o método auxiliar para verificar se o formato é válido.
        * Adicione a mensagem de erro à lista de erros se o e-mail for inválido.
    * Retorne a lista de erros.
* Execute os testes novamente para garantir que o método `isValidToInclude` esteja funcionando corretamente.


