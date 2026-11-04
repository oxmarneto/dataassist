# Base de Conhecimento — Excel

## 1. Visão geral

Excel é uma ferramenta utilizada para organização, tratamento, análise e visualização de dados.

Entre os recursos mais utilizados estão:

* Fórmulas e funções
* Tabelas
* Filtros
* Tabelas dinâmicas
* Gráficos
* Validação de dados
* Formatação condicional
* Power Query

---

## 2. Fórmulas e funções

As funções permitem realizar cálculos e operações sobre os dados.

Algumas funções comuns:

* SUM — soma
* AVERAGE — média
* COUNT — contagem
* IF — condição
* COUNTIF — contagem com critério
* SUMIF — soma com critério
* XLOOKUP — busca de informações

### Exemplo de soma

```excel id="r9c8wu"
=SUM(B2:B10)
```

Calcula a soma dos valores entre B2 e B10.

---

## 3. Função SE

A função SE permite realizar uma avaliação condicional.

### Exemplo

```excel id="5n4yqe"
=SE(B2>=5000;"Alto";"Baixo")
```

Se o valor de B2 for maior ou igual a 5000, retorna "Alto". Caso contrário, retorna "Baixo".

---

## 4. PROCV e PROCX

Funções de busca são utilizadas para encontrar informações relacionadas a uma chave.

### PROCV

O PROCV realiza uma busca vertical em uma tabela.

### PROCX

O PROCX é uma alternativa mais moderna e flexível para realizar buscas.

Exemplo:

```excel id="t7w9kp"
=PROCX(A2;TabelaClientes[ID];TabelaClientes[Nome])
```

Nesse exemplo, o Excel procura o ID de A2 na coluna `ID` e retorna o nome correspondente.

---

## 5. Tabela dinâmica

A tabela dinâmica permite resumir e analisar grandes volumes de dados.

Pode ser utilizada para:

* Somar valores
* Contar registros
* Calcular médias
* Agrupar informações
* Comparar categorias

Exemplo de análise:

```text id="3y3f3t"
Vendas por região
├── Nordeste
├── Sudeste
├── Sul
└── Centro-Oeste
```

---

## 6. Filtros

Filtros permitem visualizar apenas os registros que atendem a determinados critérios.

Exemplo:

Uma tabela de vendas pode ser filtrada para mostr
