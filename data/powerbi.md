# Base de Conhecimento — Power BI

## 1. Visão geral

Power BI é uma ferramenta utilizada para análise e visualização de dados.

Um projeto no Power BI normalmente envolve:

* Importação ou conexão com dados
* Transformação dos dados
* Modelagem
* Criação de medidas e cálculos
* Construção de visualizações
* Publicação e compartilhamento dos relatórios

---

## 2. Tabelas fato e dimensão

### Tabela fato

A tabela fato normalmente contém os eventos ou transações que serão analisados.

Exemplos:

* vendas
* pedidos
* movimentações
* pagamentos

Ela normalmente possui valores numéricos que podem ser agregados, como quantidade, receita e custo.

### Tabela dimensão

A tabela dimensão contém informações utilizadas para descrever e categorizar os dados da tabela fato.

Exemplos:

* clientes
* produtos
* funcionários
* calendário
* regiões

Uma estrutura comum é:

```text
Dimensão → Fato
```

Por exemplo:

```text
DimCliente
    ↓
FatoVendas
```

---

## 3. Relacionamentos

Relacionamentos conectam tabelas por meio de colunas relacionadas.

Exemplo:

```text
DimCliente[ID_Cliente]
        ↓
FatoVendas[ID_Cliente]
```

O relacionamento permite que filtros aplicados à dimensão afetem os dados da tabela fato.

---

## 4. Cardinalidade

A cardinalidade define como os registros de duas tabelas se relacionam.

Os principais tipos são:

* 1:1 — um para um
* 1:N — um para muitos
* N:1 — muitos para um
* N:N — muitos para muitos

Em modelos dimensionais, o relacionamento mais comum é:

```text
Dimensão (1) ─────── (*) Fato
```

Por exemplo:

```text
DimCliente (1) ─────── (*) FatoVendas
```

Um cliente pode possuir várias vendas.

---

## 5. Medidas

Medidas são cálculos criados utilizando DAX.

### Exemplo

```DAX
Total Vendas =
SUM(FatoVendas[ValorVenda])
```

A medida é calculada de acordo com o contexto dos filtros aplicados no relatório.

---

## 6. DAX

DAX (Data Analysis Expressions) é a linguagem utilizada pelo Power BI para criação de medidas, colunas calculadas e outros cálculos.

Algumas funções comuns:

* SUM
* COUNT
* DISTINCTCOUNT
* AVERAGE
* CALCULATE
* FILTER
* IF
* SWITCH

### Exemplo com CALCULATE

```DAX
Vendas 2026 =
CALCULATE(
    [Total Vendas],
    DimCalendario[Ano] = 2026
)
```

---

## 7. Power Query

O Power Query é utilizado principalmente para importar e transformar dados antes de carregá-los no modelo.

Algumas operações comuns:

* Remover colunas
* Alterar tipos de dados
* Filtrar linhas
* Dividir colunas
* Mesclar consultas
* Acrescentar consultas
* Criar colunas
* Substituir valores

O Power Query utiliza a linguagem M.

---

## 8. Modelo em estrela

O modelo em estrela é uma abordagem comum para organizar modelos analíticos.

Exemplo:

```text
              DimCliente
                   |
DimProduto ─── FatoVendas ─── DimCalendario
                   |
              DimVendedor
```

A tabela fato fica no centro e as dimensões ficam ao redor.

Esse modelo normalmente facilita a criação de análises e o gerenciamento dos relacionamentos.

---

## 9. Boas práticas

* Preferir modelos em estrela quando apropriado.
* Criar uma tabela calendário para análises temporais.
* Evitar relacionamentos desnecessários.
* Preferir medidas DAX para cálculos analíticos reutilizáveis.
* Utilizar nomes claros para tabelas, colunas e medidas.
* Evitar excesso de informações em uma única visualização.
* Verificar os relacionamentos antes de analisar resultados.

---

## 10. Regra do DataAssist

Quando uma dúvida sobre Power BI puder ser respondida utilizando esta base, o DataAssist deve priorizar essas informações.

Quando a pergunta estiver fora da base de conhecimento ou exigir informações que não esteja
