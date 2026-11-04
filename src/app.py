import re
import streamlit as st
from pathlib import Path
from ollama import chat


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="DataAssist",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# CAMINHO DA BASE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CARREGAR BASE DE CONHECIMENTO
# ============================================================

def carregar_base_conhecimento():

    arquivos = [
        "sql.md",
        "powerbi.md",
        "excel.md",
        "python.md"
    ]

    conhecimento = {}

    for arquivo in arquivos:

        caminho = DATA_DIR / arquivo

        if caminho.exists():

            conhecimento[arquivo] = caminho.read_text(
                encoding="utf-8"
            )

    return conhecimento


base_conhecimento = carregar_base_conhecimento()


# ============================================================
# TÓPICOS SUPORTADOS
# ============================================================

TOPICOS = {

    "sql.md": [
        "select",
        "where",
        "order by",
        "group by",
        "count",
        "sum",
        "avg",
        "min",
        "max",
        "case when",
        "inner join",
        "left join",
        "distinct",
        "null"
    ],

    "powerbi.md": [
        "power bi",
        "powerbi",
        "dax",
        "medida",
        "measure",
        "calculate",
        "power query",
        "tabela fato",
        "tabela dimensão",
        "dimensão",
        "cardinalidade",
        "relacionamento",
        "modelo estrela",
        "esquema estrela"
    ],

    "excel.md": [
        "excel",
        "soma",
        "média",
        "media",
        "contagem",
        "se",
        "cont.se",
        "somase",
        "procx",
        "procv",
        "xlookup",
        "vlookup",
        "tabela dinâmica",
        "filtro"
    ],

    "python.md": [
        "python",
        "variável",
        "variavel",
        "tipo de dado",
        "lista",
        "for",
        "função",
        "funcao",
        "pandas",
        "dataframe",
        "csv"
    ]
}


# ============================================================
# TÓPICOS AINDA NÃO SUPORTADOS
# ============================================================

TOPICOS_NAO_SUPORTADOS = {

    "sql.md": [
        "right join",
        "full join",
        "full outer join",
        "cross join",
        "self join"
    ]
}


# ============================================================
# NORMALIZAR TEXTO
# ============================================================

def normalizar_texto(texto):

    return texto.lower().strip()


# ============================================================
# VERIFICAR TERMO NA PERGUNTA
# ============================================================

def termo_na_pergunta(termo, pergunta):

    termo = normalizar_texto(termo)
    pergunta = normalizar_texto(pergunta)

    if " " in termo:

        return termo in pergunta

    padrao = rf"\b{re.escape(termo)}\b"

    return re.search(
        padrao,
        pergunta
    ) is not None


# ============================================================
# IDENTIFICAR ASSUNTO
# ============================================================

def identificar_assunto(pergunta):

    pontuacao = {}

    for arquivo, topicos in TOPICOS.items():

        pontuacao[arquivo] = 0

        for topico in topicos:

            if termo_na_pergunta(
                topico,
                pergunta
            ):

                pontuacao[arquivo] += 1

    maior_pontuacao = max(
        pontuacao.values()
    )

    if maior_pontuacao == 0:

        return None

    for arquivo, pontos in pontuacao.items():

        if pontos == maior_pontuacao:

            return arquivo

    return None


# ============================================================
# IDENTIFICAR TÓPICOS DA PERGUNTA
# ============================================================

def identificar_topicos_da_pergunta(
    pergunta,
    assunto
):

    topicos_encontrados = []

    for topico in TOPICOS.get(
        assunto,
        []
    ):

        if termo_na_pergunta(
            topico,
            pergunta
        ):

            topicos_encontrados.append(
                topico
            )

    return topicos_encontrados


# ============================================================
# VALIDAR TÓPICOS NA BASE
# ============================================================

def validar_topicos_na_base(
    pergunta,
    assunto
):

    contexto = base_conhecimento.get(
        assunto,
        ""
    ).lower()

    topicos_mencionados = (
        identificar_topicos_da_pergunta(
            pergunta,
            assunto
        )
    )

    topicos_nao_documentados = []

    for topico in topicos_mencionados:

        if topico not in contexto:

            topicos_nao_documentados.append(
                topico
            )

    return (
        topicos_mencionados,
        topicos_nao_documentados
    )


# ============================================================
# GERAR RESPOSTA
# ============================================================

