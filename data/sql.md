# Base de Conhecimento — SQL

## 1. SELECT

O comando SELECT é utilizado para consultar dados em uma tabela.

### Sintaxe básica

```sql
SELECT coluna1, coluna2
FROM tabela;
```

### Consulta de funcionários

```sql
SELECT nome, salario
FROM funcionarios;
```

---

## 2. WHERE

O WHERE é utilizado para filtrar registros de acordo com uma condição.

### Filtragem por salário

```sql
SELECT *
FROM funcionarios
WHERE salario > 3000;
```

Nesse exemplo, serão retornados apenas os funcionários cujo salário seja maior que 3000.

---

## 3. ORDER BY

O ORDER BY é utilizado para ordenar os resultados de uma consulta.

### Ordenação por salário

```sql
SELECT nome, salario
FROM funcionarios
ORDER BY salario DESC;
```

`DESC` ordena do maior para o menor.

`ASC` ordena do menor para o maior.

---

## 4. GROUP BY

O GROUP BY agrupa registros que possuem o mesmo valor em determinada coluna.

É normalmente utilizado junto com funções de agregação, como SUM, COUNT e AVG.

### Contagem por departamento

```sql
SELECT departamento, COUNT(*) AS quantidade
FROM funcionarios
GROUP BY departamento;
```

Nesse exemplo, os funcionários são agrupados por departamento e é contabilizada a quantidade de funcionários em cada departamento.

---

## 5. Funções de agregação

As principais funções de agregação são:

* COUNT — quantidade de registros
* SUM — soma
* AVG — média
* MIN — menor valor
* MAX — maior valor

### Resumo salarial

```sql
SELECT
    COUNT(*) AS quantidade,
    SUM(salario) AS total_salarios,
    AVG(salario) AS salario_medio
FROM funcionarios;
```

---

## 6. CASE WHEN

O CASE WHEN permite criar condições dentro de uma consulta SQL.

### Classificação por faixa salarial

```sql
SELECT
    nome,
    salario,
    CASE
        WHEN salario >= 5000 THEN 'Alto'
        WHEN salario >= 3000 THEN 'Medio'
        ELSE 'Baixo'
    END AS faixa_salarial
FROM funcionarios;
```

O SQL verifica as condições na ordem em que aparecem e retorna o resultado da primeira condição verdadeira.

---

## 7. JOIN

JOIN é utilizado para combinar informações de duas ou mais tabelas relacionadas.

### INNER JOIN

Retorna apenas os registros que possuem correspondência nas duas tabelas.

```sql
SELECT
    f.nome,
    d.nome_departamento
FROM funcionarios f
INNER JOIN departamentos d
    ON f.id_departamento = d.id_departamento;
```

### LEFT JOIN

Retorna todos os registros da tabela da esquerda e os registros correspondentes da tabela da direita.

```sql
SELECT
    f.nome,
    d.nome_departamento
FROM funcionarios f
LEFT JOIN departamentos d
    ON f.id_departamento = d.id_departamento;
```

---

## 8. DISTINCT

O DISTINCT remove valores duplicados do resultado.

### Lista de departamentos

```sql
SELECT DISTINCT departamento
FROM funcionarios;
```

---

## 9. NULL

NULL representa ausência de valor ou valor desconhecido.

Para verificar valores NULL, deve-se utilizar `IS NULL` ou `IS NOT NULL`.

### Consulta de valores NULL

```sql
SELECT *
FROM funcionarios
WHERE departamento IS NULL;
```

---

## 10. Boas práticas

* Evitar utilizar `SELECT *` quando apenas algumas colunas são necessárias.
* Utilizar nomes de tabelas e colunas claros.
* Utilizar aliases para facilitar a leitura das consultas.
* Organizar consultas maiores em linhas e blocos.
* Utilizar filtros adequados para evitar consultas desnecessariamente pesadas.
* Sempre verificar se os JOINs estão sendo realizados pelas colunas corretas.

## 11. Regra do DataAssist

Quando uma dúvida sobre SQL puder ser respondida com os conhecimentos desta base, o DataAssist deve priorizar essas informações.

Quando a pergunta estiver fora da base de conhecimento ou exigir informações que não estejam disponíveis, o DataAssist deve informar sua limitação em vez de inventar uma resposta.
