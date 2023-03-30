import subprocess
import openai

openai.api_key = "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"

# executa o comando recebido
def executeShellCommand(command):
    try:
        # Executa o comando shell no prompt do Windows
        output = subprocess.run(command, shell=True, check=True)
        # printa a saída do comando
        print(output)
    except subprocess.CalledProcessError as e:
        # Caso ocorra um erro, retorna o código de erro e a saída de erro
        print (f"Erro {e.returncode}: {e.output.decode('utf-8')}")

# obtém um comando gerado pelo ChatGPT a partir de uma descrição do comando
def generateCommand(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Escreva um comando shell do windows que faça o seguinte: {texto}",
        temperature=0.7,
        max_tokens=3072,
        stop=None
    )
    return response['choices'][0]['text']

# pega a descrição do comando do usuário
commandDescription = input("Descreva o comando que deseja executar: ")

# chama função que gera o comando a partir da descrição
commandGenerated = generateCommand(commandDescription)

# remove linhas em branco do início do comando
commandGenerated = commandGenerated.lstrip('\n\n')

# mostra o comando gerado e pergunta ao usuário se deseja executar
print(f"Comando gerado: {commandGenerated}")
if(input("Executar? (y/n) ") == 'y'):
    executeShellCommand(commandGenerated)