def gerar_resposta(pergunta):

    assunto = identificar_assunto(
        pergunta
    )

    # --------------------------------------------------------
    # TÓPICOS NÃO SUPORTADOS
    # --------------------------------------------------------

    pergunta_normalizada = (
        pergunta.lower()
    )

    for topico in TOPICOS_NAO_SUPORTADOS.get(
        assunto,
        []
    ):

        if topico in pergunta_normalizada:

            return (
                "🤖 Essa informação não está disponível "
                "na minha base de conhecimento.\n\n"
                f"O tópico **{topico.upper()}** ainda não "
                f"está documentado na base de "
                f"**{assunto.replace('.md', '').upper()}**."
            ), None


    # --------------------------------------------------------
    # ASSUNTO NÃO IDENTIFICADO
    # --------------------------------------------------------

    if assunto is None:

        return (
            "🤖 Ainda não encontrei informações suficientes "
            "na minha base de conhecimento para responder "
            "essa pergunta.\n\n"
            "Atualmente, posso ajudar principalmente com "
            "**SQL, Power BI, Excel e Python**."
        ), None


    contexto = base_conhecimento.get(
        assunto,
        ""
    )


    # --------------------------------------------------------
    # VALIDAR TÓPICOS
    # --------------------------------------------------------

    (
        topicos_mencionados,
        topicos_nao_documentados
    ) = validar_topicos_na_base(
        pergunta,
        assunto
    )


    if topicos_nao_documentados:

        topicos = ", ".join(
            f"`{topico}`"
            for topico in topicos_nao_documentados
        )

        return (
            "🤖 Essa informação não está disponível "
            "na minha base de conhecimento.\n\n"
            f"O tópico {topicos} ainda não está "
            f"documentado na base de "
            f"**{assunto.replace('.md', '').upper()}**."
        ), None


    # --------------------------------------------------------
    # NOME DA BASE
    # --------------------------------------------------------

    nome_base = assunto.replace(
        ".md",
        ""
    ).upper()


    # --------------------------------------------------------
    # PROMPT
    # --------------------------------------------------------

    prompt = f"""
Você é o DataAssist, um assistente especializado
em análise de dados.

Sua função é ajudar estudantes e profissionais
juniores com:

- SQL
- Power BI
- Excel
- Python

REGRAS OBRIGATÓRIAS:

1. A BASE DE CONHECIMENTO abaixo é sua única fonte.

2. Utilize SOMENTE informações presentes na base.

3. NÃO utilize conhecimento externo.

4. NÃO invente informações.

5. NÃO complemente a resposta com informações
   que não estejam na base.

6. Se a informação necessária não estiver
   no contexto, diga:

"Essa informação não está disponível
na minha base de conhecimento."

7. Seja didático e objetivo.

8. Quando houver código, explique as partes
   mais importantes.

9. Não crie exemplos que dependam de informações
   externas à base.

10. Priorize precisão em vez de tentar responder
    a qualquer custo.

BASE DE CONHECIMENTO:

{contexto}

PERGUNTA:

{pergunta}
"""


    # --------------------------------------------------------
    # OLLAMA
    # --------------------------------------------------------

    resposta = chat(

        model="qwen2.5:3b",

        messages=[

            {
                "role": "system",
                "content": (
                    "Você é o DataAssist. "
                    "Responda de forma objetiva, "
                    "didática e utilize exclusivamente "
                    "o contexto fornecido."
                )
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        options={
            "temperature": 0.2
        }
    )


    return (
        resposta.message.content,
        nome_base
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 DataAssist")

    st.markdown(
        "### Assistente de Dados"
    )

    st.write(
        "Mentor virtual para estudantes "
        "e profissionais juniores."
    )

    st.divider()

    st.markdown(
        "### 🧠 Modelo"
    )

    st.write(
        "`Qwen 2.5 3B`"
    )

    st.markdown(
        "### 📚 Bases disponíveis"
    )

    st.write(
        "✅ SQL\n\n"
        "✅ Power BI\n\n"
        "✅ Excel\n\n"
        "✅ Python"
    )

    st.divider()

    st.markdown(
        "### 💡 Exemplos"
    )

    st.caption(
        "• O que é uma tabela fato?"
    )

    st.caption(
        "• Como funciona o CASE WHEN?"
    )

    st.caption(
        "• O que é uma medida no Power BI?"
    )

    st.caption(
        "• Como funciona um DataFrame?"
    )

    st.divider()

    if st.button(
        "🗑️ Limpar conversa",
        use_container_width=True
    ):

        st.session_state.mensagens = []

        st.rerun()


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🤖 DataAssist")

st.subheader(
    "Seu assistente de análise de dados"
)

st.write(
    "Olá! Eu sou o DataAssist. "
    "Posso ajudar com **SQL, Power BI, Excel e Python**."
)


# ============================================================
# HISTÓRICO
# ============================================================

if "mensagens" not in st.session_state:

    st.session_state.mensagens = []


for mensagem in st.session_state.mensagens:

    with st.chat_message(
        mensagem["role"]
    ):

        st.markdown(
            mensagem["content"]
        )


# ============================================================
# PERGUNTA
# ============================================================

pergunta = st.chat_input(
    "Digite sua pergunta..."
)


if pergunta:

    st.chat_message(
        "user"
    ).markdown(
        pergunta
    )

    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )


    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "🤖 Pensando..."
        ):

            resposta, fonte = gerar_resposta(
                pergunta
            )

        if fonte:

            st.caption(
                f"🧠 Fonte: Base de conhecimento — {fonte}"
            )

        st.markdown(
            resposta
        )


    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )