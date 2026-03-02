# CRIANDO O CLIENTE USANDO A API DA OPENAI

from openai import OpenAI

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)

cliente = OpenAI(api_key="") # CRIANDO O CLIENTE

resposta = cliente.chat.completions.create( # VAMOS CRIAR UM CHAT, E PEDIR A API DE COMPLETIONS, MAS VAMOS CRIAR A NOSSA PRÓPRIA. NÃO ACEITAR A SUGESTÃO DA IA DE ASSISTÊNCIA
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # SYSTEM INSTRUCTIONS
        {"role": "user", "content": prompt}
    ]
)

print(resposta)

roteiro_viagem = resposta.choices[0].message.content
print(roteiro_viagem)
