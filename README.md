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


