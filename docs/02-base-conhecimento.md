# Base de Conhecimento do DataAssist

## 1. Objetivo

A base de conhecimento do DataAssist reúne informações estruturadas sobre os principais temas utilizados pelo assistente.

O objetivo é fornecer um contexto confiável para que o DataAssist consiga responder dúvidas de forma consistente, didática e adequada ao público-alvo.

---

## 2. Estrutura

A base está organizada por tecnologia:

```text
data/
├── sql.md
├── powerbi.md
├── excel.md
└── python.md
```

Cada arquivo contém conceitos, exemplos, boas práticas e regras relacionadas à respectiva tecnologia.

---

## 3. Conteúdo da base

### SQL

O arquivo `sql.md` contém conceitos como:

* SELECT
* WHERE
* ORDER BY
* GROUP BY
* Funções de agregação
* CASE WHEN
* JOIN
* DISTINCT
* NULL
* Boas práticas

### Power BI

O arquivo `powerbi.md` contém conceitos como:

* Tabelas fato e dimensão
* Relacionamentos
* Cardinalidade
* Medidas
* DAX
* Power Query
* Modelo em estrela
* Boas práticas

### Excel

O arquivo `excel.md` contém conceitos como:

* Fórmulas e funções
* SE
* PROCV e PROCX
* Tabelas dinâmicas
* Filtros
* Formatação condicional
* Power Query
* Boas práticas

### Python

O arquivo `python.md` contém conceitos como:

* Variáveis
* Tipos de dados
* Condições
* Listas
* Estruturas de repetição
* Funções
* Pandas
* Leitura de arquivos
* Boas práticas

---

## 4. Utilização pelo agente

A base de conhecimento será utilizada como fonte de contexto para as respostas do DataAssist.

O fluxo esperado é:

```text
Pergunta do usuário
        ↓
Identificação do assunto
        ↓
Busca na base de conhecimento
        ↓
Recuperação das informações relevantes
        ↓
Envio do contexto para o modelo de IA
        ↓
Geração da resposta
        ↓
Resposta ao usuário
```

---

## 5. Controle de qualidade

O DataAssist deve priorizar informações presentes na base de conhecimento.

Quando a informação necessária não estiver disponível, o agente deve reconhecer sua limitação em vez de criar uma resposta sem fundamento.

A base também poderá ser expandida futuramente com novos conteúdos, exemplos e tecnologias.

---

## 6. Evolução da base

A base de conhecimento foi criada de forma modular para facilitar sua manutenção.

Novos arquivos podem ser adicionados conforme o DataAssist evoluir.

Exemplos de futuras extensões:

```text
data/
├── sql.md
├── powerbi.md
├── excel.md
├── python.md
├── azure.md
└── estatistica.md
```

A expansão deve manter a organização por assunto e priorizar conteúdos relevantes para análise de dados.
