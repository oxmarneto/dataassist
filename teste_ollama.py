from ollama import chat

resposta = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Explique em uma frase o que é uma tabela fato."
        }
    ]
)

print(resposta.message.content)