# Base de Conhecimento — Python

## 1. Visão geral

Python é uma linguagem de programação muito utilizada em análise de dados, automação, ciência de dados e desenvolvimento de aplicações.

Na análise de dados, Python pode ser utilizado para:

* Manipulação de dados
* Limpeza de dados
* Análise exploratória
* Automação de tarefas
* Criação de gráficos
* Integração com outras ferramentas

---

## 2. Variáveis

Nesse exemplo:
Variáveis armazenam valores que podem ser utilizados durante a execução de um programa.

### Exemplo: Variáveis

```python
nome = "Jorge"
idade = 30
salario = 3500.00
```

Nesse exemplo:

* `nome` armazena um texto.
* `idade` armazena um número inteiro.
* `salario` armazena um número decimal.

---

## 3. Tipos de dados

Alguns tipos de dados comuns em Python são:

* `str` — texto
* `int` — número inteiro
* `float` — número decimal
* `bool` — verdadeiro ou falso
* `list` — lista de valores
* `dict` — estrutura de chave e valor

### Exemplo: Tipos de dados

```python
nome = "Ana"
idade = 25
notas = [8, 9, 7]
```

---

## 4. Condições

As estruturas condicionais permitem executar diferentes comandos dependendo de uma condição.

### Exemplo: Condições

```python
salario = 3500

if salario >= 3000:
    print("Salário acima ou igual a 3000")
else:
    print("Salário abaixo de 3000")
```

---

## 5. Listas

Listas armazenam vários valores em uma única estrutura.

### Exemplo: Listas

```python
produtos = ["Notebook", "Mouse", "Teclado"]

print(produtos[0])
```

O resultado será:

```text
Notebook
```

---

## 6. Laços

O `for` pode ser utilizado para percorrer elementos de uma coleção.

### Exemplo: Laços

```python
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)
```

Resultado:

```text
10
20
30
```

---

## 7. Funções

Funções permitem organizar código reutilizável.

### Exemplo: Funções

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

resultado = calcular_media(8, 10)
print(resultado)
```

Resultado:

```text
9.0
```

---

## 8. Pandas

Pandas é uma biblioteca muito utilizada para manipulação e análise de dados.

### Exemplo: Pandas

```python
import pandas as pd

dados = pd.DataFrame({
    "Produto": ["A", "B", "C"],
    "Vendas": [100, 200, 150]
})

print(dados)
```

O `DataFrame` representa uma estrutura tabular semelhante a uma tabela.

---

## 9. Leitura de arquivos

O Pandas pode ser utilizado para carregar arquivos CSV.

### Exemplo: Leitura de arquivos

```python
import pandas as pd

dados = pd.read_csv("vendas.csv")

print(dados.head())
```

O método `head()` apresenta as primeiras linhas do DataFrame.

---

## 10. Boas práticas

* Utilizar nomes claros para variáveis e funções.
* Evitar repetir código desnecessariamente.
* Organizar o código em funções quando apropriado.
* Utilizar comentários para explicar trechos que realmente precisem de contexto.
* Verificar os tipos dos dados antes de realizar operações.
* Utilizar bibliotecas adequadas para cada tarefa.
* Tratar erros quando necessário.
* Manter o código simples e legível.

---

## 11. Regra do DataAssist

Quando uma dúvida sobre Python puder ser respondida utilizando esta base, o DataAssist deve priorizar essas informações.

Quando a pergunta estiver fora da base de conhecimento ou exigir informações que não estejam disponíveis, o DataAssist deve informar sua limitação em vez de inventar uma resposta.
