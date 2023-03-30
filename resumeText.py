import openai

openai.api_key = "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"

# Obtém o conteúdo de um arquivo a partir de um nome de arquivo
def leArquivo(nomeArquivo):
    # Abrir o arquivo em modo de leitura
    with open(nomeArquivo, 'r') as file:
        # Ler o conteúdo do arquivo em uma variável
        conteudo = file.read()
        # Exibir o conteúdo do arquivo
        return conteudo
    
# Obtém um texto resumido pelo ChatGPT
def resumeTexto(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Faça um resumo do seguinte texto: {texto}",
        temperature=0.8,
        max_tokens=3072
    )
    return response['choices'][0]['text']

texto = leArquivo("arquivo.txt")
resumo = resumeTexto(texto)

print("********Texto original********")
print(texto)

print("********Texto resumido********")
print(resumo)

