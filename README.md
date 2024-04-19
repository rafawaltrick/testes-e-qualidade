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



## Estrutura de Arquivos e Execução Calculadora de Salário com TDD

**Estrutura de Arquivos:**

```
calculadora_salario/
├── testes_calculadora_salario.py      
├── calculadora_salario.py           
```

**Execução Simples:**

**1. Pré-requisitos:**

* Python 3 instalado
* Editor de código (Visual Studio Code, PyCharm, Sublime Text, etc.)

**2. Passos:**

1. **Crie o diretório:**
    * Crie um diretório chamado `calculadora_salario` no local desejado.
2. **Baixe os arquivos:**
    * Baixe os arquivos `testes_calculadora_salario.py`, `calculadora_salario.py` e `README.md` para dentro do diretório `calculadora_salario`.
3. **Abra o editor de código:**
    * Abra o diretório `calculadora_salario` no seu editor de código.
4. **Execute os testes:**
    * No terminal, navegue até o diretório `calculadora_salario`.
    * Execute o comando:

```
python3 testes_calculadora_salario.py
```


